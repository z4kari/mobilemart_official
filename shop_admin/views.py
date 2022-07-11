from django.shortcuts import render

# Create your views here.


def add_products(request):
    return render(request,'shop_admin/add_products.html')

def home(request):
    return render(request,'shop_admin/home.html')

def login(request):
    return render(request,'shop_admin/login.html')

def manage_user(request):
    return render(request,'shop_admin/manage_user.html')

def stock(request):
    return render(request,'shop_admin/stock.html')

def update(request):
    return render(request,'shop_admin/update.html')