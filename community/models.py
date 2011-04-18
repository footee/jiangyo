# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
from datetime import datetime

class Area(models.Model):
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    url = models.TextField(null=False, blank=False)
    name = models.TextField(null=False, blank=False)
    community = models.IntegerField(null=False, blank=False)
    class Meta:
        db_table = u'area'

class CommunityInfo(models.Model):
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    url = models.IntegerField(null=False, blank=False)
    name = models.TextField(null=False, blank=False)
    latitude = models.DecimalField(null=True, blank=True, max_digits=3, decimal_places=15)
    longitude = models.DecimalField(null=True, blank=True, max_digits=3, decimal_places=15))
    location = models.TextField(null=True, blank=True)
    sale_trends = models.TextField(null=True, blank=True)
    rental_trends = models.TextField(null=True, blank=True)
    houses = models.IntegerField(null=True, blank=True)
    pack = models.TextField(null=True, blank=True)
    developer = models.TextField(null=True, blank=True)
    tenement = models.TextField(null=True, blank=True)
    tenement_type = models.TextField(null=True, blank=True)
    building_date = models.DateField(null=True, blank=True)
    plot_ratio = models.TextField(null=True, blank=True, max_digits=3, decimal_places=3) # This field type is a guess.
    afforest = models.DecimalField(null=True, blank=True, max_digits=3, decimal_places=3) # This field type is a guess.
    area = models.TextField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
    class Meta:
        db_table = u'community_info'

class CommunityPrice(models.Model):
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    info = models.ForeignKey(CommunityInfo)
    price = models.IntegerField(null=True, blank=True)
    sales = models.IntegerField(null=True, blank=True)
    sale_1 = models.IntegerField(null=True, blank=True)
    sale_2 = models.IntegerField(null=True, blank=True)
    sale_3 = models.IntegerField(null=True, blank=True)
    sale_4 = models.IntegerField(null=True, blank=True)
    sale_5 = models.IntegerField(null=True, blank=True)
    sale_6 = models.IntegerField(null=True, blank=True)
    rental = models.IntegerField(null=True, blank=True)
    rents = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
    class Meta:
        db_table = u'community_price'

