from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    studid = models.IntegerField(primary_key=True,unique=True) 
    name = models.CharField(max_length=128)
    age = models.IntegerField(default=0)
    marks = models.IntegerField(default=0)
    sex = models.CharField(max_length=13,default="NotSpecified")
    def __unicode__(self):
        return self.name
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    def __unicode__(self):
        return self.user.username
