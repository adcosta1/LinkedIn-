from django.db import models
from django.contrib.auth.models import User
import pycountry



class Education(models.Model):

    id = models.AutoField(primary_key=True)
    graduationyear = models.IntegerField()
    degreename = models.CharField(max_length=30)
    institutionname = models.CharField(max_length=50)
    userid = models.IntegerField(null=True,blank=True)
    

class ProfessionalExperience(models.Model):
    id = models.AutoField(primary_key=True)
    date_init = models.DateField(null=True,blank=True,auto_now=False)
    date_end = models.DateField(null=True,blank=True,auto_now=False)
    role = models.CharField(max_length=50)
    company_name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    userid = models.IntegerField(null=True,blank=True)

class LinkedinUser(User):
    STATE_CHOICES = []
    for state in pycountry.subdivisions.get(country_code='US'):
        STATE_CHOICES.append((state.code, state.name))
        
    CATEGORY_CHOICES=[('Tech','Tech'),('Advocacy','Advocacy'),('Medicine','Medicine'),('Engineering','Engineering'),('Humans','Humans'),('Math','Math')]
    
    photo = models.FileField(upload_to='static/media',null=True,blank=True)
    gender = models.CharField(max_length=10, choices= (("Men", "Men"), ("Woman", "Woman"), ("Non","I prefer not to identify")))
    state = models.CharField(max_length=5, choices=STATE_CHOICES)
    DOB = models.DateField()
    Race = models.CharField(max_length=10, choices=(("B", "Black"), ("W", "White"), ("N", "Native"), ("A","Asian"), ("O", "Other")))
    Bio = models.CharField(max_length=500)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,null=True,blank=True)
    education = models.OneToOneField(Education,null=True,blank=True, on_delete=models.CASCADE)
    experience = models.OneToOneField(ProfessionalExperience,null=True,blank=True, on_delete=models.CASCADE)


    

    

    
    
    

