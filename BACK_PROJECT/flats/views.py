from django.shortcuts import render

# Create your views here.


def flat(request):
    return render(request, 'flats/flats.html')


def home(request):
    return render(request, 'home/home.html')
