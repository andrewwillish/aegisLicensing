__author__ = 'andrew.willis'

import urllib2, urllib
import hashlib

import aegisControlCore

data = [('licenseNumber', str(hashlib.md5('123456789').hexdigest())),\
    ('clientId', str(hashlib.md5('syalala').hexdigest())),\
    ('blockStatus', 'andrewwillish@gmail.com'),\
    ('expiryDate', 'bweeek')]
