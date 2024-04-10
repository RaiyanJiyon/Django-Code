from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import StudentRegistration

def thankyou(request):
    return render(request, 'enroll/success.html')

def showuserdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print("Request Comes From Post Method.")
  
            print('First Name:', fm.cleaned_data['firstname'])

            print('Last Name:', fm.cleaned_data['lastname'])

            print('Nickname:', fm.cleaned_data['nickname'])

            print('Roll:', fm.cleaned_data['roll'])

            print('Fees:', fm.cleaned_data['fees'])

            print('CGPA:', fm.cleaned_data['CGPA'])

            print('Comment:', fm.cleaned_data['comment'])

            print('Email:', fm.cleaned_data['email'])

            print('Website:', fm.cleaned_data['website'])

            print('Password:', fm.cleaned_data['password'])

            print('Description:', fm.cleaned_data['description'])

            print('Feedback:', fm.cleaned_data['feedback'])

            print('Notes:', fm.cleaned_data['notes'])
            
            print('Agree:', fm.cleaned_data['agree'])
            
        else:
            print("Form data is not valid.")
    else:
        print("Request Comes From Get Method.")
        fm = StudentRegistration()
        
    return render(request, 'enroll/userreg.html', context={'form': fm})
