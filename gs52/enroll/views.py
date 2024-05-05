from django.shortcuts import render
from enroll.forms import StudentRegistration
from .models import User

# Create your views here.

# another way to update data
def showuserdata(request):
    if request.method == 'POST':
        pi = User.objects.get(pk=1)
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
             fm.save()
    else:
            fm = StudentRegistration()
            print("Request comes from get method")
    
    return render(request, 'enroll/userreg.html', context={'form': fm})