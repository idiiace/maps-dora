# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse

import json
from map.models import *

def polish_polygon(data):
	f=[]
	for i in data.split(','):
		try:
			lat,lng=i.split(' ')
			f.append({"lng":float(lng),"lat":float(lat)})
		except:pass

	return json.dumps(f)

# Create your views here.
def return_city_lat_lng(request,idd):
	a=City.objects.filter(id=int(idd))[0]
	a=polish_polygon(a.coordinates.polygon)
	return HttpResponse(a)

def return_id_city(request):
	a=City.objects.all()
	k={}
	for i in a:
		k[i.Name]=i.id
	k=json.dumps(k)
	return HttpResponse(k)

def return_county_lat_lng(request,idd):
	a=county.objects.filter(id=int(idd))[0]
	a=polish_polygon(a.coordinates.polygon)
	return HttpResponse(a)

def return_subcounty_lat_lng(request):
	a=subcounty.objects.filter(id=int(idd))[0]
	a=polish_polygon(a.coordinates.polygon)
	return HttpResponse(a)

