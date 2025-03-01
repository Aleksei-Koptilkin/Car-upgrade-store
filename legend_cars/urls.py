from django.urls import path, include
from . import views


app_name = 'legend_cars'

urlpatterns = [
    path('', views.Cars.as_view(), name='car_selection'),
    path('<slug:slug_car>', views.CarInfo.as_view(), name='car_url')
]
