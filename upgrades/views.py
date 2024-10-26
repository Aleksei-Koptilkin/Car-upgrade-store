from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def upgrades(request):
    return HttpResponse("<h1>Апгрейды для автомобилей<h1>")