from __future__ import unicode_literals
from django.db import models


# Create your models here.
class BookInfo(models.Model):
    num = models.CharField(max_length=12, default=None)
    name = models.CharField(max_length=1000, default=None)
    price = models.CharField(max_length=10, default=None)
    ISBN = models.CharField(max_length=15, default=None)
    author = models.CharField(max_length=1000, default=None)
    publisher = models.CharField(max_length=50, default=None)
    img = models.ImageField(default=None)
    website = models.CharField(max_length=120, default=None)
    sales = models.IntegerField(max_length=10, default=0)
    comment1 = models.CharField(max_length=512)
    comment2 = models.CharField(max_length=512)
    comment3 = models.CharField(max_length=512)
    comment4 = models.CharField(max_length=512)
    comment5 = models.CharField(max_length=512)
    comment6 = models.CharField(max_length=512)
    comment7 = models.CharField(max_length=512)
    comment8 = models.CharField(max_length=512)
    comment9 = models.CharField(max_length=512)
    comment10 = models.CharField(max_length=512)

    class Meta:
        verbose_name = '书本信息'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name


class Best_seller(models.Model):
    num = models.CharField(max_length=12, default=None)
    name = models.CharField(max_length=100, default=None)

    class Meta:
        verbose_name = '畅销'
        verbose_name_plural = verbose_name


class hot_search(models.Model):
    name = models.CharField(max_length=100, default=None)

    class Meta:
        verbose_name = '热搜'
        verbose_name_plural = verbose_name


class UserModel(models.Model):  # 创建userModel表  用户表
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class MyCollect(models.Model):
    username = models.CharField(max_length=50)
    num = models.CharField(max_length=12, default=None)
    name = models.CharField(max_length=1000, default=None)
    price = models.CharField(max_length=10, default=None)
    ISBN = models.CharField(max_length=15, default=None)
    author = models.CharField(max_length=1000, default=None)
    publisher = models.CharField(max_length=50, default=None)
    img = models.ImageField(default=None)
    website = models.CharField(max_length=120, default=None)
    sales = models.IntegerField(max_length=10, default=0)

    class Meta:
        verbose_name = '个人收藏'
        verbose_name_plural = verbose_name


class Score(models.Model):
    username = models.CharField(max_length=50)
    num = models.CharField(max_length=12, default=None)
    name = models.CharField(max_length=1000, default=None)
    score = models.IntegerField(default=1)
    price = models.CharField(max_length=10, default=None)
    ISBN = models.CharField(max_length=15, default=None)
    author = models.CharField(max_length=1000, default=None)
    publisher = models.CharField(max_length=50, default=None)
    img = models.ImageField(default=None)
    website = models.CharField(max_length=120, default=None)
    sales = models.IntegerField(max_length=10, default=0)

    class Meta:
        verbose_name = '得分'
        verbose_name_plural = verbose_name