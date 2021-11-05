import os
import re

from django.shortcuts import render
import requests
from .models import Fox
import cv2


# Create your views here.
def randomFox(request):
    response = requests.get('https://randomfox.ca/floof/')
    fox_images = response.json()
    context = {'images': fox_images['image']}
    numbers = re.findall('[0-9]+', fox_images['link'])
    res = requests.get(fox_images['image'])
    file_name = 'fox' + numbers[0] + '.jpg'
    with open(file_name, 'wb') as f:
        f.write(res.content)
        f.close()
    fox = Fox()
    fox.id_from_web = numbers[0]
    fox.link_from_web = fox_images['link']
    # ERROR:file name is a string, not a file object
    fox.image_form_web = file_name
    fox.save()
    os.remove(file_name)

    return render(request, 'RandomFox/randomFox.html', context)
