from django.db import models
from django import forms
class WorkerStat(models.Model):
    worker_email=models.EmailField()
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
    citizenship_image = models.ImageField(upload_to="media/",default="")
    certificate_image = models.ImageField(upload_to="media/" ,default="")

    def __str__(self):
        return self.worker_email_