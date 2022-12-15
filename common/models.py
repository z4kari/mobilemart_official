from django.db import models

# Create your models here.
class ShopAdminLogin(models.Model):
    email = models.CharField(max_length = 100)
    pswd = models.CharField(max_length = 100)

class CustomerSignup(models.Model):
    name =  models.CharField(max_length = 100)
    email =  models.CharField(max_length = 100)
    pswd =  models.CharField(max_length = 100)
    phone =  models.BigIntegerField()


