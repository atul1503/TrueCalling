from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin




class UserPhoneLabelMapping(models.Model):
    username=models.CharField(max_length=100,null=True)
    fullname=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=15)
    

    label_types=[
        ('SPAM','SPAM'),
        ('SALES',"SALES"),
        ('FRAUD','FRAUD'),
        ('VERIFIED','VERIFIED')
    ]

    label=models.CharField(choices=label_types,max_length=50)


