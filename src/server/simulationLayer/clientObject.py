#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys

### PANDA Imports ###

## Server Imports ##

########################################################################
# Store a client object for each client in server.clients
# A client object will store all information regarding that client

class Client():
    
    def __init__(self, _id, _server, _connection, _netAddress):
    	print "Client Object Created"

    	self.server = _server

    	# Net Connection info
        self.id = _id
    	self.connection = _connection
    	self.netAddress = _netAddress

    	# Control Object for this client
        self.name = None
    	self.controlObject = None

    	# Ghost objects of this client? or near it
    	self.ghostObjects = []

        # Movecmds
        self.moveCmds = []



    def start(self):
        self.clientUpdateData = {}
        self.clientUpdateData[self.controlObject.id] = {}

    def getState(self):
        self.clientUpdateData[self.controlObject.id]['pos'] = self.controlObject.position
        #self.clientUpdateData[self.controlObject.id]['time'] = self.controlObject.time

        return self.clientUpdateData


    def handleMovement(self, _timeStep):
        if self.controlObject != None:
            self.controlObject.doMovement(self.moveCmds, _timeStep)
        self.moveCmds = []