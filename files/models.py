from django.db import models
from accounts.models import FileShareAppUser

from django_s3_storage.storage import S3Storage

storage = S3Storage(aws_s3_bucket_name='s3-bucket-name')




class FileItem(models.Model):
    file_uploader = models.ForeignKey(FileShareAppUser, on_delete=models.CASCADE,related_name= 'file_uploader')
    file_downloader = models.ForeignKey(FileShareAppUser, on_delete=models.CASCADE, related_name= 'file_downloader')
    file_file = models.FileField(storage=storage)
    file_desc = models.TextField(blank=True)
    file_name = models.CharField(max_length=20,blank=False,default="file_test")


    
    def __str__(self):
        return self.item_name