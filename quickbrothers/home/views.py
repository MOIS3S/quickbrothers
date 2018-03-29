from django.shortcuts import render


def index(request):
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
