from django.urls import path

from .views import create_media, file_upload


app_name = 'uploader'

urlpatterns = [
	path('', create_media , name='create_media'),
	path('uploader/', file_upload , name='uploader'),
]
