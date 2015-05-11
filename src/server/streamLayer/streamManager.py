#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##

### PANDA Imports ###
from direct.task.Task import Task
from panda3d.core import Datagram

## Server Imports ##
from connectionLayer.connectionManager import ConnectionManager
from connectionLayer.opcodes import *
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

        # Connection Manager
        self.connectionMgr = ConnectionManager(self)
        self.connectionMgr.start()

    	# init Sub Managers
        self.clientManager = ClientManager(self)
    	self.moveManager = MoveManager(self)
    	self.ghostManager = GhostManager(self)
    	self.datablockManager = DatablockManager(self)

        # Setup opcodes and handlers
        self.unpackOpcodes = {
            MSG_SERVER_MOVE_CMD : self.moveManager.readStreamPacket
        }


    def unpackPacket(self, _opcode, _data, _client):
    	"""Read the packets and pass to the correct sub manager"""

    	self.unpackOpcodes[_opcode](_data, _client)




