from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('projects/aventura-hospital', AventuraHospiltal, name='aventura-hospital'),
    path('projects/memorial-hospital', MemorialHospiltal, name='memorial-hospital'),
    path('projects/leon-medical-center', LeonMedicalCenter, name='leon-medical-center'),
    path('projects/JFK-hospital', JFKHospital, name='jfk-hospital'),
    path('projects/general-palmetto-hospital', GeneralPalmettoHospital, name='general-palmetto-hospital'),
    path('projects/Telemundo', Telemundo, name='telemundo'),
    ]
