from rest_framework import serializers
from files.models import FileItem
from accounts.models import FileShareAppUser
from accounts.serializers import FileShareAppUserSerializer

class FileItemSerializer(serializers.HyperlinkedModelSerializer): 
    #file_uploader = FileShareAppUserSerializer(read_only=True)
    #file_downloader = FileShareAppUserSerializer(read_only=False)

    class Meta:
        model = FileItem
        fields = ('url','id','file_uploader', 'file_downloader', 'file_file', 'file_desc','file_name',)

        extra_kwargs = {'file_uploader':{'read_only':True}}


        def validate_file_downloader(self, file_downloader):
            downloader_obj = FileShareAppUser.objects.get( id = int(file_downloader.split('/')[-2]))
            if not file_downloader.is_file_downloader:
                raise serializers.ValidationError(
                    _('selected user is not uploader')
                    )
            return file_downloader

        # def create(self, validated_data):
        #     file_obj = FileItem(
        #         file_uploader = self.request.user,
        #         file_downloader = validated_data['file_downloader'],
        #         file_file = validated_data['file_file'],
        #         file_desc = validated_data['file_desc'],
        #         file_name = validated_data['file_name'],
        #         )
        #     file_obj.save()
        #     return file_obj