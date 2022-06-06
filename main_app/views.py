from django.views.generic.base import TemplateView
from .models import Truck
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class TruckList(TemplateView):
    template_name = "truck_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context['trucks'] = Truck.objects.filter(name__icontains=name)
            context['header'] = f"Searching for {name}"
        else:
            context["trucks"] = Truck.objects.all()
            return context

class TruckCreate(CreateView):
    model = Truck
    fields = ['name', 'image', 'coolStuff']
    template_name = "truck_create.html"
    success_url = "/trucks/"

class TruckDetail(DetailView):
    model = Truck
    template_name = "truck_detail.html"

class TruckUpdate(UpdateView):
    model = Truck
    fields = ['name', 'image', 'coolStuff']
    template_name = "truck_create.html"
    success_url = "/trucks/"

class TruckDelete(DeleteView):
    model = Truck
    template_name = "truck_delete.html"
    success_url = "/trucks/"