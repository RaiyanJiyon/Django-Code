from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('Request comes from POST method.')

            print('Name:', fm.cleaned_data['name'])
            print('Email:', fm.cleaned_data['email'])
            print('Password:', fm.cleaned_data['password'])
    else:
        fm = StudentRegistration()
        print('Request comes from get method.')
        
    return render(request, 'enroll/userreg.html', context={'form':fm})
