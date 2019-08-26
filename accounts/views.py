from rest_framework import viewsets
from accounts.serializers import FileShareAppUserSerializer
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
from accounts.permissions import IsLoggedInUserOrAdmin, IsAdminUser




class FileShareAppUserViewSet(viewsets.ModelViewSet):

    queryset = FileShareAppUser.objects.all()
    serializer_class = FileShareAppUserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'retrieve':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

