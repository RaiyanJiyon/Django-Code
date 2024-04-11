from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def showuserdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('Valid Request from POST method')

            print('Name:', fm.cleaned_data['name'])
            print('Email:', fm.cleaned_data['email'])
    
    else:
        fm = StudentRegistration()
        print('Invalid Request from Get method')
    
    return render(request, 'enroll/userreg.html', context={'form':fm})