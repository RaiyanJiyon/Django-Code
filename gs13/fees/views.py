from django.shortcuts import render
from datetime import datetime
# Create your views here.

def fees_django(request):
    d = datetime.now()
    return render(request, 'fees/feesone.html', context={'dt': d})

def nestedfor(request):
    student = {'stu1': {"name": "Rahul", "roll": 103},
           'stu2': {"name": "Sonam", "roll": 104},
           'stu3': {"name": "Raj", "roll": 101},
           'stu4': {"name": "Anu", "roll": 102},
          }
    return render(request, "fees/feestwo.html", context= {'student': student})
    