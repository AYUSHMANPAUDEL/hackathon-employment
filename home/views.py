from django.shortcuts import render, HttpResponse , redirect  
from datetime import datetime
from home.models import Request
from django.views.generic import ListView
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

def work(request):
    selected_option = request.GET.get('selected_option', '')
    
    if selected_option == 'electric':
        data = Request.objects.filter(selected='electric').order_by('date')
    elif selected_option == 'plumber':
        data = Request.objects.filter(selected='plumber').order_by('date')
    elif selected_option == 'other':
        data = Request.objects.filter(selected='other').order_by('date')
    else:
        data = Request.objects.all()

    return render(request, 'work.html', {'data': data, 'selected_option': selected_option})