import requests
from django.shortcuts import render


def NASA_astronomy_picture_of_the_day(request):
    context = {}
    req = requests.get('https://api.nasa.gov/planetary/apod?api_key=JbPh57ub5qcB6frjO0UHzsSxiySqwyiZe7b3WpZe')
    context['copyright'] = req.json()['copyright']
    context['title'] = req.json()['title']
    context['date'] = req.json()['date']
    context['explanation'] = req.json()['explanation']
    context['url'] = req.json()['url']
    context['hdurl'] = req.json()['hdurl']
    return render(request, 'NASA/NASA.html', context)
