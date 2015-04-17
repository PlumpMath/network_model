#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys

### PANDA Imports ###
from direct.task.Task import Task

## Server Imports ##
from managerCodes import *
from moveManager import MoveManager 
from ghostManager import GhostManager

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


    def handlePacket(self, _opcode, _managerCode, _data, _client):
    	"""Read the packets and pass to the correct sub manager"""
    	
    	if _managerCode == MOVE_MANAGER:
    		

    	if _managerCode == GHOST_MANAGER:
    		pass
