from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        print('Data Comes From Post Method')
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            phone = fm.cleaned_data['phone']
            password = fm.cleaned_data['password']

            print('Name:', name)
            print('Email:', email)
            print('Phone:', phone)
            print('Password:', password)
        else:
            print('Form is not valid')
    else:
        print('Data Comes From Get Method')
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', context={'form':fm})
