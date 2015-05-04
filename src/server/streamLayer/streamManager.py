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
from clientManager import ClientManager

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
        self.clientManager = ClientManager(self)


    def handlePacket(self, _opcode, _managerCode, _data, _client):
    	"""Read the packets and pass to the correct sub manager"""

    	if _managerCode == DATABLOCK_MANAGER:
    		self.datablockManager.readStreamPacket(_data, _client)
    	
    	if _managerCode == MOVE_MANAGER:
    		self.moveManager.readStreamPacket(_data, _client)

    	if _managerCode == GHOST_MANAGER:
    		self.ghostManager.readStreamPacket(_data, _client)

        if _managerCode == MOTD:
            self.clientManager.readStreamPacket(_data, _client)


    def buildPacket(self, _opcode, _managerCode=None, _data=[]):

    	pkt = Datagram()
    	pkt.addUint8(_opcode)

        if _managerCode == MOVE_MANAGER:
            pkt.addUint8(_managerCode)

    	if _managerCode == GHOST_MANAGER:
    		pkt.addUint8(_managerCode)
    		self.ghostManager.ghostManagerData(pkt)

        if _managerCode == MOTD:
            pkt.addUint8(_managerCode)
            self.motdData(pkt, _data)

        if _managerCode == DATABLOCK_MANAGER:
            pkt.addUint8(_managerCode)

        return pkt


    def motdData(self, _packet, _data):
        """Forward the server MOTD and the client created ID"""
        pkt = _packet
        pkt.addString(self.server.motd)
        pkt.addString(_data)

        return pkt


