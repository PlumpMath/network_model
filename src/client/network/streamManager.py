#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys

### PANDA Imports ###
from direct.task.Task import Task
from panda3d.core import Datagram

## Client Imports ##
from managerCodes import *
from datablockManager import DatablockManager
from ghostManager import GhostManager

########################################################################
# The Stream manager passes the packets to the correct sub managers.
# The stream manager handles the building of packets, data are gathered from 
# sub managers


class StreamManager():
    
    def __init__(self, _client):
    	print "Loaded Stream Manager"

    	# Server ref
    	self.client = _client

    	# init Sub Managers
    	self.datablockManager = DatablockManager(self)
        self.ghostManager = GhostManager(self)


    def handlePacket(self, _opcode, _managerCode, _data):
    	"""Read the packets and pass to the correct sub manager"""

    	if _managerCode == DATABLOCK_MANAGER:
    		self.datablockManager.readStreamPacket(_data)
    	
    	if _managerCode == MOVE_MANAGER:
    		self.moveManager.readStreamPacket(_data)

    	if _managerCode == GHOST_MANAGER:
    		self.ghostManager.readStreamPacket(_data)

        if _managerCode == MOTD:
            self.readMOTD(_data)


    def buildPacket(self, _opcode, _managerCode=None):

    	pkt = Datagram()
    	pkt.addUint8(_opcode)

    	if _managerCode == MOVE_MANAGER:
    		pkt.addUint8(_managerCode)

        if _managerCode == MOTD:
            pkt.addUint8(_managerCode) # MOTD code

        return pkt


    def readMOTD(self, _data):
        motd = _data.getString()
        clientId = _data.getString()
        self.client.id = clientId

        print "MOTD: ", motd
        print "Local ClientID: ", clientId

        # Reply to server with the client name
        self.client.connectionMgr.motdReply(self.client.name, clientId)
