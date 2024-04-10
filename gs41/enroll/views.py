from django.shortcuts import render
from .forms import StudentRegistration

def thankyou(request):
    return render(request, 'enroll/success.html')

def showuserdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print("Request Comes From Post Method.")
  
            print('Name:', fm.cleaned_data['name'])
            print('Email:', fm.cleaned_data['email'])
            print('Password:', fm.cleaned_data['password'])
            
    else:
        print("Request Comes From Get Method.")
        fm = StudentRegistration()
        
    return render(request, 'enroll/userreg.html', context={'form': fm})