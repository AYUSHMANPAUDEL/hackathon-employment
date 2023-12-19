from django.db import models
from django import forms
from django.contrib.auth.models import User

class Pofile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email_token = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)

class WorkerStat(models.Model):
    worker_user_name = models.CharField(max_length=40,default="",unique="True")
    worker_email=models.EmailField(primary_key=True)
    verified = models.BooleanField(default=False)
    WORK_AREAS = [
    ('EL', 'Electrical Services'),
    ('CA', 'Carpentry'),
    ('AR', 'Appliance Repair'),
    ('PA', 'Painting'),
    ('GA', 'Gardening/Landscaping'),
    ('RO', 'Roofing'),
    ('HV', 'HVAC (Heating, Ventilation, and Air Conditioning)'),
    ('FI', 'Flooring Installation/Repair'),
    ('WI', 'Window Installation/Repair'),
    ('LO', 'Locksmith Services'),
    ('PC', 'Pest Control'),
    ('DI', 'Drywall Installation/Repair'),
    ('FA', 'Furniture Assembly'),
    ('PW', 'Pressure Washing'),
    ('TI', 'Tile Installation/Repair'),
    ('HS', 'Home Security Installation'),
    ('ST', 'Septic Tank Maintenance'),
    ('GD', 'Garage Door Installation/Repair'),
    ('CS', 'Chimney Sweeping/Repair'),
    ('CI', 'Cabinet Installation/Repair'),
    ('FI', 'Fence Installation/Repair'),
    ('DC', 'Deck Construction/Repair'),
    ('GU', 'Gutter Cleaning/Installation'),
    ('CW', 'Concrete Work'),
    ('HT', 'Home Theater Installation'),
    ('PL', 'Plastering'),
    ('WP', 'Waterproofing'),
    ('SI', 'Solar Panel Installation'),
    ('ID', 'Interior Design'),
    ('HI', 'Home Inspection Services'),
    ]
    workarea = models.CharField(max_length=30, choices=WORK_AREAS,default="")
    citizenship_image = models.ImageField(upload_to="static/media/citizen",default="")
    certificate_image = models.ImageField(upload_to="static/media/certificate" ,default="")

    def __str__(self):
        return self.worker_email 
    
class UserData(models.Model):
    user_name = models.CharField(max_length=40,default="",unique=True)
    user_email=models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=20,default="")
    last_name = models.CharField(max_length=20,default="")
    user_image = models.ImageField(upload_to="static/media/userimage" ,default="")
    def __str__(self):
        return self.user_email
    