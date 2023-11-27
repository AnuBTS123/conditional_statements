from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':1500,'b':7000,'c':1700}
    return render(request,'condition.html')