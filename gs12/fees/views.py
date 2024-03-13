from django.shortcuts import render

# Create your views here.

def fees_django(request):
    cname = "Learn Django"
    duration = "3 Month"
    fees = 12000

    fees_details = {"nm": cname, "du": duration, "fee": fees}

    return render(request, 'fees/feesone.html', context=fees_details)

def fees_python(request):
    return render(request, 'fees/feestwo.html')