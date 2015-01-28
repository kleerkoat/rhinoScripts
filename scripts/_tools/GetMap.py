# Written by Lorenz Lachauer, 28.6.2011
# License: CC-BY-NC-SA
# eat-a-bug.blogspot.com
# This script imports a static map form OpenStreetMaps, 
# based on an adress entered by the user


import urllib,urllib2,time
import os, Rhino, scriptcontext
import rhinoscriptsyntax as rs
import re, socket, math


def GetMap():
    socket.setdefaulttimeout(10)
    filename='c:\\map.jpg' # you migth hve to change this path
    street = rs.GetString('Street')
    city = rs.GetString('City')
    country = rs.GetString('Country')
    zoom = rs.GetInteger('Zoom', 17, 1, 19)
    rs.UnitSystem(4, True)
    url='http://nominatim.openstreetmap.org/search?q='+street+','+city+','+country+'&format=xml'
    rs.CurrentView('Top')
    try:
        xml = urllib.urlopen(url).read()
    except:
        print 'http://nominatim.openstreetmap.org produced an error'
        return
    temp = xml[xml.find("lat=")+5:-1]
    lat= temp[0:temp.find("'")]
    temp = xml[xml.find("lon=")+5:-1]
    lng= temp[0:temp.find("'")]
    print 'Latitude, Longitude: '+lat+", "+lng
    picture_page = 'http://osm-tah-cache.firefishy.com/MapOf/?lat='+lat+'&long='+lng+'&z='+str(zoom)+'&w=1000&h=1000&format=jpeg'
    opener1 = urllib2.build_opener()
    try:
        page1 = opener1.open(picture_page)
        my_picture = page1.read()
    except:
        print 'http://osm-tah-cache.firefishy.com produced an error'
        return
    try:
        fout = open(filename, 'wb')
        fout.write(my_picture)
        fout.close()
    except:
        print 'writing of '+path+' produced an error'
        return
    res =  40075017 * math.cos(float(lat)/180*math.pi) / (256 * 2 ** zoom) *1000
    rs.Command('_-BackgroundBitmap Remove _Enter',False)
    rs.Command('_-BackgroundBitmap '+filename+' '+str(-res/2)+','+str(-res/2)+',0 '+str(res/2)+','+str(res/2)+',0 _Enter',True)
    rs.Command('_-BackgroundBitmap Grayscale=No _Enter', False)
    rs.Command('_-EarthAnchorPoint Latitude '+lat+' Longitude '+lng+' _Enter _Enter _Enter _Enter _Enter', False)

GetMap()