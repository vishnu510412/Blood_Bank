from django.db import models

# Create your models here.


class UserReg(models.Model):

    user1 = models.CharField(max_length=60)
    donardts = models.CharField(max_length=50)
    bdgroup  = models.CharField(max_length=40)
    age = models.CharField(max_length=40 )





    
