from django.shortcuts import render
from enroll.forms import StudentRegistration
from .models import User
# Create your views here.

def showuserdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']

            reg = User(name=nm, email=em, password=pw)
            reg.save()
      
            #if we want to update any particular data, then we have to define id
            # reg = User(id=1, name=nm, email=em, password=pw)
            # reg.save()

            # if we want to delete any particular data, then we have to define id
            # reg = User(id=1)
            # reg.delete()
    else:
            fm = StudentRegistration()
            print("Request comes from get method")
    
    return render(request, 'enroll/userreg.html', context={'form': fm})
