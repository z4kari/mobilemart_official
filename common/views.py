from django.shortcuts import render,redirect

from common.models import CustomerSignup, ShopAdminLogin

# Create your views here.
def alogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        pswd = request.POST['pswd']
        try:
            a_login = ShopAdminLogin.objects.get(email=email,pswd=pswd)
            return redirect('shopadmin:admin_home')
        except:
            return render(request,'common/admin_login.html')

    return render(request,'common/admin_login.html')
def cust_signup(request):
    if request.method =='POST':
        name = request.POST['name']
        email =  request.POST['email']
        pswd  = request.POST['pswd']
        phone =request.POST['phone']
       
        csignup = CustomerSignup(name=name,email=email,pswd=pswd,phone=phone)
        csignup.save()
        return redirect('customer:home')


    return render(request,'common/customer_signup.html')
def cust_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        pswd = request.POST['pswd']
        try:
            c_login = CustomerSignup.objects.get(email = email,pswd=pswd)
            request.session['cust_id'] = c_login.id #session 
            return redirect('customer:home')
        except:
            msg = 'invalid entry'
            return render(request,'common/customer_login.html',{"error_msg":msg})
    
    
    return render(request,'common/customer_login.html')