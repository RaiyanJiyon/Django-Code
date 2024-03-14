from django.shortcuts import render

# Create your views here.

def learn_django(request):
    course = "Django"
    duration = "four month"
    seat = False
    course_details = {'cu': course, 'du': duration, 'se': seat}

    return render(request, 'course/courseone.html', context=course_details)