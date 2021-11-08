import json

from django.shortcuts import render


def weather(request):
    if request.GET.get('selectDistrict'):
        district_name = request.GET.get('selectDistrict')
        print(district_name)
    with open('Weather/files/bd_districts.json', encoding='utf-8') as json_file:
        data = json.load(json_file)

    districts = []
    k = 1
    while k <= 63:
        districts.append(data['districts'][k]['name'])
        k += 1
    districts.sort()
    context = {'districts': districts}
    return render(request, 'Weather/weather.html', context)


def search(request):
    if request.method == 'POST':
        district_name = request.POST['district']
        print(district_name)