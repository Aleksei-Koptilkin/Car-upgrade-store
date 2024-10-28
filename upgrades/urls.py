from django.urls import path, include
from . import views


app_name = 'upgrades'

urlpatterns = [
    path('', views.upgrades, name='upgrades_selection'),
]