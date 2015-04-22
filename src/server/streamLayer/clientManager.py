#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys

### PANDA Imports ###
from direct.task.Task import Task

## Server Imports ##

########################################################################


class ClientManager():
    
    def __init__(self, _streamManager):
    	print "Loaded Client Manager"

    	# Stream manager ref
    	self.streamManager = _streamManager

    def readStreamPacket(self, _data, _clientConnection):
    	name = _data.getString()
    	clientId = _data.getString()
    	self.streamManager.server.clients[clientId].name = name
    	# Send msg to all players that player "name" connected
    	# Tell ghostManager that it needs to create objects for the client and the other clients on the server
    	self.streamManager.ghostManager.createClientControlObject(clientId, _clientConnection)
    	# When done create a datablock and send the data to the client.
    	# From there it should only be the movemanager that handles the clients movements for now
    	