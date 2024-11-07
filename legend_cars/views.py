from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from .models import Car

# Create your views here.


def cars(request):
    data = {
        'cars': Car.objects.all()
    }
    return render(request, 'legend_cars/list_cars.html', context=data )

def get_info_car_model(request, id_car):
    car = get_object_or_404(Car, id=id_car)

    return render(request, 'legend_cars/car_info.html', context={'car':car})
