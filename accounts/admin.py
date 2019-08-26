from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import FileShareAppUserCreationForm, FileShareAppUserChangeForm
from .models import FileShareAppUser

class FileShareAppUserAdmin(UserAdmin):
    add_form = FileShareAppUserCreationForm
    form = FileShareAppUserChangeForm
    model = FileShareAppUser
    list_display = ['email', 'username','is_file_uploader','is_file_downloader']
    list_editable = ('is_file_uploader','is_file_downloader')

admin.site.register(FileShareAppUser, FileShareAppUserAdmin)