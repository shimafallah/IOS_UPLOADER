from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db import models


class MediaUser(models.Model):
	file = models.ImageField(upload_to='')

	class Meta:
		verbose_name = 'Media'
		verbose_name_plural = 'Medias'

	def __str__(self):
		return self.file.name


@receiver(post_delete, sender=MediaUser)
def delete_media_file(sender, instance, **kwargs):
    instance.file.delete(False) 
