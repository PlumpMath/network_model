#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys

### PANDA Imports ###
from direct.task.Task import Task

## Server Imports ##
from simulationLayer.controlObject import ControlObject

########################################################################
# The Ghost manager provides two key functions: the "ghosting" of 
# objects from one host to another, and the transferring of state 
# information between the original object and its ghost.  A ghost 
# is a copy of an object persisted and transmitted to a remote 
# host.

# Ghost manager talks to client ghosts. Regarding data from the server
# Control Objects


class GhostManager():
    
    def __init__(self, _streamManager):
    	print "Loaded Ghost Manager"

    	# Stream manager ref
    	self.streamManager = _streamManager

    def readStreamPacket(self, _data, _client):
    	pass


    def ghostManagerData(self, _packet, _data=[]):
    	"""Should add ghost manager data on the packet
    	packet:
    	opcode int8
    	managerCode int8
    	data...
    	"""
    	pkt = _packet
    	return pkt


    def createClientControlObject(self, _clientId, _clientConnection):
    	clientObj = self.streamManager.server.clients[_clientId]
    	clientObj.controlObject = ControlObject(clientObj, _clientId)

    	# Send the client an updated datablock containing info about the currect game state
    	self.streamManager.datablockManager.sendPreGameData(_clientConnection)

    	if len(self.streamManager.server.clients) > 1:
    		self.streamManager.datablockManager.broadcastNewClientUpdate(_clientId)