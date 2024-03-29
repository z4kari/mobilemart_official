from django.db import models

# Create your models here.


class AddMobile(models.Model):
    mobileName = models.CharField(max_length=100)
    brandName = models.CharField(max_length=100)
    salesPackage = models.CharField(max_length=100)
    networkProvider = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    cellularTechnology = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    ram = models.BigIntegerField()
    internalStorage = models.BigIntegerField()
    battery = models.BigIntegerField()
    camera = models.BigIntegerField()
    processor = models.CharField(max_length=100)
    display = models.CharField(max_length=100)
    frontImage = models.ImageField(upload_to='addMobiles/')
    backImage = models.ImageField(upload_to='addMobiles/')
    leftImage = models.ImageField(upload_to='addMobiles/')
    rightImage = models.ImageField(upload_to='addMobiles/')
    marketPrice = models.BigIntegerField()
    Price = models.BigIntegerField()
    qty = models.BigIntegerField()
    description = models.CharField(max_length=150)


    

class AddLap(models.Model):
    model_name = models.CharField(max_length=100)
    sales_package = models.CharField(max_length=100)
    model_number = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    part_number = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    lap_type  = models.CharField(max_length=100)
    suitable = models.CharField(max_length=100)
    Battery_cell  = models.CharField(max_length=100)
    ms_office  = models.CharField(max_length=100)
    weight  = models.CharField(max_length=100)
    dgm  = models.CharField(max_length=100)
    dgmc  = models.CharField(max_length=100)
    processor_brand  = models.CharField(max_length=100)
    processor_name  = models.CharField(max_length=100)
    processor_generation = models.CharField(max_length=100)
    ssd  = models.CharField(max_length=100)
    ssd_capacity  = models.CharField(max_length=100)
    ram  = models.CharField(max_length=100)
    ram_type  = models.CharField(max_length=100)
    processor_varient  = models.CharField(max_length=100)
    clock_speed  = models.CharField(max_length=100)
    graphic_processor  = models.CharField(max_length=100)
    os_architecture  = models.CharField(max_length=100)
    os  = models.CharField(max_length=100)
    touch_screen  = models.CharField(max_length=100)
    screen_size  = models.CharField(max_length=100)
    screen_resolution  = models.CharField(max_length=100)
    screen_type  = models.CharField(max_length=100)
    Speakers  = models.CharField(max_length=100)
    internal_mic  = models.CharField(max_length=100)
    Sound_properties  = models.CharField(max_length=100)
    refresh_rate  = models.CharField(max_length=100)
    wireless_lan  = models.CharField(max_length=100)
    bluetooth  = models.CharField(max_length=100)
    ethernet  = models.CharField(max_length=100)
    warranty_type  = models.CharField(max_length=100)
    warranty_service_type  = models.CharField(max_length=100)
    covered_in_warranty  = models.CharField(max_length=100)
    not_in_warranty  = models.CharField(max_length=100)
    frontImage  = models.ImageField('addLap/')
    backImage  = models.ImageField('addLap/')
    leftImage  = models.ImageField('addLap/')
    rightImage  = models.ImageField('addLap/')
    marketPrice = models.BigIntegerField()
    Price = models.BigIntegerField()
    qty = models.BigIntegerField()
    description = models.CharField(max_length=150)


class AddSpeaker(models.Model):
    model_name = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    sales_package = models.CharField(max_length=100)
    model_number = models.CharField(max_length=100)
    speaker_type = models.CharField(max_length=100)
    bluetooth = models.CharField(max_length=100)
    configuration = models.CharField(max_length=100)
    power_output = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    battery_capacity = models.CharField(max_length=100)
    width = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    depth = models.CharField(max_length=100)
    market_price = models.BigIntegerField()
    price = models.BigIntegerField()
    qty = models.BigIntegerField()
    description = models.CharField(max_length=100)
    Image1= models.ImageField('addspeaker/')
    Image2 = models.ImageField('addspeaker/')



class AddHf(models.Model):
    model_name = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    hf_type = models.CharField(max_length=100)
    inline_remote =  models.CharField(max_length=100)
    sales_package = models.CharField(max_length=100)
    connectivity = models.CharField(max_length=100)
    hf_design = models.CharField(max_length=100)
    deep_bass = models.CharField(max_length=100)
    microphone = models.CharField(max_length=100) 
    warranty_summary = models.CharField(max_length=100)  
    covered_warranty = models.CharField(max_length=100)
    not_in_warranty = models.CharField(max_length=100)    
    image1 = models.ImageField('addhf/')
    image2 = models.ImageField('addhf/')
    market_price = models.BigIntegerField()
    price = models.BigIntegerField()
    qty = models.BigIntegerField()
    description = models.CharField(max_length=100)    


class AddCable(models.Model):
    brand_name =   models.CharField(max_length=100)   
    sales_package =  models.CharField(max_length=100)   
    model =  models.CharField(max_length=100)   
    cable_type =  models.CharField(max_length=100)   
    connector1 =  models.CharField(max_length=100)   
    connector2 =  models.CharField(max_length=100)   
    color =  models.CharField(max_length=100)   
    length =  models.CharField(max_length=100)   
    meterial =   models.CharField(max_length=100)   
    warranty =  models.CharField(max_length=100)   
    covered_warranty =  models.CharField(max_length=100)   
    not_in_warranty =  models.CharField(max_length=100)   
    market_price = models.BigIntegerField()
    price = models.BigIntegerField()
    qty = models.BigIntegerField()
    description =  models.CharField(max_length=100)   
    image1 = models.ImageField('addCable/')
    image2 = models.ImageField('addCable/')


class AddCharger(models.Model):
    brand_name =  models.CharField(max_length=100) 
    sales_package =  models.CharField(max_length=100) 
    model_name =  models.CharField(max_length=100) 
    model_number =  models.CharField(max_length=100) 
    output_interferance =  models.CharField(max_length=100) 
    led =  models.CharField(max_length=100) 
    dispaly =  models.CharField(max_length=100) 
    cable_length =  models.CharField(max_length=100) 
    power_input =  models.CharField(max_length=100) 
    power_source =  models.CharField(max_length=100) 
    output_current =  models.CharField(max_length=100) 
    output_wattage =  models.CharField(max_length=100) 
    warranty =  models.CharField(max_length=100) 
    covered_warranty =  models.CharField(max_length=100) 
    not_in_warranty =  models.CharField(max_length=100) 
    market_price =  models.BigIntegerField()
    price =  models.BigIntegerField()
    qty =  models.BigIntegerField()
    description =  models.CharField(max_length=100) 
    image1 = models.ImageField('addCharger/')
    image2 = models.ImageField('addCharger/')



class AddMmc(models.Model):
    brand_name  =  models.CharField(max_length=100) 
    sales_package  =  models.CharField(max_length=100) 
    series  =  models.CharField(max_length=100) 
    model_number  =  models.CharField(max_length=100) 
    write_speed  =  models.CharField(max_length=100) 
    read_speed  =  models.CharField(max_length=100) 
    weight  =  models.CharField(max_length=100) 
    warranty  =  models.CharField(max_length=100) 
    covered_warranty  =  models.CharField(max_length=100) 
    not_in_warranty  =  models.CharField(max_length=100) 
    capacity  =  models.CharField(max_length=100) 
    market_price =  models.BigIntegerField()
    price =  models.BigIntegerField()
    qty =  models.BigIntegerField()
    description  =  models.CharField(max_length=100) 
    image1 = models.ImageField('addMmc/')
    image2 = models.ImageField('addMmc/')




class AddPowerBank(models.Model):
    model_name =  models.CharField(max_length=100) 
    sales_package  =  models.CharField(max_length=100) 
    brand_name  =  models.CharField(max_length=100) 
    capacity  =  models.CharField(max_length=100) 
    suitable_device =  models.CharField(max_length=100) 
    nof_output_ports = models.BigIntegerField()
    warranty  =  models.CharField(max_length=100) 
    covered_warranty  =  models.CharField(max_length=100) 
    not_in_warranty  =  models.CharField(max_length=100) 
    color =  models.CharField(max_length=100) 
    width = models.CharField(max_length=100) 
    height = models.CharField(max_length=100) 
    depth = models.CharField(max_length=100) 
    weight = models.CharField(max_length=100) 
    market_price =  models.BigIntegerField()
    price =  models.BigIntegerField()
    qty =  models.BigIntegerField()
    description  =  models.CharField(max_length=100) 
    image1 = models.ImageField('addPowerbank/')
    image2 = models.ImageField('addPowerbank/')

