from django.shortcuts import render, HttpResponse, redirect
from.models import*

# Create your views here.


def bmi_input(request):
    if request.method=='POST':
        age=int(request.POST.get('age'))
        gender=request.POST.get('gender')
        height=int(request.POST.get('height'))
        weight=int(request.POST.get('weight'))
        result=round((weight/((height/100)**2)),1)
        return render(request,'output.html',{'result':result})
    return render(request,'inputs.html')
