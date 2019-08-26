from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import FileShareAppUser

class FileShareAppUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = FileShareAppUser
        fields = ('username', 'email')

class FileShareAppUserChangeForm(UserChangeForm):

    class Meta:
        model = FileShareAppUser
        fields = ('username', 'email')