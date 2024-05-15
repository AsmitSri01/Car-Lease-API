from django.db import models

# Create your models here.
class Car(models.Model):
    name=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    status=models.CharField(max_length=100,default='available')
    transmission=models.CharField(max_length=20)


class Lease(models.Model):
    driver_id=models.CharField(max_length=100)
    car=models.ForeignKey(Car,on_delete=models.CASCADE)
    