from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse

from .models import ChunkedUpload


@csrf_exempt
def create_media(request):
    return render(request, 'temp_media/media_form.html')

@csrf_exempt
def file_upload(request):
        data = request.POST
        chunk = request.FILES.get('chunk')
        upload_id = data.get('upload_id')

        if upload_id and upload_id != 'null':
            upload = ChunkedUpload.objects.get(id=upload_id)
        else:
            filename = data.get('filename')
            total_size = int(data.get('total_size'))
            upload = ChunkedUpload.objects.create(filename=filename, total_size=total_size)

        upload.append_chunk(chunk)
        upload.check_completion()

        if upload.status == 'completed':

            return JsonResponse({
                'upload_id': upload.id,
                'status': upload.status,
                'file_url': upload.file.url,
            })
        else:
            # If the upload is not complete, return a response with the current offset
            return JsonResponse({
                'upload_id': upload.id,
                'status': upload.status,
                'offset': upload.offset,
            })
