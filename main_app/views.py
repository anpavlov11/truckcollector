from unicodedata import name
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Truck

import truckcollector_project

class Home(View):
    def get(truck, request):
        return HttpResponse('Truck Collector Home')

class Home(TemplateView):
    template_name = 'home.html'

class About(View):
    def get(truck, request):
        return HttpResponse('Truck Collector About')

class About(TemplateView):
    template_name = 'about.html'

# class TruckList(View):
#     def __init__(truck, name, coolStuff, image):
#         truck.name = name
#         truck.coolStuff = coolStuff
#         truck.image = image
        
#         Truck = [
#             Truck('2019', 'Ram', '1500', 'I drive a 2019 Ram 1500. My truck has a name--Stevie like Stevie Nicks. My truck has also be moderatley modified. I have done all the aftermarket modifications myself.', 'https://i.imgur.com/wYZiK58.jpg')
#         ]

class TruckList(TemplateView):
    template_name = 'truck_list.html'

    def get_context_data(truck, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trucks'] = Truck.objects.all()
        return context