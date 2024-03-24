from django.shortcuts import render

# Create your views here.

def learn_django(request):
    return render(request, 'course/courseone.html', context={'cu': "Learn Django", 'cd' : '4 month', 'st': 55})
