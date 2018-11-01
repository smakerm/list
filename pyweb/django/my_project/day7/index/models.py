from django.db import models

# Create your models here.
class Users(models.Model):
    uname = models.CharField(max_length=30)
    upass = models.CharField(max_length=30)
    uemail = models.EmailField()