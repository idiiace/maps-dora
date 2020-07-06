import xmltodict as xm
from map.models import *

coun={}


def return_counties():
    a=open("C:\projectmaps\djanmaps\maps\delimiters\counties\counties.kml").read()
    cntjs=xm.parse(a)
    return cntjs

def return_subcounties():
    a=open("C:\projectmaps\djanmaps\maps\delimiters\subcounties\sub.kml").read()
    cntjs=xm.parse(a)
    return cntjs

def populate_database():
    cntjs=return_counties()
    coun={}
    count=0
    for i in cntjs[u'kml'][u'Document']['Folder']['Placemark']:
        cty=i[u'ExtendedData'][u'SchemaData']['SimpleData'][1]['#text']
        print cty
        countyy=i[u'ExtendedData'][u'SchemaData']['SimpleData'][2]['#text']
        try:
            coun[cty]
        except:coun[cty]=[]
        try:
            cord=i['MultiGeometry']['Polygon'][u'outerBoundaryIs'][u'LinearRing'][u'coordinates']
            coun[cty].append({countyy:cord})
        except:
            count+=1
    print count
            
        #except:print "error"
    return coun

def add_counties():
    a=populate_database()
    for city in a.keys():
        city=City.objects.filter(Name=city)[0]
        for x in a[city.Name]:
            coun=x.keys()[0]
            cord=x[coun]
            v=county()
            v.name=coun
            v.parent=city
            cod=Coordinate()
            cod.polygon=cord
            cod.save()
            v.coordinates=cod
            v.save()
            print "Sucessfully Saved County"

def add_subcounties():
    cntjs=return_subcounties()
    coun={}
    count=0
    for i in cntjs[u'kml'][u'Document']['Folder']['Placemark']:
        cty=i[u'ExtendedData'][u'SchemaData']['SimpleData'][1]['#text']
        countyy=i[u'ExtendedData'][u'SchemaData']['SimpleData'][2]['#text']
        sub=i[u'ExtendedData'][u'SchemaData']['SimpleData'][3]['#text']
        z=i
        #make sure the subcounty is inheriting the right parent
        subparent=county.objects.filter(name=countyy)
        for i in subparent:
            try:
                if i.parent.Name==cty:
                    su=subcounties()
                    su.Name=sub
                    su.parent=i
                    c=Coordinate()
                    c.polygon=z['MultiGeometry']['Polygon'][u'outerBoundaryIs'][u'LinearRing'][u'coordinates']
                    c.save()

                    #['MultiGeometry']['Polygon'][u'outerBoundaryIs'][u'LinearRing'][u'coordinates']
                    su.coordinates=c
                    su.save()
                    print "saved ",sub
                    break
            except:
                count+=1
    print count

 
                
        

    
                
                



        




