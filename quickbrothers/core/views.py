from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.core.mail import EmailMessage
from django.http import JsonResponse
from .models import Project
from .forms import ContactForm


class ProjectListView(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project


def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            message = request.POST.get('message', '')
            email = EmailMessage(
                "Quickbrothers: Nuevo mensaje de contacto de sitio web",
                "De {} <{}>\n\n Escribio:\n\n {}".format(name, email, message),
                "no-contestar@inbox.mailtrap.io",
                ["moisescastillo20@gmail.com",
                 "wallprotection@quickbrothersinc.net"],
                reply_to=[email]
                )
            try:
                email.send()
                return JsonResponse({'success': True})
            except:
                return JsonResponse({'error': True})


def handler404(request, *args, **argv):
    return render(request, 'core/404.html', status='404')


def handler500(request, *args, **argv):
    return render(request, 'core/500.html', status='500')
