#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys

### PANDA Imports ###
from direct.task.Task import Task

## Server Imports ##

########################################################################
# The Datablock manager provides "latest state" delivery of 
# datablocks from the server to the client. Datablocks are objects 
# which contain relatively static data and the manager guarantees 
# delivery only of the latest state at a very low frequency. Like 
# the Ghost manager, the Datablock manager is asymmetric, and 
# datablocks are only transmitted from server to client. The most 
# common use of datablocks is to transmit initialization or 
# reference data for ghosts.

# For now datablocks will be used for the first initialization of game data
# also it would be the first talk between client and server and back to client


class DatablockManager():
    
    def __init__(self, _streamManager):
    	print "Loaded Datablock Manager"

    	# Stream manager ref
    	self.streamManager = _streamManager

    def readStreamPacket(self, _data, _client):
    	pass


    def buildDatablock(self, _clientConnection=None, _dataLength=0, _data=[]):
    	pkt = self.streamManager.buildPacket(2, 2)
        pkt.addUint8(_dataLength)

    	for index in range(len(_data)):
            pkt.addString(_data[index])

    	return pkt



    def sendPreGameData(self, _clientConnection):
    	# Build a packet that contains all the needed data for this client
    	# to create ghost object and the control object for that client.
        currectControlClientIds = []
        count = 0
        for client in self.streamManager.server.clients:
            if self.streamManager.server.clients[client].controlObject:
                count += 1
                name = self.streamManager.server.clients[client].name
                currectControlClientIds.append(client +","+ name)

        pkt = self.buildDatablock(_clientConnection, count, currectControlClientIds)

        self.streamManager.server.connectionMgr.sendPacket(pkt, _clientConnection)

    def broadcastNewClientUpdate(self, _clientId):
        clients = self.streamManager.server.clients
        clientName = clients[_clientId].name
        data = [_clientId + "," + clientName]
        for client in clients:
            if client != _clientId:
                conn = clients[client].connection
                pkt = self.buildDatablock(None, 1, data)
                self.streamManager.server.connectionMgr.sendPacket(pkt, conn)

