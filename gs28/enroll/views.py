from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def showformdetails(request):
    fm = StudentRegistration()
    return render(request, 'enroll/sturegistration.html', context={'form': fm})
