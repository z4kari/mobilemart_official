from django.urls import path 
from . import views

app_name='customer'

urlpatterns=[ 
    path('home',views.Home,name='home'),
    path('mobile',views.mobile,name='mobile'),
    path('lap',views.lap,name='lap'),
    path('accessories',views.accessories,name='accessories'),
    path('sp',views.spe,name='speakers'),
    path('mob_detailed/<int:id>',views.mob_details,name='mob_detailed'),
    path('lap_detailed/<int:id>',views.lap_details,name='lap_detailed'),
    path('speaker_detailed/<int:id>',views.speaker_detailed,name='speaker_detailed'),
    path('hf',views.hf,name='hf'),
    path('hf_detailed/<int:id>',views.hf_detailed,name='hf_detailed'),
    path('powerbank',views.powerbank,name='powerbank'),
    path('powerbank_detailed/<int:id>',views.powerbank_detailed,name='powerbank_detailed'),
    path('mmc',views.mmc,name='mmc'),
    path('mmc_detailed/<int:id>',views.mmc_detailed,name='mmc_detailed'),
    path('charger',views.charger,name='charger'),
    path('charger_detailed/<int:id>',views.charger_detailed,name='charger_detailed'),
    path('cable',views.cable,name='cable'),
    path('cable_detailed/<int:id>',views.cable_detailed,name='cable_detailed'),
    path('whishlist',views.whishlist,name='whishlist'),
    path('cart',views.cart,name='cart'),














    path('test',views.test),
    path('index',views.index),
  
]