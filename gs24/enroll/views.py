from django.shortcuts import render
from enroll.models import Student

# Create your views here.

def studentinfo(request):
    stud = Student.objects.all()
    # print("My Output", stud) -> for debugging
    return render(request, 'enroll/studetails.html', context={'stu': stud})