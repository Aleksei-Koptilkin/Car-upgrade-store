from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

# Create your views here.



model_car_dict = {
    'bmwm5e39': {
        'model': 'BMW M5 E39',
        'production_years': 'Годы выпуска: c 1998 по 2003',
        'engine_info': 'Двигатель: S62B50 объемом 4.9 л. и мощностью 394 л.с.',
    },
    'bmwm5e60': {
        'model': 'BMW M5 E60',
        'production_years': 'Годы выпуска: с 2003 по 2010',
        'engine_info': 'Двигатель: S85B50 объемом 5.0 л. и мощностью 507 л.с.',
    },
    'mercedese55': {
        'model': 'Mercedes-Benz E55 AMG',
        'production_years': 'Годы выпуска: с 1997 по 1999',
        'engine_info': 'Двигатель: M113 E55 объемом 5.5 л. и мощностью 354 л.с.',
    },
    'nissans15': {
        'model': 'Nissan Silvia S15 Spec-R',
        'production_years': 'Годы выпуска: с 1999 по 2001',
        'engine_info': 'Двигатель SR20DET объемом 2 л. и мощностью 250 л.с.',
    },
}
def cars(request):
    data = {
        'cars': model_car_dict
    }
    return render(request, 'legend_cars/list_cars.html', context=data )
def get_info_car_model(request, model_car):
    data = {
        'path': 'legend_cars/car_info.html',
        'model': model_car_dict[model_car]['model'],
        'production_years': model_car_dict[model_car]['production_years'],
        'engine_info': model_car_dict[model_car]['engine_info'],
    }
    if model_car in model_car_dict:
        return render(request, data['path'], context=data)
    else:
        return HttpResponseNotFound(f'Автомобиль {model_car} пока отсутствует.')