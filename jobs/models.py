from django.db import models
from accounts.models import LinkedinUser

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, null=True,blank=True)
    description = models.CharField(max_length=300)
    postedby = models.ForeignKey(LinkedinUser, on_delete=models.CASCADE)
    deadline_date = models.DateField(auto_now=False)