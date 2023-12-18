from django.shortcuts import render, HttpResponse , redirect  
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login
# Create your views here.
def singup_page(request):
    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        email = request.POST.get("emailAddress")
        password = request.POST.get("password")
        username = request.POST.get("username")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose a different username.")
        else:
            # If the username is unique, create and save the user
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.save()
            messages.success(request, "You have successfully created an account.")
    return render(request , 'register.html')

def login_page(request):
      if request.method == "POST":
        user_name = request.POST.get("username")
        pass1 = request.POST.get("password")
        print(user_name,pass1)
        user=authenticate(request,username=user_name,password=pass1)
        if user is not None :
            login(request,user)
            return render(request,'home.html')
        else:
            messages.warning(request, "Username or Password is wrong")
      return render(request , 'login.html')

def home_page(request):
    return render(request,'home.html')

def go(request):
    return redirect("/home")

def beworker(request):
    return render(request,"beworker.html")