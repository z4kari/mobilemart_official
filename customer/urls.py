from django.urls import path 
from . import views

app_name='customer'

urlpatterns=[ 
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('forgot',views.forgot_pass,name='forgot'),
    path('home',views.home,name='home')
]