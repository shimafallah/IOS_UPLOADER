from django.shortcuts import redirect
from django.shortcuts import render

from .models import MediaUser


def create_media(request):
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        for file in files:
            MediaUser.objects.create(file=file)
        return redirect('uploader:create_media')
    
    return render(request, 'temp_media/media_form.html')
