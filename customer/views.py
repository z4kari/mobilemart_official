from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from shop_admin.models import AddMobile,AddCable,AddCharger,AddHf,AddSpeaker,AddLap,AddMmc,AddPowerBank
# from rest_framework.parsers import JSONParser

# Create your views here.

def Home(request):
    # if 'cust_id' in request.session :
    return render(request,'customer/home.html')


def mobile(request):
    mob = AddMobile.objects.all()
    return render(request,'customer/mobile.html',{'mobile':mob})


def lap(request):
    laptop = AddLap.objects.all()
    return render(request,'customer/laptops.html',{'lap':laptop})

def accessories(request):
    return render(request,'customer/accessories.html')

def spe(request):
    speaker = AddSpeaker.objects.all()
    return render(request,'customer/speakers.html',{'sp':speaker})

def mob_details(request,id=0):
    mob=AddMobile.objects.get(id=id)
    return render(request,'customer/mob_detailed.html',{'mobDetailed':mob})




def lap_details(request,id=0):
    lap = AddLap.objects.get(id=id)
    return render(request,'customer/lap_detailed.html',{'l':lap})


def speaker_detailed(request,id=0):
    speaker = AddSpeaker.objects.get(id=id)
    return render(request,'customer/speaker_detailed.html',{'s':speaker})


def hf(request):
    headphone = AddHf.objects.all()
    return render(request,'customer/hf.html',{'hf':headphone})

def hf_detailed(request,id=0):
    headphone = AddHf.objects.get(id=id)
    return render(request,'customer/hf_detailed.html',{'hf':headphone})

def powerbank(request):
    pb = AddPowerBank.objects.all()
    return render(request,'customer/powerbank.html',{'p':pb})

def powerbank_detailed(request,id=0):
    pb = AddPowerBank.objects.get(id=id)
    return render(request,'customer/powerbank_detailed.html',{'p':pb})

def mmc(request):
    mmc = AddMmc.objects.all()
    return render(request,'customer/mmc.html',{'mycards':mmc})

def mmc_detailed(request,id=0):
    mmc = AddMmc.objects.get(id=id)
    return render(request,'customer/mmc_detailed.html',{'m':mmc})


def charger(request):
    charger = AddCharger.objects.all()
    return render(request,'customer/charger.html',{'chargers':charger})


def charger_detailed(request,id=0):
    charger = AddCharger.objects.get(id=id)
    return render(request,'customer/charger_detailed.html',{'chargers':charger})

def cable(request):
    cable = AddCable.objects.all()
    return render(request,'customer/cable.html',{'cables':cable})

def cable_detailed(request,id=0):
    cable = AddCable.objects.get(id=id)
    return render(request,'customer/cable_detailed.html',{'cableDetail':cable})


def whishlist(request):
    return render(request,'customer/whishlist.html')

def cart(request,id=0):
    
    return render(request,'customer/cart.html')


def index(request):
    return render(request,'customer/index.html')



def test(request):
    return render(request,'customer/test.html')