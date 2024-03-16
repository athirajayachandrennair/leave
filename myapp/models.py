from django.db import models

# Create your models here.

class table(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)

class enq(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)

class staf(models.Model):
    name=models.CharField(max_length=200,null=True)
    lname=models.CharField(max_length=200,null=True)
    age=models.CharField(max_length=200,null=True)
    gender=models.CharField(max_length=200,null=True)
    department=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)


class ad(models.Model):
    
    email=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)

COLOR_CHOICES = (
    ('ring','RING'),
    ('chain', 'CHAIN'),

)     
class jew(models.Model):
   
    
    name=models.CharField(max_length=200,null=True)
    price=models.CharField(max_length=200,null=True)
    gram=models.IntegerField(null=True)
    image = models.ImageField(null=True,blank=True,upload_to ="images/")
    mod = models.CharField(max_length=6, choices=COLOR_CHOICES, default='CHAIN')



  

class cus(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)

class order(models.Model):
    name=models.CharField(max_length=200,null=True)
    price=models.CharField(max_length=200,null=True)
    orid=models.CharField(max_length=200,null=True)
    orn=models.CharField(max_length=200,null=True)
    add=models.CharField(max_length=200,null=True)
    pin=models.CharField(max_length=200,null=True)
    pay=models.CharField(max_length=200,null=True)

class cart(models.Model):
    product=models.CharField(max_length=200,null=True)
    userS=models.CharField(max_length=200,null=True)
    
    





