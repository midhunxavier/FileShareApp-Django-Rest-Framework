from rest_framework import viewsets
from files.serializers import FileItemSerializer
from files.models import FileItem
from accounts.models import FileShareAppUser

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from files.permissions import IsFileDownloader, IsFileUploader, IsAdminUser
from django.core.mail import send_mail
from django.conf import settings

class FileItemViewSet(viewsets.ModelViewSet):
    queryset = FileItem.objects.all()
    serializer_class = FileItemSerializer

    def create(self, request, *args, **kwargs):
        downloader= request.data['file_downloader']
        downloader_obj = FileShareAppUser.objects.get( id = int(downloader.split('/')[-2]))
        
        if not downloader_obj.is_file_downloader:
            return Response({'message': 'recipient cant download'},status= HTTP_404_NOT_FOUND)

        serializer_context = {
                        'request': request,
                                }
        serializer = FileItemSerializer(data=request.data,context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(file_uploader= self.request.user)

        subject = 'File Shared'
        message = 'Hi {0}, \n\nI have share a file with you.\n\n Regards,\n{1}'.format(downloader_obj.username,request.user.username)
        email_from = 'midhunayyanthole@gmail.com'
        recipient_list = [downloader_obj.email,]
        try:
            send_mail( subject, message, email_from, recipient_list ,fail_silently=False)
        except:
            return Response({'message': 'Recipient is not added to authorized maillist'},status= HTTP_200_OK)


        return Response(serializer.data)


    # def perform_create(self, serializer):
    #     serializer.save(file_uploader=self.request.user)
        
        
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsFileUploader]
        elif self.action == 'retrive':
            permission_classes = [IsFileDownloader]
        elif self.action == 'list':
            permission_classes = [IsFileUploader]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
        


@api_view(['GET'])
def upload_history_file_list(request):
 
    if request.method == 'GET':
        user_name = request.user.username
        queryset = FileItem.objects.filter(file_uploader__username=user_name)
        serializer_context = {
                        'request': request,
                                }
        serializer = FileItemSerializer(queryset,context=serializer_context,many=True)
        return Response(serializer.data)


@api_view(['GET'])
def download_history_file_list(request):
 
    if request.method == 'GET':
        user_name = request.user.username
        queryset = FileItem.objects.filter(file_downloader__username=user_name)
        serializer_context = {
                        'request': request,
                                }
        serializer = FileItemSerializer(queryset,context=serializer_context,many=True)
        return Response(serializer.data)