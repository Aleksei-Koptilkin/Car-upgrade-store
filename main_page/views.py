from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

# Create your views here.

def main_page(requset):
    return render(requset, 'main_page/main_page.html')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')