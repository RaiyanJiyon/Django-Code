from django.shortcuts import render

# Create your views here.

def learn_django(request):
    course_name1 = {"cname": "Learn Django / React With Jiyon"}
    return render(request, 'course/courseone.html', context=course_name1)
    
    # we can code also like this
    # return render(request, 'course/courseone.html', course_name)

def learn_python(request):
    course_name2 = {"cname2": "Learn HTML/CSS With Jiyon"}
    return render(request, 'course/coursetwo.html', course_name2)