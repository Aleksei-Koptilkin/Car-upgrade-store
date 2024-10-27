from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cars, name='car_selection'),
    path('<str:model_car>', views.get_info_car_model, name='car_url')
]
