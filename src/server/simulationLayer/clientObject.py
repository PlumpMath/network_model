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
    
    def __init__(self, _server, _connection, _netAddress):
    	print "Client Object Created"

    	self.server = _server

    	# Net Connection info
    	self.connection = _connection
    	self.netAddress = _netAddress

    	# Control Object for this client
        self.name = None
    	self.controlObject = None

    	# Ghost objects of this client? or near it
    	self.ghostObjects = []

        # State
        self.state = {}

    def getState(self):

        self.state['pos'] = self.controlObject.position

        return self.state 
