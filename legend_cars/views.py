from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView
from .models import Car

# Create your views here.


class Cars(ListView):
    model = Car
    template_name = 'legend_cars/list_cars.html'
    context_object_name = 'cars'
    ordering = 'car_brand'


class CarInfo(DetailView):
    model = Car
    template_name = 'legend_cars/car_info.html'
    slug_url_kwarg = 'slug_car'
