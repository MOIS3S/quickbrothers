from django.shortcuts import render
from django.core.mail import send_mail
from .forms import *


def index(request):
    if request.method == 'POST':
        form = SendEmailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            text = 'Nombre: {}  Email: {}  Mensaje: {}'.format(name, email, message)
            send_mail(name, text, email, ['wallprotection@quickbrothersinc.net'])
            return render(request, 'index.html')
        else:
            form = SendEmailForm()
            return render(request, 'index.html', {'form':form})
    else:
        return render(request, 'index.html')

def AventuraHospiltal(request):
    return render(request, 'projects/aventura-hospital.html')

def MemorialHospiltal(request):
    return render(request, 'projects/memorial-hospital.html')

def LeonMedicalCenter(request):
    return render(request, 'projects/leon-medical-center.html')

def JFKHospital(request):
    return render(request, 'projects/jfk-hospital.html')

def GeneralPalmettoHospital(request):
    return render(request, 'projects/general-palmetto-hospital.html')

def Telemundo(request):
    return render(request, 'projects/telemundo.html')
