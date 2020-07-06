# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models as models


class Coordinate(models.Model):

    # Fields
    polygon = models.TextField()


class Country(models.Model):

    # Fields
    Name = models.TextField(max_length=250)
    coordinates = models.ForeignKey(Coordinate)
    
    def __unicode__(self):
        return self.Name;  


class City(models.Model):

    # Fields
    Name = models.TextField(max_length=250)
    parent = models.ForeignKey(Country)
    coordinates = models.ForeignKey(Coordinate)
    def __unicode__(self):
        return self.Name;  


class county(models.Model):

    # Fields

    name = models.CharField(max_length=255)
    parent = models.ForeignKey(City)
    coordinates = models.ForeignKey(Coordinate)
    def __unicode__(self):
        return self.name;  


class subcounties(models.Model):

    # Fields
    Name = models.TextField(max_length=100)
    parent = models.ForeignKey(county)
    coordinates = models.ForeignKey(Coordinate)
    def __unicode__(self):
        return self.Name;  




