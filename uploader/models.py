from django.db import models


class MediaUser(models.Model):
	file = models.ImageField(upload_to='')

	class Meta:
		verbose_name = 'Media'
		verbose_name_plural = 'Medias'

	def __str__(self):
		return self.file.name

