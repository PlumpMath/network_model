#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys

### PANDA Imports ###
from pandac.PandaModules import QueuedConnectionManager
from pandac.PandaModules import QueuedConnectionReader
from pandac.PandaModules import QueuedConnectionListener
from pandac.PandaModules import ConnectionWriter
#from direct.distributed.PyDatagram import PyDatagram
#from direct.distributed.PyDatagramIterator import PyDatagramIterator

from direct.task.Task import Task

## Server Imports ##
from config import svrHOSTNAME, svrTCPPORT, svrBACKLOG
from platformPacketModule import PlatformPacketModule
from opcodes import MSG_CLIENT_PACKET

########################################################################
# The Connection manager deals with the frequency of packet transmission as well 
# as packet size and stream manager ordering.


class ConnectionManager():
    
    def __init__(self, _server):
    	print "Loaded Connection Manager"

    	# Ref to base
    	self.server = _server

    	self.activeConnections = []


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
    	self.tcpListener = QueuedConnectionListener(self.tcpManager, 0)

    	# TCP Socket
    	self.tcpSocket = self.tcpManager.openTCPServerRendezvous(svrHOSTNAME, svrTCPPORT,
    						svrBACKLOG)
        #self.tcpSocket.setNoDelay(True)
    	self.tcpListener.addConnection(self.tcpSocket)


    def startTcpTasks(self):
    	taskMgr.add(self.pPacketModule.tcpListenerTask, "tcpListenerTask", -40)
        print "TCP Listener Started"
    	taskMgr.add(self.pPacketModule.tcpReaderTask, "tcpReaderTask", -39)
        print "TCP Reader Started"
        taskMgr.add(self.pPacketModule.handleDisconnects, "HandleDisconnects", 50)


        # Handle Datagrams
    def passPacketToStreamMgr(self, _data, _opcode, _managerCode, _client, _packetSize):
        """
        Check for the handle assigned to the opcode.
        """
        if opcode == MSG_CLIENT_PACKET:
        	self.server.streamMgr.handlePacket(_opcode, _managerCode, _data, _client)
        	print _packetSize

        else:
            print "Server: BAD-opcode - %d" % opcode
            print "Server: Opcode Data -", data
            
        return


    def sendPacket(self, _data, _connection):
    	pass