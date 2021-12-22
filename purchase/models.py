from django.db import models
from django.db.models.base import Model

from user.models import *
from product.models import *


class PurchaseReq(models.Model):
    buy_user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    pid=models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        unique_together=(('buy_user', 'pid'),)