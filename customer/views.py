from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request,'customer/login.html')

def forgot_pass(request):
    return render(request,'customer/forgot.html')

def home(request):
    return render(request,'customer/home.html')

def signup(request):
    return render(request,'customer/signup.html')