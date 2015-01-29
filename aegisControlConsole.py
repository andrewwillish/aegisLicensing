__author__ = 'andrew.willis'

import ctypes
import time
import datetime
import os
import sys
import aegisControlCore

class controlConsole:
    def __init__(self):
        #invoking main menu looping around to keep asking for new order
        while True:
            os.system('cls')
            print 'Aegis Controller - v1.0'
            print ''
            commandVar = raw_input('Insert Command >> ')

            os.system('cls')

            #Parsing command
            if commandVar == 'exit':
                sys.exit(0)
            elif commandVar == '':
                pass
            elif commandVar == 'help':
                self.printHelp()
            elif commandVar == 'regClient':
                self.regClient()
            else:
                print ('invalid command')
            print ''
        return

    def printHelp(self, *args):
        print 'help\t\t- Show this help menu'
        print 'regClient\t\t- Register new client to database'
        return

    def regClient(self):
        clientName = raw_input('Enter client name >> ')
        os.system('cls')
        clientPassword, clientPasswordConf = 'a', 'b'
        retake = False
        while clientPassword != clientPasswordConf:
            if clientPassword != clientPasswordConf and retake is True:
                print 'Password confirmation is not match'
            retake = True
            clientPassword = raw_input('Enter client password >> ')
            clientPasswordConf = raw_input('Confirm client password >> ')
            os.system('cls')
        os.system('cls')
        clientEmail = raw_input('Enter client email >> ')
        os.system('cls')
        clientContact = raw_input('Enter client contact detail >> ')
        os.system('cls')

        print 'Client Name : ', clientName
        print 'Client Password : ', clientPassword
        print 'Client Name : ', clientEmail
        print 'Client Name : ', clientContact
        rep = raw_input('Confirm client record? [y/n]')
        if rep == 'y':
            data = [('licenseNumber', str(hashlib.md5('123456789').hexdigest())),\
                ('clientId', str(hashlib.md5('syalala').hexdigest())),\
                ('blockStatus', 'andrewwillish@gmail.com'),\
                ('expiryDate', 'bweeek')]
            aegisControlCore.webCom()
        return
controlConsole()