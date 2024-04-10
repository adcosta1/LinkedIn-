from django.db import models
from django.contrib.auth.models import User
import pycountry



class LinkedinUser(User):
    STATE_CHOICES = []
    for state in pycountry.subdivisions.get(country_code='US'):
        STATE_CHOICES.append((state.code, state.name))
    
    
    gender = models.CharField(max_length=10, choices= (("Men", "Men"), ("Woman", "Woman"), ("Non","I prefer not to identify")))
    state = models.CharField(max_length=5, choices=STATE_CHOICES)
    DOB = models.DateField()
    Race = models.CharField(max_length=10, choices=(("B", "Black"), ("W", "White"), ("N", "Native"), ("A","Asian"), ("O", "Other")))
    Bio = models.CharField(max_length=500)
    
    
class Education(models.Model):
    id = models.AutoField(primary_key=True)
    graduationyear = models.IntegerField()
    degreename = models.CharField(max_length=30)
    institutionname = models.CharField(max_length=50)
    user = models.ForeignKey(LinkedinUser,on_delete=models.CASCADE)
    
class ProfessionalExperience(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now=False)
    user = models.ForeignKey(LinkedinUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    company_name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    
class Job(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, null=True,blank=True)
    description = models.CharField(max_length=300)
    postedby = models.ForeignKey(LinkedinUser, on_delete=models.CASCADE)
    deadline_date = models.DateField(auto_now=False)
    
class Events(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, null=True,blank=True)
    description = models.CharField(max_length=500)
    date = models.DateField(auto_now=False)
    organizer = models.ForeignKey(LinkedinUser, on_delete=models.CASCADE)
    
    
    


