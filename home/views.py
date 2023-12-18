from django.shortcuts import render, HttpResponse , redirect ,get_object_or_404 
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required

# Create your views here.
def singup_page(request):
    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        email = request.POST.get("emailAddress")
        password = request.POST.get("password")
        username = request.POST.get("username")
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username already exists. Please choose a different username.")
        else:
            # If the username is unique, create and save the user
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.save()
            messages.success(request, "You have successfully created an account.")
    return render(request , 'signup-login.html')

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
      return render(request , 'login-signup.html')

def home_page(request):
    return render(request,'home.html')



from home.models import Request
from django.views.generic import ListView

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
# for worker end
def work(request):

    selected_option = request.GET.get('selected_option', '')
    
    # Get all requests where is_accepted is False and order by date
    data = Request.objects.filter(is_accepted=False).order_by('date')

    # Further filter by request_type if selected_option is provided
    if selected_option:
        if selected_option == 'electric':
            data = data.filter(selected='electric')
        elif selected_option == 'plumber':
            data = data.filter(selected='plumber')
        elif selected_option == 'other':
            data = data.filter(selected='other')

    return render(request, 'work.html', {'data': data, 'selected_option': selected_option})
def item_detail(request, item_id):
    item = get_object_or_404(Request, id=item_id)
    service_request = Request.objects.get(pk=item_id)
    service_request.accepted_by = request.user
    service_request.is_accepted = True
    service_request.accepted_date = datetime.today()

    service_request.save()
    return render(request, 'item_detail.html', {'item': item})
