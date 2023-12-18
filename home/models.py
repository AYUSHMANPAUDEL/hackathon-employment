from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

# Create your models here.
# class Savedata(models.Model):
#     firstname = models.CharField( max_length=50)
#     lastname = models.CharField( max_length=50)
#     birthday = models.CharField( max_length=50)
#     email = models.CharField( max_length=50)
#     password = models.CharField( max_length=50)
#     phonenumber = models.CharField(max_length=10)
#     date = models.DateField()
# Create your models here.
class Request(models.Model):
    name=models.CharField( max_length=50)
    phone=models.CharField( max_length=12)
    address=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    selected=models.CharField( max_length=50, null=True)
    problem=models.TextField()
    date=models.DateField()
    accepted_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='accepted_requests')
    is_accepted = models.BooleanField(default=False)
    accepted_date=models.DateField(null=True)