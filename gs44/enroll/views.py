from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def showuserdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('Valid Post Request.')
            
            print('Name:', fm.cleaned_data['name'])
            print('Email:', fm.cleaned_data['email'])
            print('Password:', fm.cleaned_data['password'])
            print('Re-Password:', fm.cleaned_data['repassword'])
    else:
        fm = StudentRegistration()
        print('Comes from Get method.')
        
    return render(request, 'enroll/userreg.html', context={'form':fm})
