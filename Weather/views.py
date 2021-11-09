import json

from django.http import HttpResponse
from django.shortcuts import render


def weather(request):
    with open('Weather/files/bd_districts.json', encoding='utf-8') as json_file:
        data = json.load(json_file)

    districts = []
    k = 1
    while k <= 63:
        districts.append(data['districts'][k]['name'])
        k += 1
    districts.sort()
    context = {'districts': districts}
    if request.POST:
        district = request.POST.get('selectDistrict')
        print(district)
        return render(request, 'Weather/weather.html', context)
    else:

        return render(request, 'Weather/weather.html', context)


def weatherForecast(request):
    district = request.POST.get('selectDistrict')
    print(district)
    return HttpResponse(district)