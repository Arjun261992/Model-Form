from django.shortcuts import render, HttpResponseRedirect
from .forms import EmployeeRegistration
from .models import employees
from django.contrib import messages

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        fm = employees(first_name=first_name, last_name=last_name, email=email,phone=phone)
        fm.save()
        messages.success(request, 'Your Information is stored')
        
    else:
        request.method == ''
    stud= employees.objects.all()
    
    
    return render(request, 'cd/addandshow.html', {'stu':stud})
def delete_data(request,id):
    if request.method == 'POST':
        pi = employees.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
