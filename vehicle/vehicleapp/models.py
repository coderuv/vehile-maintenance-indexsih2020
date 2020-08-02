from django.db import models
import os
from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_save, post_save
ss = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/static/"


# Create your models here.
class vehicles(models.Model):
    vehicle_name= models.CharField(max_length=100,null=True,blank=True)
    description= models.CharField(max_length=100,null=True,blank=True)
    mileage= models.IntegerField()
    price= models.IntegerField()
    oil_change= models.IntegerField()
    airfilter_change= models.IntegerField()
    spark_plug_change= models.IntegerField()
    tire_change= models.IntegerField()
    battery_change = models.IntegerField()
    vehicle_image= models.ImageField(upload_to="vehicleapp/static/")
    img_url= models.CharField(max_length=100,null=True, blank=True)
    rating = models.IntegerField()


@receiver(post_save, sender=vehicles)
def save_profile(sender, instance,created, **kwargs):
    if instance.img_url==None:
        instance.img_url= instance.vehicle_image.url.replace("vehicleapp/","/")
        instance.save()

class max_values(models.Model):
    mileage= models.IntegerField()
    price= models.IntegerField()
    oil_change= models.IntegerField()
    airfilter_change= models.IntegerField()
    spark_plug_change= models.IntegerField()
    tire_change= models.IntegerField()
    battery_change = models.IntegerField()
    
    
    
@receiver(post_save, sender=max_values)
def save_profile1(sender, instance,created, **kwargs):
    a=vehicles.objects.all()
    for i in a:
        mileage=(i.mileage/instance.mileage) *100
        price=(i.price/instance.price) *100
        oil_change=(i.oil_change/instance.oil_change) *100
        airfilter_change=(i.airfilter_change/instance.airfilter_change) *100
        tire_change=(i.tire_change/instance.tire_change) *100
        battery_change=(i.battery_change/instance.battery_change) *100
        av=(mileage+price+oil_change+airfilter_change+tire_change+battery_change)/6
        print(av)
        i.rating=av/20
        i.save()
        
        
