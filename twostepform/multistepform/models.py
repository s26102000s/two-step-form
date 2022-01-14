from django.db import models

# Create your models here.
class MultiStepFormModel(models.Model):
    id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)
    marrital=models.CharField(max_length=255)
    father=models.CharField(max_length=255)
    spouse=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    objects=models.Manager()