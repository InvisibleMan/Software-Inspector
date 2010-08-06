from django.db import models
from django.contrib.auth.models import User

#class User(models.Model):
#    login = models.CharField(max_length=20)
#    password = models.CharField(max_length=20)
#    create_date = models.DateTimeField('date created')
#    
#    def __unicode__(self):
#        return self.login


class Soft(models.Model):
    name = models.CharField(max_length=50)
    # Здесь будет внешний ключ на производителя
    vendor = models.CharField(max_length=50)
    # Здесь будет внешний ключ на категорию
    url = models.URLField()
    
    def __unicode__(self):
        return self.name

class SoftVersion(models.Model):
    url = models.URLField()
    download_url = models.URLField()
    price = models.DecimalField()
    version = models.CharField(max_length=10)
    # платформа
    platform = models.PositiveIntegerField()

class SoftItem(models.Model):
    user = models.ForeignKey(User)
    soft = models.ForeignKey(SoftVersion)
