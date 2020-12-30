from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .facialRecog import facial_recognition

import time
import json
import os
from PIL import Image

from distComputing.settings import BASE_DIR

def facialRecog(request):
    if request.method == 'POST':
        try:
            image = request.FILES.get('img', None)
            if image:
                image = convert(image)
                if image is None:
                    return HttpResponse('[error] POST data should be image file.')
                result = facial_recognition(image)
                return JsonResponse({'result': result})
            else:
                return HttpResponse('[error] Empty image file.')
        except Exception as err:
            return HttpResponse('[error] POST data is incompatible.')
    else:
        return HttpResponse('[error] Request method should be POST.')

def convert(image_file):
    """
    Convert image file from type <class 'django.core.files.uploadedfile.InMemoryUploadedFile'> 
    to <class ???>
    """
    
    file_name = os.path.join(BASE_DIR, 'img', 'img_'+str(int(time.time()))+'.'+image_file.name.split('.')[-1])
    if image_file.name.split('.')[-1] not in ['jpeg','jpg','png']:
        return None
    with open(file_name, 'wb+') as fp:
        fp.write(image_file.read())

    # return Image.open(file_name)
    return file_name
