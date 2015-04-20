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

    def readStreamPacket(self, _data, _client):
    	name = _data.getString()
    	clientId = _data.getString()
    	self.streamManager.server.clients[clientId].name = name