from django.urls import path, include
from . import views


app_name = 'main_page'

urlpatterns = [
    path('', views.main_page, name='main_page'),
]