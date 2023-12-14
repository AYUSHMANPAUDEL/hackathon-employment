from django.shortcuts import render, HttpResponse , redirect  

# Create your views here.
def home(request):
    return render(request , 'index.html')
def request(request):
    return render(request , 'request.html')
