from django.urls import path

from .views import create_media


app_name = 'uploader'

urlpatterns = [
	path('', create_media , name='create_media'),
]
