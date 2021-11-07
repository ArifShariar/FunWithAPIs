import json

from django.shortcuts import render


def weather(request):
    with open('Weather/files/bd_districts.json', encoding='utf-8') as json_file:
        data = json.load(json_file)

    districts = []
    k = 1
    while k <= 63:
        districts.append(data['districts'][k]['name'])
        k += 1
    context = {'districts': districts}
    return render(request, 'Weather/weather.html', context)
