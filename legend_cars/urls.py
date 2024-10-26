from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cars),
    path('<str:model_car>', views.get_info_car_model)
]
