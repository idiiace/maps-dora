# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *
# Register your models here.


class subcountiesAdmin(admin.ModelAdmin):
    list_display = ('Name', 'parent')

class cityAdmin(admin.ModelAdmin):
    list_display = ('Name', 'parent','id')

class countyAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


admin.site.register(county,countyAdmin)
admin.site.register(subcounties,subcountiesAdmin)
admin.site.register(City,cityAdmin)


