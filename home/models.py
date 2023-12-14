from django.db import models

# Create your models here.
class Request(models.Model):
    name=models.CharField( max_length=50)
    phone=models.CharField( max_length=12)
    address=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    problem=models.TextField()
    date=models.DateField()