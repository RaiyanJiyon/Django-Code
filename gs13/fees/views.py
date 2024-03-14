from django.shortcuts import render
from datetime import datetime
# Create your views here.

def fees_django(request):
    d = datetime.now()
    return render(request, 'fees/feesone.html', context={'dt': d})
