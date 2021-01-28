from django import forms
from .models import employees
from django.core import validators

class EmployeeRegistration(forms.ModelForm):
  class meta:
    model= employees
    fields = ['first_name', 'last_name', 'email', 'phone']