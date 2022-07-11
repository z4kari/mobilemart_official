from django.urls import path 
from . import views

app_name='sadmin'

urlpatterns = [ 
    path('add_products',views.add_products,name='add_pro'),
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('manage_user',views.manage_user,name='manage_user'),
     path('stock',views.stock,name='stock'),
     path('update',views.update,name='update_products')
]