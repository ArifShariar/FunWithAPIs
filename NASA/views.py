from django.shortcuts import render


def NASA_astronomy_picture_of_the_day(request):
    return render(request, 'NASA/NASA.html')
