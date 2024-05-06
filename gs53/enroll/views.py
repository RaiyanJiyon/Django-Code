from django.shortcuts import render

# Create your views here.

def home(request, check):
    return render(request, 'enroll/home.html', context={'ch': check})

# def showdetails(request, my_id):
#     student = {'id': my_id}
#     return render(request, 'enroll/show.html', student)

def showdetails(request, my_id):
    if my_id == 1:
        student = {'id': my_id, 'name': 'Rohan'}
    if my_id == 2:
        student = {'id': my_id, 'name': 'Sonam'}
    if my_id == 3:
        student = {'id': my_id, 'name': 'Rahul'}
    return render(request, 'enroll/show.html', student)

def show_subdetails(request, my_id, my_subid):
    if my_id == 1 and my_subid == 5:
        student = {'id': my_id, 'name': 'rohan', 'info': 'sub details'}
    if my_id == 2 and my_subid == 6:
        student = {'id': my_id, 'name': 'akash', 'info': 'sub details'}
    if my_id == 3 and my_subid == 7:
        student = {'id': my_id, 'name': 'ashsish', 'info': 'sub details'}
    return render(request, 'enroll/show.html', student)