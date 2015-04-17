#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys
import time

### PANDA Imports ###
from pandac.PandaModules import QueuedConnectionManager
from pandac.PandaModules import QueuedConnectionReader
from pandac.PandaModules import ConnectionWriter
from direct.task.Task import Task

## Client Imports ##
from platformPacketModule import PlatformPacketModule
from opcodes import MSG_CLIENT_PACKET

########################################################################

class ConnectionManager():
    
    def __init__(self, _client):
        print "Connection Manager Loaded"

        # Ref to client
    	self.client = _client


    def start(self):
    	self.pPacketModule = PlatformPacketModule(self)
    	self.setupTcp()
    	self.startTcpTasks()


    def setupTcp(self):
    	"""
    	Setup all tcp related Classes
    	"""
    	self.tcpManager = QueuedConnectionManager()
    	self.tcpReader = QueuedConnectionReader(self.tcpManager, 0)
    	self.tcpWriter = ConnectionWriter(self.tcpManager, 0)


    def startTcpTasks(self):
    	taskMgr.add(self.pPacketModule.tcpReaderTask, "tcpReaderTask", -39)
        print "TCP Reader Started"


        # Handle Datagrams
    def passPacketToStreamMgr(self, _data, _opcode, _managerCode):
        """
        Check for the handle assigned to the opcode.
        """
        if opcode == MSG_CLIENT_PACKET:
        	self.server.streamMgr.handlePacket(_opcode, _managerCode, _data, _client)
        	print _packetSize

        else:
            print "Client: BAD-opcode - %d" % opcode
            print "Client: Opcode Data -", data
            
        return


    def sendPacket(self, _data, _connection):
    	pass