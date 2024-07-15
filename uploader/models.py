from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from django.db.models.signals import post_delete
from django.core.files.base import ContentFile
from django.dispatch import receiver
from django.db import models
import os


class ChunkedUpload(models.Model):

    STATUS_CHOICES = [
        ('started', 'Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    filename = models.CharField(max_length=255)
    file = models.FileField(upload_to='')
    offset = models.BigIntegerField(default=0)
    total_size = models.BigIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='started')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def append_chunk(self, chunk):
        try:
            # If chunk is an InMemoryUploadedFile or TemporaryUploadedFile, read the data
            if isinstance(chunk, (InMemoryUploadedFile, TemporaryUploadedFile)):
                chunk = chunk.read()

            if self.file:
                # If a file has already been uploaded, append the chunk to it
                with open(self.file.path, 'ab') as destination:
                    # Seek to the end of the file to append the new chunk
                    destination.seek(0, os.SEEK_END)
                    destination.write(chunk)
            else:
                # If no file has been uploaded yet, create a new file with the chunk
                self.file.save(self.filename, ContentFile(chunk))

            # Update the offset
            self.offset = self.file.size
            self.save()

        except Exception as e:
            self.status = 'failed'
            self.save()
            raise e


    def check_completion(self):
        if self.offset >= self.total_size:
            self.status = 'completed'
            self.save()

    def __str__(self):
        return self.filename


@receiver(post_delete, sender=ChunkedUpload)
def delete_media_file(sender, instance, **kwargs):
    instance.file.delete(False) 
