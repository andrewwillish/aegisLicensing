__author__ = 'andrew.willis'

import os
import random
import getpass
import hashlib
import urllib, urllib2

CURRENT_USER = str(getpass.getuser())
SCRIPT_ROOT = os.path.dirname(os.path.realpath(__file__)).replace('\\','/')
WIN_ROOT = os.environ['ProgramFiles'][:2]+'/'

#cutom error declaration
class aegisError(Exception):
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return repr(self.text)

#generate validation code
def genValidationCode(*args):
    #generate first and second code generation
    firstGenCode = str(random.randint(0, 50))
    secGenCode = str(random.randint(50, 99))

    if len(firstGenCode) == 1: firstGenCode = '0' + firstGenCode
    if len(secGenCode) == 1: secGenCode = '0' + secGenCode

    firstGenCode = firstGenCode.replace('0', str(random.randint(0, 9)))
    secGenCode = secGenCode.replace('0', str(random.randint(0, 9)))

    firstModulo = int(firstGenCode[0]) % int(firstGenCode[1])
    secModulo = int(secGenCode[0]) %  int(secGenCode[1])

    lastDigit = secModulo - firstModulo
    if lastDigit <=0 : lastDigit = lastDigit * -1

    validationCode = str(firstGenCode) + str(secGenCode) + str(lastDigit)
    return validationCode

#web communication
def webCom(data=[], url=None):
    if url is None: raise ValueError, 'url data is not specified'
    dataPack = urllib.urlencode(data)
    req = urllib2.Request(url, dataPack)
    req.add_header("Content-type", "application/x-www-form-urlencoded")
    ret = urllib2.urlopen(req).read()
    return ret