from django.db import models



# Create your models here.
class Udata(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)


   
class Rdata(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.IntegerField()
    email=models.CharField(max_length=100)
    bgroup=models.CharField(max_length=8)
    bdate=models.DateField
    gender=models.CharField(max_length=10)
    weight=models.CharField(max_length=50)
    state=models.CharField(max_length=10)
    district=models.CharField(max_length=50)
    pincode=models.IntegerField()
