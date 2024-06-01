from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import StudentRegistrations
from .models import User

# This Function Will Add new Item and Show All Items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistrations(request.POST)
        # Second way to save data
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistrations()  # Reset the form after successful submission
    else:
        fm = StudentRegistrations()
    
    # Fetch all student records regardless of POST or GET request
    stud = User.objects.all()
        
    return render(request, 'enroll/addandshow.html', context={'form': fm, 'stu': stud})

# This Function Will Update Data
def update_data(request, id):
    pi = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        fm = StudentRegistrations(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')  # Redirect after successful update
    else:
        fm = StudentRegistrations(instance=pi)

    return render(request, 'enroll/updatestudent.html', context={'form': fm})

# This Function Will Delete Data
def delete_data(request, id):
    if request.method == 'POST':
        pi = get_object_or_404(User, pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    # Optional: Handle GET request if you want to show a confirmation page
    return render(request, 'enroll/delete_confirmation.html', context={'id': id})

