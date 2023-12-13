from django.shortcuts import render, HttpResponse , redirect  
from datetime import datetime
from home.models import savedata
# Create your views here.
def home(request):
    if request.method == "POST":
        firstname = request.POST.get("firstName")
        lastname = request.POST.get("lastName")
        email = request.POST.get("emailAddress")
        password = request.POST.get("password")
        birthday = request.POST.get("birthdayDate")
        phonenumber = request.POST.get("phoneNumber")
        b = savedata(firstname=firstname,lastname=lastname,email=email,password=password,birthday=birthday,phonenumber=phonenumber,date=datetime.today())
        b.save()
    return render(request , 'register.html')
