from django.urls import path, include
from . import views


app_name = 'legend_cars'

urlpatterns = [
    path('', views.cars, name='car_selection'),
    path('<int:id_car>', views.get_info_car_model, name='car_url')
]
