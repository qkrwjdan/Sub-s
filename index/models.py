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

