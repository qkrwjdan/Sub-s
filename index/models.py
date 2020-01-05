from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    
    female = '여'
    male = '남'
    gender_choice = [
        (female,'여'),
        (male,'남'),
    ]
    gender = models.CharField(
        max_length = 5,
        choices = gender_choice,
        default = female,
    )

    age = models.IntegerField(default = 0)
    job = models.CharField(max_length = 30)

    def __str__(self):
        return self.user.username

class Service(models.Model):
    service_name = models.CharField(max_length = 30)
    plan_name = models.CharField(max_length = 30)
    price = models.IntegerField(default = 0)
    detail = models.TextField()

    def __str__(self):
        return self.service_name + ' - ' + self.plan_name


class UsingPlan(models.Model):
    #이렇게 foreign키로만 단순하게 하는게 맞는걸까??
    user = models.ForeignKey(User,on_delete = models.CASCADE,null = True,default = None)
    service = models.ForeignKey(Service,on_delete = models.CASCADE, null = True,default = None)

    def __str__(self):
        return self.user.username + '-' + self.service.service_name

