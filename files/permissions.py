from rest_framework import permissions
from accounts.models import FileShareAppUser
from django.shortcuts import get_object_or_404


class IsFileUploader(permissions.BasePermission):
    
    def has_permission(self, request, view): 
        try:
            fileshareapp_user_obj = get_object_or_404(FileShareAppUser , id = request.user.id)
            is_uploader = fileshareapp_user_obj.is_file_uploader
        except:
            is_uploader = False
        return is_uploader 

class IsFileDownloader(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        try:
            file_downloader_obj = obj.file_downloader
            fileshareapp_user_obj = get_object_or_404(FileShareAppUser , id = request.user.id)
        except:
            return False
        return file_downloader_obj == fileshareapp_user_obj


class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff