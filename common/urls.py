from django.urls import path 
from . import views

app_name='common'

urlpatterns=[ 
    path('alogin',views.alogin,name='alogin'),
    path('cust_signup',views.cust_signup,name='csignup'),
    path('cust_login',views.cust_login,name='clogin'),
   
]