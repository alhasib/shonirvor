# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Division(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=45)
    division = models.ForeignKey(Division)

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=45)
    District = models.ForeignKey(District)

    def __str__(self):
        return self.name

class Profile(models.Model):
    full_name = models.CharField(max_length=45)
    area = models.ForeignKey(Area)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=70,blank=True)
    facebook_link = models.CharField(max_length=250,blank=True)
    linkedin_link = models.CharField(max_length=250,blank=True)
    adress = models.TextField(max_length=500,blank=True)
    profile_image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.full_name
