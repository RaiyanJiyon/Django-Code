from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def showformsdetails(request):
    fm = StudentRegistration()
    fm.order_fields(field_order= ['first_name', 'last_name', 'email'])
    return render(request, 'enroll/sturegistration.html', context={"form": fm})
