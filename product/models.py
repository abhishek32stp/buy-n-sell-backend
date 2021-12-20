from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
 
 
# models for Product Tags
class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)
 
    def __str__(self):
        return self.name
 
 
# models for Product
class Product(models.Model):
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=500,null=True)
    timeStamp = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)
 
    def __str__(self):
        return self.name