from django.db import models
from accounts.models import LinkedinUser
import pycountry

class Job(models.Model):
    from accounts.models import LinkedinUser
    CATEGORY_CHOICES=[('Tech','Tech'),('Advocacy','Advocacy'),('Medicine','Medicine'),('Engineering','Engineering'),('Humans','Humans'),('Math','Math')]
    STATE_CHOICES = []
    for state in pycountry.subdivisions.get(country_code='US'):
        STATE_CHOICES.append((state.code, state.name))
    
    id = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to='static/media',null=True,blank=True)
    title = models.CharField(max_length=30, null=True,blank=True)
    description = models.CharField(max_length=300)
    postedby = models.ForeignKey(LinkedinUser, on_delete=models.CASCADE,null=True,blank=True)
    deadline_date = models.DateField(auto_now=False)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,null=True,blank=True)
    link = models.URLField(null=True,blank=True)
    state = models.CharField(max_length=5, choices=STATE_CHOICES, null=True,blank=True)
    
