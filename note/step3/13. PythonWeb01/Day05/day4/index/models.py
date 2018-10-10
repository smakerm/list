from django.db import models
import datetime

# Create your models here.
# 实体类 : Publisher
# 对应到数据库中的一张表
# 该类中的每个属性,会对应到数据表中的每个字段


class Publisher(models.Model):
    name = models.CharField(max_length=30, default='匿名')
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    website = models.URLField()


class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(null=True)


class Book(models.Model):
    title = models.CharField(max_length=50)
    publication_date = models.DateField()
