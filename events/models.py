from django.db import models
from accounts.models import LinkedinUser

class Events(models.Model):
    CATEGORY_CHOICES=[('Tech','Tech'),('Advocacy','Advocacy'),('Medicine','Medicine'),('Engineering','Engineering'),('Humans','Humans'),('Math','Math')]
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, null=True,blank=True)
    description = models.CharField(max_length=500)
    date = models.DateField(auto_now=False)
    organizer = models.ForeignKey(LinkedinUser,on_delete=models.CASCADE,null=True,blank=True)
    photo = models.ImageField(upload_to='static/media',null=True,blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,null=True,blank=True)
    
    
