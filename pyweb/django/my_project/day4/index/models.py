from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30,verbose_name='名称')
    address = models.CharField(max_length=50,verbose_name='地址')
    city = models.CharField(max_length=20,verbose_name='所在城市')
    country = models.CharField(max_length=30,verbose_name='国家')
    website = models.URLField(verbose_name='网址')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "出版社"
        verbose_name_plural = verbose_name

class Author(models.Model):
    name = models.CharField(max_length=20,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(null=True,verbose_name='邮箱')
    picture = models.ImageField(null=True,verbose_name='头像',upload_to='static/upload/usrimg')
    publisher = models.ManyToManyField(Publisher,verbose_name="签约出版社")

    def __str__(self):
        return self.name

    class Meta:
        # db_table = 'author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name
        ordering = ['age','-id']

class Book(models.Model):
    title = models.CharField(max_length=50,verbose_name='书名')
    publication_date = models.DateField(default = timezone.now,verbose_name='出版日期')
    publisher = models.ForeignKey(Publisher,null=True,verbose_name='出版社')
    author = models.ManyToManyField(Author,verbose_name='作者')


    def __str__(self):
        return self.title

    class Meta:

        verbose_name = '图书'
        verbose_name_plural = verbose_name
        ordering = ['-publication_date']

class Wife(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    author = models.OneToOneField(Author,null=True,verbose_name='相公')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '娘子'
        verbose_name_plural = verbose_name