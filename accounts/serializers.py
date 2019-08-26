from rest_framework import serializers
from accounts.models import FileShareAppUser



class FileShareAppUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FileShareAppUser
        fields = ('url','id', 'username','email', 'password', 'is_file_uploader', 'is_file_downloader',)

        extra_kwargs = {'password': {'write_only': True},}


    def create(self, validated_data):

        user = FileShareAppUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user