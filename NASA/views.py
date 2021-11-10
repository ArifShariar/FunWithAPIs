from django.shortcuts import render


def NASA(request):
    return render(request, 'NASA/NASA.html')
