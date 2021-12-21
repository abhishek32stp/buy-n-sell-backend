from django.db import models
from django.db.models.base import Model
#from ..product.models import *


class PurchaseReq(models.Model):
    buy_user=models.IntegerField()
    pid=models.IntegerField()

    class Meta:
        unique_together=(('buy_user', 'pid'),)