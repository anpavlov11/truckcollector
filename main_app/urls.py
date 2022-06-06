from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('trucks/', views.TruckList.as_view(), name='truck_list'),
    path('trucks/new/', views.TruckCreate.as_view(), name="truck_create"),
    path('trucks/<int:pk>/', views.TruckDetail.as_view(), name="truck_detail"),
    path('trucks/<int:pk>/update',views.TruckUpdate.as_view(), name="truck_update"),
    path('trucks/<int:pk>/delete',views.TruckDelete.as_view(), name="truck_delete"),
]