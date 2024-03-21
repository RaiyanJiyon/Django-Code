from django.shortcuts import render

# Create your views here.

def learn_django(request):
    course = "Django For Everyone"
    duration = "four month"
    seat = False
    course_details = {'cu': course, 'du': duration, 'se': seat}

    return render(request, 'course/courseone.html', context=course_details)

def float_format(request):
    return render(request, "course/courseone.html", context={"p1": 56.234, "p2": 56.0000, "p3": 56.34567})


def django_tag(request):
    return render(request, "course/coursetwo.html", {"nm": True})

def example_two(request):
    name = "Django"
    seats = 4

    course_details = {'nm':name, 'st':seats}
    return render(request, "course/coursethree.html", context = course_details)

def example_three(request):
    students = {'names': ["Sabbir", "Tamim", "Ishaq", "Mahabub", "Sohel"]}
    return render(request, "course/coursefour.html", context=students)

def example_four(request):
    stu = {'stu1': {"name": "Rahul", "roll": 103},
           'stu2': {"name": "Sonam", "roll": 104},
           'stu3': {"name": "Raj", "roll": 101},
           'stu4': {"name": "Anu", "roll": 102},
          }
    students = {'students': stu}
    return render(request, "course/coursefive.html", context=(students))

def example_five(request):
    data = {'name': 'Rahul', 'roll': 101}
    return render(request, "course/coursesix.html", context={'data': data})