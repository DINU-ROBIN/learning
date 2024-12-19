from django.db import models

# Create your models here.

class create(models.Model):
    username=models.CharField(max_length=10,unique=True)
    userpassword=models.CharField(max_length=100)
