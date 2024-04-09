from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def showforminfo(request):
    fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', context={'form': fm})
