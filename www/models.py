# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Soft(models.Model):
    name = models.CharField(max_length=50)
    # Здесь будет внешний ключ на производителя
    vendor = models.CharField(max_length=50)
    # Здесь будет внешний ключ на категорию
    url = models.URLField(verify_exists=False, null=True, blank=True)
    
    def __unicode__(self):
        return self.name

class SoftVersion(models.Model):
    name = models.CharField(max_length=50)
    soft = models.ForeignKey(Soft)
    url = models.URLField(verify_exists=False, null=True, blank=True)
    download_url = models.URLField(verify_exists=False, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    version = models.CharField(max_length=10)
    user_version = models.CharField(max_length=10)
    # платформа
    platform = models.PositiveIntegerField()
    
    def __unicode__(self):
        return self.name

class SoftItem(models.Model):
    user = models.ForeignKey(User)
    soft_version = models.ForeignKey(SoftVersion)
