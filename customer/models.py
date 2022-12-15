from django.db import models
from common.models import CustomerSignup
from shop_admin.models import AddMobile
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(CustomerSignup, on_delete=models.CASCADE)
    product = models.ForeignKey(AddMobile, on_delete=models.CASCADE)
