from django.db import models

# Create your models here.

class Client(models.Model):
    Name=models.CharField(max_length=30)
    Mobile=models.PositiveIntegerField()
    Email=models.CharField(max_length=20)
    Company_Name=models.CharField(max_length=15)
    Currency=models.CharField(max_length=50)
    Billing_method=models.CharField(max_length=50)
    Profile_picture=models.FileField()
