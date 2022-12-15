from django.urls import path
from . import views

app_name = 'shopadmin'

urlpatterns = [
    path('home', views.home, name='admin_home'),
    path('add_products', views.add_products, name='add_products'),
    path('adminIndex', views.adminIndex, name='adminIndex'),
    path('addMobile', views.addMobile, name='addMobile'),
    path('addLaptop', views.addLaptop, name='addLaptop'),
    path('addSpeaker', views.addSpeaker, name='addSpeaker'),
    path('addAccessories', views.addAccessories, name='addAccessories'),
    path('test1', views.test, name='test'),
    path('hf',views.hf,name='hf'),
    path('powerbank',views.powerBank,name='powerBank'),
    path('mmc',views.mmc,name='mmc'),
    path('charger',views.charger,name='charger'),
    path('cables',views.cables,name='cables'),
    path('view_products',views.view_products,name='view_products'),
    path('view_mobiles',views.view_mobiles,name='view_mobiles'),
    path('view_lap',views.view_lap,name='view_lap'),
    path('view_speaker',views.view_speaker,name='view_speaker'),
    path('view_hf',views.view_hf,name='view_hf'),
    path('view_cable',views.view_cable,name='view_cable'),
    path('view_charger',views.view_charger,name='view_charger'),
    path('view_mmc',views.view_mmc,name='view_mmc'),
    path('view_pbank',views.view_pbank,name='view_pbank'),
    path('delete_pb/<int:id>', views.delete_pb, name='delete_pb'),
    path('delete_mobile/<int:id>', views.delete_mobile, name='delete_mobile'),
    path('delete_lap/<int:id>', views.delete_lap, name='delete_lap'),
    path('delete_speaker/<int:id>', views.delete_speaker, name='delete_speaker'),
    path('delete_mmc/<int:id>', views.delete_mmc, name='delete_mmc'),
    path('delete_hf/<int:id>', views.delete_hf, name='delete_hf'),
    path('delete_charger/<int:id>', views.delete_charger, name='delete_charger'),
    path('delete_cable/<int:id>', views.delete_cable, name='delete_cable'),
    path('update_powerbanks/<int:id>',views.update_powerbanks,name='update_powerbanks'),
    path('updatePbank',views.updatePbank,name='updatePbank'),
    path('update_mmc/<int:id>',views.update_mmc,name='update_mmc'),
    path('updateMmc',views.updateMmc,name='updateMmc'),
    path('update_mobiles/<int:id>',views.update_mobiles,name='update_mobiles'),
    path('updateMobile',views.updateMobile,name='updateMobile'),
    path('update_laptop/<int:id>',views.update_laptop,name='update_laptop'),
    path('updateLaptop',views.updateLaptop,name='updateLaptop'),
    path('update_speaker/<int:id>',views.update_speaker,name='update_speaker'),
    path('updateSpeaker',views.updateSpeaker,name='updateSpeaker'),
    path('update_cable/<int:id>',views.update_cable,name='update_cable'),
    path('updateCable',views.updateCable,name='updateCable'),
    path('update_charger/<int:id>',views.update_charger,name='update_charger'),
    path('updateCharger',views.updateCharger,name='updateCharger'),
    path('update_hf/<int:id>',views.update_hf,name='update_hf'),
    path('updateHf',views.updateHf,name='updateHf'),
    




    































]
