from django.db import models
from django.contrib.auth.models import User

class State(models.Model):
    id=models.AutoField(primary_key=True)
    state=models.CharField(max_length=15)

class MyUser(User):
    #gender= models.Choices({"Men": "Men", "Woman": "Woman", "Non":"I prefer not to identify"})
    state= models.ForeignKey(State,on_delete=models.PROTECT)
    DOB= models.DateField(auto_now=False)
    #Race=models.Choices({"B": "Black", "W": "White", "N": "Native", "A":"Asian", "O": "Other"})
    Bio= models.CharField(max_length=500)
    


