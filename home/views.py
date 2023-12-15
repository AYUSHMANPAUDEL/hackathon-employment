from django.shortcuts import render, HttpResponse , redirect  
from datetime import datetime
from home.models import Request
# Create your views here.
def home(request):
    return render(request , 'index.html')
def request(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        email=request.POST.get('email')
        problem=request.POST.get('problem')
        selected=request.POST.get('selected')
        Requests=Request(name=name,phone=phone,address=address, email=email ,problem=problem , selected=selected ,date=datetime.today())
        Requests.save()
    return render(request , 'request.html')
def formadded(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        email=request.POST.get('email')
        problem=request.POST.get('problem')
        selected=request.POST.get('selected')
        Requests=Request(name=name,phone=phone,address=address, email=email ,problem=problem , selected=selected ,date=datetime.today())
        Requests.save()
    return render(request , 'formadded.html')
def payment(request):
    if request.user.is_authenticated:
        return render(request , 'payment.html')
    else:
        return render(request , 'redircting.html')
        
def login(request):
    if request.user.is_authenticated:
        return render(request , 'index.html')
    else:
        return render(request , 'login.html')
