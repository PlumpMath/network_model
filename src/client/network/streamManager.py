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
#from moveManager import MoveManager 
#from ghostManager import GhostManager
#from datablockManager import DatablockManager

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
    	#self.moveManager = MoveManager(self)
    	#self.ghostManager = GhostManager(self)
    	#self.datablockManager = DatablockManager(self)


    def handlePacket(self, _opcode, _managerCode, _data):
    	"""Read the packets and pass to the correct sub manager"""

    	if _managerCode == DATABLOCK_MANAGER:
    		self.datablockManager.readStreamPacket(_data, _client)
    	
    	if _managerCode == MOVE_MANAGER:
    		self.moveManager.readStreamPacket(_data, _client)

    	if _managerCode == GHOST_MANAGER:
    		self.ghostManager.readStreamPacket(_data, _client)

        if _managerCode == MOTD:
            self.readMOTD(_data)


    def buildPacket(self, _opcode, _managerCode=None):

    	pkt = Datagram()
    	pkt.addUint8(_opcode)

    	if _managerCode == MOVE_MANAGER:
    		pkt.addUint8(_managerCode)
    		self.ghostManagerData(pkt)

        if _managerCode == MOTD:
            pkt.addUint8(_managerCode) # MOTD code

        return pkt


	def ghostManagerData(self, _packet, _data=[]):
		"""Should add ghost manager data on the packet
		packet:
		opcode int8
		managerCode int8
		data...
		"""
		pkt = _packet
		return pkt


    def readMOTD(self, _data):
        motd = _data.getString()
        clientId = _data.getString()

        print "MOTD: ", motd
        print "ClientID: ", clientId

        # Reply to server with the client name
        self.client.connectionMgr.motdReply(self.client.name, clientId)
