from django import forms
from django.core.validators import RegexValidator


class ContactForm(forms.Form):
    name = forms.CharField(required=True, min_length=3, max_length=100)
    email = forms.EmailField(required=True, min_length=3, max_length=100)
    phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
    message = forms.CharField(required=True, min_length=10, max_length=1000)
