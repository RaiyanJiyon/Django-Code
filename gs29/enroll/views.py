from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def showformsdetails(request):
    fm = StudentRegistration(auto_id=True, label_suffix="-", initial={'name': 'sonam'})
    return render(request, 'enroll/sturegistration.html', context={"form": fm})
