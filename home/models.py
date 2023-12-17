from django.db import models
from django import forms
class WorkerStat(models.Model):
    worker_email=models.EmailField()
    verified = models.BooleanField(default=False)
    WORK_AREAS = [
        ('PL', 'Plumbing'),
        ('EL', 'Electrical'),
        ('O', 'Other'),
    ]
    workarea = models.CharField(max_length=30, choices=WORK_AREAS,default="")
    citizenship_image = models.ImageField(upload_to="media/",default="")
    certificate_image = models.ImageField(upload_to="media/" ,default="")

    def __str__(self):
        return self.worker_email_