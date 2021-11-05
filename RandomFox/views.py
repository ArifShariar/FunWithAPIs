from django.shortcuts import render
import requests


# Create your views here.
def randomFox(request):
    response = requests.get('https://randomfox.ca/floof/')
    fox_images = response.json()
    context = {'images': fox_images['image']}
    return render(request, 'RandomFox/randomFox.html', context)
