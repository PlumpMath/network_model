#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys

### PANDA Imports ###
from direct.task.Task import Task
from panda3d.core import Datagram

## Server Imports ##
from managerCodes import *
from moveManager import MoveManager 
from ghostManager import GhostManager
from datablockManager import DatablockManager

########################################################################
# The Stream manager passes the packets to the correct sub managers.
# The stream manager handles the building of packets, data are gathered from 
# sub managers


class StreamManager():
    
    def __init__(self, _server):
    	print "Loaded Stream Manager"

    	# Server ref
    	self.server = _server

    	# init Sub Managers
    	self.moveManager = MoveManager(self)
    	self.ghostManager = GhostManager(self)
    	self.datablockManager = DatablockManager(self)


    def handlePacket(self, _opcode, _managerCode, _data, _client):
    	"""Read the packets and pass to the correct sub manager"""

    	if _managerCode == DATABLOCK_MANAGER:
    		self.datablockManager.readStreamPacket(_data, _client)
    	
    	if _managerCode == MOVE_MANAGER:
    		self.moveManager.readStreamPacket(_data, _client)

    	if _managerCode == GHOST_MANAGER:
    		self.ghostManager.readStreamPacket(_data, _client)

        if _managerCode == MOTD:
            self.server.connectionMgr.sendMOTD(_client)


    def buildPacket(self, _opcode, _managerCode=None):

    	pkt = Datagram()
    	pkt.addUint8(_opcode)

    	if _managerCode == GHOST_MANAGER:
    		pkt.addUint8(_managerCode)
    		self.ghostManagerData(pkt)

        else:
            # For first reply: MOTD
            pkt.addUint8(MOTD)
            pkt.addString(self.server.motd)

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

