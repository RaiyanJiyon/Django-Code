from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration

# Create your views here.

def thankyou(request):
    return render(request, 'enroll/successpage.html')


def showuserdata(request):
    if request.method == 'POST':
        print("Request Comes From Post Method.")
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']

            print('Name:', name)
            print('Email:', email)
            print('Password:', password)

            # we can do this way also
            # return render(request, 'enroll/successpage.html', context={'nm': name})

            # but recommonded way is this one
            return HttpResponseRedirect('/reg/success/')
    
    else:
        print("Requet Comes From Get Method.")
        fm = StudentRegistration()
        
    return render(request, 'enroll/userreg.html', context={'form':fm})
