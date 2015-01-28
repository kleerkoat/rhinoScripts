#!/usr/bin/python
# -*- coding: utf-8 -*-

# Rhumblr 0.1 – written by Lorenz Lachauer – 2011-02-14

from urllib2 import Request, urlopen, HTTPError
from urllib import urlencode
import re
import rhinoscriptsyntax as rs

def PostViewToTumblr(email, password):
    size = rs.ViewSize()
    path = '\\mypic.png'
    rs.Command('-_ViewCaptureToFile ' + path + ' Width=' + str(size[0]) + ' Height=' + str(size[1]) + ' DrawGrid=Yes DrawWorldAxes=Yes DrawCPlaneAxes=Yes _Enter', 0)
    print 'Post ' + rs.CurrentView() + ' view to tumblr' 
    comment = rs.StringBox (title='Add a caption to your post')

    url = 'http://www.tumblr.com/api/write'

    img=open(path, 'rb').read()

    values = {
    'type': 'photo',
    'email': email,
    'password': password,
    'data': img,
    'send-to-twitter': 'auto',
    'caption' : comment}
    
    data = urlencode(values,'utf-8')
    req = Request(url, data)

    try:
        response = urlopen(req)
        page = response.read()
        print 'Upload successful'
    except HTTPError, e:
        print 'Upload failed ' + e.code

#PostViewToTumblr(<your email>, <your password>)
PostViewToTumblr('monkeygrip@gmail.com', 'rrg1235')

