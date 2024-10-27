from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.upgrades, name='upgrades_selection'),
]