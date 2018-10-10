from django.db import models

# Create your models here.


class Users(models.Model):
    uphone = models.CharField(max_length=20)
    upass = models.CharField(max_length=50)
    uemail = models.EmailField()
    uname = models.CharField(max_length=20, null=True)
    isActive = models.BooleanField(default=True)
