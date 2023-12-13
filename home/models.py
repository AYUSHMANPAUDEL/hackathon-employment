from django.db import models

# Create your models here.
class savedata(models.Model):
    firstname = models.CharField( max_length=50)
    lastname = models.CharField( max_length=50)
    birthday = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    password = models.CharField( max_length=50)
    phonenumber = models.CharField(max_length=10)
    date = models.DateField()
