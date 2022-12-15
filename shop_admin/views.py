from django.shortcuts import render,redirect

from shop_admin.models import AddMobile,AddLap,AddSpeaker,AddHf,AddCable,AddCharger,AddMmc,AddPowerBank

# Create your views here.
def  home(request):
    return render(request,'shop_admin/home.html')

def  add_products(request):
    return render(request,'shop_admin/add_products.html')


def adminIndex(request):
    return render(request,'shop_admin/index.html')



def addMobile(request):
    if request.method == 'POST':
        mobileName = request.POST['mobileName']
        brandName = request.POST['brandName']
        salesPackage = request.POST['salesPackage']
        nsp = request.POST['nsp']
        os   = request.POST['os']
        ct   = request.POST['CT']
        color = request.POST['color']
        ram = request.POST['ram']
        storage  = request.POST['storage']
        battery   = request.POST['battery']
        camera    = request.POST['camera']
        processor  = request.POST['processor']
        display   = request.POST['display']
        marketPrice = request.POST['marketPrice']
        price  = request.POST['price']
        qty = request.POST['qty']
        frontImage = request.FILES['frontImage']
        backImage = request.FILES['backImage']
        leftImage = request.FILES['leftImage']
        rightImage = request.FILES['rightImage']

        mobile = AddMobile(mobileName=mobileName,brandName=brandName,salesPackage=salesPackage,networkProvider=nsp,os=os,cellularTechnology=ct,color=color,ram=ram,internalStorage=storage,battery=battery,camera=camera,processor=processor,display=display,marketPrice=marketPrice,Price=price,qty=qty,frontImage=frontImage,backImage=backImage,leftImage=leftImage,rightImage=rightImage)    
        mobile.save()
    return render(request,'shop_admin/addMobile.html')


def addLaptop(request):
    if request.method == 'POST':
        model_name = request.POST['model_name']
        sales_package = request.POST['sales_package']
        model_number = request.POST['model_number']
        part_number = request.POST['part_number']
        series = request.POST['series']
        color = request.POST['color']
        lap_type = request.POST['lap_type']
        suitable = request.POST['suitable']
        Battery_cell = request.POST['Battery_cell']
        ms_office = request.POST['ms_office']
        weight = request.POST['weight']
        dgm = request.POST['dgm']
        dgmc = request.POST['dgmc']
        processor_brand = request.POST['processor_brand']
        processor_name = request.POST['processor_name']
        ssd = request.POST['ssd']
        ssd_capacity = request.POST['ssd_capacity']
        ram = request.POST['ram']
        ram_type = request.POST['ram_type']
        processor_varient = request.POST['processor_varient']
        clock_speed = request.POST['clock_speed']
        graphic_processor = request.POST['graphic_processor']
        os_architecture = request.POST['os_architecture']
        os = request.POST['os']
        touch_screen = request.POST['touch_screen']
        screen_size = request.POST['screen_size']
        screen_resolution = request.POST['screen_resolution']
        screen_type = request.POST['screen_type']
        Speakers = request.POST['Speakers']
        internal_mic = request.POST['internal_mic']
        Sound_properties = request.POST['Sound_properties']
        refresh_rate = request.POST['refresh_rate']
        wireless_lan = request.POST['wireless_lan']
        bluetooth = request.POST['bluetooth']
        ethernet = request.POST['ethernet']
        marketPrice = request.POST['marketPrice']
        Price  = request.POST['Price']
        qty = request.POST['qty']
        description = request.POST['description']
        warranty_type = request.POST['warranty_type']
        warranty_service_type = request.POST['warranty_service_type']
        covered_in_warranty = request.POST['covered_in_warranty']
        not_in_warranty = request.POST['not_in_warranty']
        frontImage = request.FILES['frontImage']
        backImage = request.FILES['backImage']
        leftImage = request.FILES['leftImage']
        rightImage = request.FILES['rightImage']
        brand_name = request.POST['brand_name']


        lap = AddLap(model_name=model_name,brand_name=brand_name,sales_package=sales_package,model_number=model_number,part_number=part_number,series=series,color=color,lap_type=lap_type,suitable=suitable,Battery_cell=Battery_cell,ms_office=ms_office,weight=weight,dgm=dgm,dgmc=dgmc,processor_brand=processor_brand,processor_name=processor_name,ssd=ssd,ssd_capacity=ssd_capacity,ram=ram,ram_type=ram_type,processor_varient=processor_varient,clock_speed=clock_speed,graphic_processor=graphic_processor,os_architecture=os_architecture,os=os,touch_screen=touch_screen,screen_size=screen_size,screen_resolution=screen_resolution,screen_type=screen_type,Speakers=Speakers,internal_mic=internal_mic,Sound_properties=Sound_properties,refresh_rate=refresh_rate,wireless_lan=wireless_lan,bluetooth=bluetooth,ethernet=ethernet,marketPrice=marketPrice,Price=Price,qty=qty,description=description,warranty_service_type=warranty_service_type,covered_in_warranty=covered_in_warranty,not_in_warranty=not_in_warranty,frontImage=frontImage,backImage=backImage,leftImage=leftImage,rightImage=rightImage,warranty_type=warranty_type,)
        lap.save()
    return render(request,'shop_admin/addLaptop.html')


def addSpeaker(request):
    if request.method == 'POST':
        model_name = request.POST['model_name']
        brand_name = request.POST['brand_name']
        sales_package = request.POST['sales_package']
        model_number = request.POST['model_number']
        speaker_type = request.POST['speaker_type']
        bluetooth = request.POST['bluetooth']
        configuration = request.POST['configuration']
        power_output = request.POST['power_output']
        color = request.POST['color']
        battery_capacity = request.POST['battery_capacity']
        width = request.POST['width']
        height = request.POST['height']
        depth = request.POST['depth']
        market_price = request.POST['market_price']
        price = request.POST['price']
        qty = request.POST['qty']
        description = request.POST['description']
        frontImage = request.FILES['Image1']
        backImage = request.FILES['Image2']

        speaker = AddSpeaker(model_name=model_name,brand_name=brand_name,sales_package=sales_package,model_number=model_number,speaker_type=speaker_type,bluetooth=bluetooth,configuration=configuration,power_output=power_output,color=color,battery_capacity=battery_capacity,width=width,height=height,depth=depth,market_price=market_price,price=price,qty=qty,description=description,Image1=frontImage,Image2=backImage)
        speaker.save()

    return render(request,'shop_admin/addSpeaker.html')


def addAccessories(request):
    return render(request,'shop_admin/addAccessories.html')

def hf(request):
    if request.method == 'POST':
        model_name = request.POST['model_name']
        brand_name = request.POST['brand_name']
        color = request.POST['color']
        hf_type = request.POST['hf_type']
        inline_remote = request.POST['inline_remote']
        sales_package = request.POST['sales_package']
        connectivity = request.POST['connectivity']
        hf_design =  request.POST['hf_design']
        deep_bass = request.POST['deep_bass']
        microphone = request.POST['microphone']
        warranty_summary = request.POST['warranty_summary']
        covered_warranty = request.POST['covered_warranty']
        not_in_warranty = request.POST['not_in_warranty']
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        market_price = request.POST['market_price']
        price = request.POST['price']
        qty = request.POST['qty']
        description = request.POST['description']

        hf = AddHf(model_name=model_name,brand_name=brand_name,color=color,hf_type=hf_type,inline_remote=inline_remote,sales_package=sales_package,connectivity=connectivity,hf_design=hf_design,deep_bass=deep_bass,microphone=microphone,warranty_summary=warranty_summary,covered_warranty=covered_warranty,not_in_warranty=not_in_warranty,image1=image1,image2=image2,market_price=market_price,price=price,qty=qty,description=description)
        hf.save()
    return render(request,'shop_admin/hf.html')

def powerBank(request):
    if request.method == 'POST':
        model_name = request.POST['model_name']
        sales_package = request.POST['sales_package']
        brand_name = request.POST['brand_name']
        capacity = request.POST['capacity']
        suitable_device = request.POST['suitable_device']
        nof_output_ports = request.POST['nof_output_ports']
        warranty = request.POST['warranty']
        covered_warranty = request.POST['covered_warranty']
        not_in_warranty = request.POST['not_in_warranty']
        color = request.POST['color']
        width = request.POST['width']
        height = request.POST['height']
        depth = request.POST['depth']
        weight = request.POST['weight']
        market_price = request.POST['market_price']
        price = request.POST['price']
        qty = request.POST['qty']
        description = request.POST['description']
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']

        power_bank = AddPowerBank(model_name=model_name,sales_package=sales_package,brand_name=brand_name,capacity=capacity,suitable_device=suitable_device,nof_output_ports=nof_output_ports,warranty=warranty,covered_warranty=covered_warranty,not_in_warranty=not_in_warranty,color=color,width=width,height=height,depth=depth,weight=weight,market_price=market_price,price=price,qty=qty,description=description,image1=image1,image2=image2)
        power_bank.save()
    return render(request,'shop_admin/powerbank.html')


def mmc(request):
    if request.method == 'POST':
        brand_name = request.POST['brand_name']
        sales_package = request.POST['sales_package']
        series =  request.POST['series']
        model_number = request.POST['model_number']
        write_speed = request.POST['write_speed']
        read_speed = request.POST['read_speed']
        weight = request.POST['weight']
        warranty = request.POST['warranty']
        covered_warranty = request.POST['covered_warranty']
        not_in_warranty = request.POST['not_in_warranty']
        capacity = request.POST['capacity']
        market_price = request.POST['market_price']
        price = request.POST['price']
        qty = request.POST['qty']
        description = request.POST['description']
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']

        mmc = AddMmc(brand_name=brand_name,sales_package=sales_package,series=series,model_number=model_number,write_speed=write_speed,read_speed=read_speed,weight=weight,warranty=warranty,covered_warranty=covered_warranty,not_in_warranty=not_in_warranty,capacity=capacity,market_price=market_price,price=price,qty=qty,description=description,image1=image1,image2=image2)
        mmc.save()
    return render(request,'shop_admin/mmc.html')

def charger(request):
    if request.method == 'POST':
        brand_name = request.POST['brand_name']
        sales_package = request.POST['sales_package']
        model_name = request.POST['model_name']
        model_number = request.POST['model_number']
        output_interferance = request.POST['output_interferance']
        led = request.POST['led']
        dispaly = request.POST['dispaly']
        cable_length = request.POST['cable_length']
        power_input = request.POST['power_input']
        power_source = request.POST['power_source']
        output_current = request.POST['output_current']
        output_wattage = request.POST['output_wattage']
        warranty = request.POST['warranty']
        covered_warranty = request.POST['covered_warranty']
        not_in_warranty = request.POST['not_in_warranty']
        market_price = request.POST['market_price']
        price = request.POST['price']
        qty = request.POST['qty']
        description = request.POST['description']
        image1 = request.FILES['image1']
        image2  = request.FILES['image2']

        charger = AddCharger(brand_name=brand_name,sales_package=sales_package,model_name=model_name,model_number=model_number,output_interferance=output_interferance,led=led,dispaly=dispaly,cable_length=cable_length,power_input=power_input,power_source=power_source,output_current=output_current,output_wattage=output_wattage,warranty=warranty,covered_warranty=covered_warranty,not_in_warranty=not_in_warranty,market_price=market_price,price=price,qty=qty,description=description,image1=image1,image2=image2)
        charger.save()
    return render(request,'shop_admin/charger.html')


def cables(request):
    if request.method == 'POST':
        brand_name = request.POST['brand_name']
        sales_package =  request.POST['sales_package']
        model = request.POST['model']
        cable_type = request.POST['cable_type']
        connector1 = request.POST['connector1']
        connector2 = request.POST['connector2']
        color = request.POST['color']
        length = request.POST['length']
        meterial =  request.POST['meterial']
        warranty = request.POST['warranty']
        covered_warranty = request.POST['covered_warranty']
        not_in_warranty = request.POST['not_in_warranty']
        market_price = request.POST['market_price']
        price = request.POST['price']
        qty = request.POST['qty']
        description = request.POST['description']
        image1 = request.FILES['image1']
        image2 =  request.FILES['image2']

        cable = AddCable(brand_name=brand_name,sales_package=sales_package,model=model,cable_type=cable_type,connector1=connector1,connector2=connector2,color=color,length=length,meterial=meterial,warranty=warranty,covered_warranty=covered_warranty,not_in_warranty=not_in_warranty,market_price=market_price,price=price,qty=qty,description=description,image1=image1,image2=image2)
        cable.save()
    return render(request,'shop_admin/cables.html')


def view_products(request):
    return render(request,'shop_admin/view_products.html')


def view_mobiles(request):
    viewMobile = AddMobile.objects.all()
    return render(request,'shop_admin/view_mobiles.html',{'mobiles':viewMobile})

def view_lap(request):
    viewLap = AddLap.objects.all()
    return render(request,'shop_admin/view_lap.html',{'laptops':viewLap})

def view_speaker(request):
    viewSpeaker = AddSpeaker.objects.all()
    return render(request,'shop_admin/view_speaker.html',{'speakers':viewSpeaker})

def view_hf(request):
    viewHf = AddHf.objects.all()
    return render(request,'shop_admin/view_hf.html',{'hf':viewHf})


def view_cable(request):
    viewCable = AddCable.objects.all()
    return render(request,'shop_admin/view_cable.html',{'cables':viewCable})

def view_charger(request):
    viewCharger = AddCharger.objects.all()
    return render(request,'shop_admin/view_charger.html',{'chargers':viewCharger})


def view_mmc(request):
    viewMmc = AddMmc.objects.all()
    return render(request,'shop_admin/view_mmc.html',{'mcards':viewMmc})

def view_pbank(request):
    viewPbank = AddPowerBank.objects.all()
    return render(request,'shop_admin/view_pbank.html',{'Powerbanks':viewPbank})



def delete_pb(request,id=0):
    deletePb = AddPowerBank.objects.get(id=id).delete()
    
    return redirect('shopadmin:view_pbank')

def delete_mobile(request,id=0):
    deleteMobile = AddMobile.objects.get(id=id).delete()
    
    return redirect('shopadmin:view_mobiles')

def delete_lap(request,id=0):
    deleteLap = AddLap.objects.get(id=id).delete()
    
    return redirect('shopadmin:view_lap')

def delete_speaker(request,id=0):
    deleteSpeaker = AddSpeaker.objects.get(id=id).delete()
    
    return redirect('shopadmin:view_speaker')

def delete_mmc(request,id=0):
    deleteMmc = AddMmc.objects.get(id=id).delete()
    
    return redirect('shopadmin:view_mmc')

def delete_hf(request,id=0):
    deleteHf = AddHf.objects.get(id=id).delete()
    
    return redirect('shopadmin:view_hf')


def delete_charger(request,id=0):
    deleteCharger = AddCharger.objects.get(id=id).delete()
    
    return redirect('shopadmin:view_charger')




def delete_cable(request,id=0):
    deleteCable = AddCable.objects.get(id=id).delete()
    
    return redirect('shopadmin:view_cable')


def update_powerbanks(request,id=0):
    update_pbank = AddPowerBank.objects.get(id=id)
    return render(request,'shop_admin/update_powerbanks.html',{'updatePb':update_pbank})


def updatePbank(request):
    if request.method == 'POST':
        capacity = request.POST['capacity']
        nof_output_ports = request.POST['nof_output_ports']
        color = request.POST['color']
        market_price = request.POST['market_price']
        price = request.POST['price']
        qty = request.POST['qty']
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        pb_id  = request.POST['pb_id']

        updatePowerBank = AddPowerBank.objects.filter(id=pb_id)
        updatePowerBank.update(capacity=capacity,nof_output_ports=nof_output_ports,color=color,market_price=market_price,price=price,qty=qty,image1=image1,image2=image2)
        
    return redirect('shopadmin:view_pbank')


def update_mmc(request,id=0):
    update_mmc = AddMmc.objects.get(id=id)
    return render(request,'shop_admin/update_mmc.html',{'updateMMC':update_mmc})

def updateMmc(request):
    if request.method == 'POST':
        write_speed = request.POST['write_speed']
        read_speed = request.POST['read_speed']
        market_price = request.POST['market_price']
        price = request.POST['price']
        qty = request.POST['qty']
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        mmc_id  = request.POST['mmc_id']

        updateMmc = AddMmc.objects.filter(id=mmc_id)
        updateMmc.update(write_speed=write_speed,read_speed=read_speed,market_price=market_price,price=price,qty=qty,image1=image1,image2=image2)
        
    return redirect('shopadmin:view_mmc')


def update_mobiles(request,id=0):
    updateMobile = AddMobile.objects.get(id=id)
    return render(request,'shop_admin/update_mobiles.html',{'updateMOBILE':updateMobile})


def updateMobile(request):
    if request.method == 'POST':
        ram = request.POST['ram']
        internalStorage = request.POST['internalStorage']
        battery = request.POST['battery']
        camera = request.POST['camera']
        marketPrice = request.POST['marketPrice']
        price = request.POST['price']
        qty = request.POST['qty']
        frontImage = request.FILES['frontImage']
        backImage = request.FILES['backImage']
        leftImage = request.FILES['leftImage']
        rightImage = request.FILES['rightImage']
        mob_id  = request.POST['mob_id']

        updateMobile = AddMobile.objects.filter(id=mob_id)
        updateMobile.update(ram=ram,internalStorage=internalStorage,battery=battery,camera=camera,marketPrice=marketPrice,Price=price,qty=qty,frontImage=frontImage,backImage=backImage,leftImage=leftImage,rightImage=rightImage)
        
    return redirect('shopadmin:view_mobiles')


def update_laptop(request,id=0):
    updateLaptop = AddLap.objects.get(id=id)
    return render(request,'shop_admin/update_lap.html',{'updateLaptop':updateLaptop})


def updateLaptop(request):
    if request.method == 'POST':
        color = request.POST['color']
        suitable = request.POST['suitable']
        ms_office =request.POST['ms_office']
        ssd = request.POST['ssd']
        ssd_capacity = request.POST['ssd_capacity']
        ram = request.POST['ram']
        marketPrice = request.POST['marketPrice']
        Price = request.POST['Price']
        qty = request.POST['qty']
        frontImage = request.FILES['frontImage']
        backImage = request.FILES['backImage']
        leftImage = request.FILES['leftImage']
        rightImage = request.FILES['rightImage']
        lap_id  = request.POST['lap_id']

        updateLap = AddLap.objects.filter(id=lap_id)
        updateLap.update(color=color,suitable=suitable,ms_office=ms_office,ssd=ssd,ssd_capacity=ssd_capacity,ram=ram,marketPrice=marketPrice,Price=Price,qty=qty,frontImage=frontImage,backImage=backImage,leftImage=leftImage,rightImage=rightImage)
        
    return redirect('shopadmin:view_lap')



def update_speaker(request,id=0):
    updateSpeaker = AddSpeaker.objects.get(id=id)
    return render(request,'shop_admin/update_speaker.html',{'updateSpeaker':updateSpeaker})




def updateSpeaker(request):
    if request.method == 'POST':
        battery_capacity = request.POST['battery_capacity']
        color = request.POST['color']
        market_price = request.POST['market_price']
        price = request.POST['price']
        qty = request.POST['qty']
        Image1 = request.FILES['Image1']
        Image2 = request.FILES['Image2']
        speaker_id  = request.POST['speaker_id']

        updateSpeaker = AddSpeaker.objects.filter(id=speaker_id)
        updateSpeaker.update(battery_capacity=battery_capacity,color=color,market_price=market_price,price=price,qty=qty,Image1=Image1,Image2=Image2)
        
    return redirect('shopadmin:view_speaker')


def update_cable(request,id=0):
    updateCable = AddCable.objects.get(id=id)
    return render(request,'shop_admin/update_cable.html',{'updCable':updateCable})

def updateCable(request):
    if request.method == 'POST':
        length = request.POST['length']
        meterial = request.POST['meterial']

        color = request.POST['color']
        market_price = request.POST['market_price']
        price = request.POST['price']
        qty = request.POST['qty']
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        cable_id  = request.POST['cable_id']

        updateCable = AddCable.objects.filter(id=cable_id)
        updateCable.update(length=length,meterial=meterial,color=color,market_price=market_price,price=price,qty=qty,image1=image1,image2=image2)
        
    return redirect('shopadmin:view_cable')


def update_charger(request,id=0):
    updateCharger = AddCharger.objects.get(id=id)
    return render(request,'shop_admin/update_charger.html',{'updCharger':updateCharger})


def updateCharger(request):
    if request.method == 'POST':
        cable_length = request.POST['cable_length']
    
        market_price = request.POST['market_price']
        price = request.POST['price']
        qty = request.POST['qty']
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        charger_id  = request.POST['charger_id']

        updateCharger = AddCharger.objects.filter(id=charger_id)
        updateCharger.update(cable_length=cable_length,market_price=market_price,price=price,qty=qty,image1=image1,image2=image2)
    return redirect('shopadmin:view_charger')  


def update_hf(request,id=0):
    updateHf = AddHf.objects.get(id=id)
    return render(request,'shop_admin/update_hf.html',{'updHf':updateHf})



def updateHf(request):
    if request.method == 'POST':
    
        market_price = request.POST['market_price']
        price = request.POST['price']
        qty = request.POST['qty']
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        hf_id  = request.POST['hf_id']

        updateHf = AddHf.objects.filter(id=hf_id)
        updateHf.update(market_price=market_price,price=price,qty=qty,image1=image1,image2=image2)
    return redirect('shopadmin:view_charger')  

def test(request):
    return render(request,'shop_admin/block.html')