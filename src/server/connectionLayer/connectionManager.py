#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##

### PANDA Imports ###
from pandac.PandaModules import QueuedConnectionManager
from pandac.PandaModules import QueuedConnectionReader
from pandac.PandaModules import QueuedConnectionListener
from pandac.PandaModules import ConnectionWriter

from direct.task.Task import Task

## Server Imports ##
from platformPacketModule import PlatformPacketModule

########################################################################
# The Connection manager deals with the frequency of packet transmission as well 
# as packet size and stream manager ordering.


class ConnectionManager():
    
    def __init__(self, _streamManager):
    	print "Loaded Connection Manager"

    	# Ref to base
    	self.streamMgr = _streamManager
        self.cfg = self.streamMgr.server.config


    def start(self):
    	self.pPacketModule = PlatformPacketModule(self)
    	
        # TCP
        self.setupTcp()
    	self.startTcpTasks()

        # UDP
        self.setupUdp()
        self.startUdpTasks()


    def setupTcp(self):
    	"""
    	Setup all tcp related Classes
    	"""
    	self.tcpManager = QueuedConnectionManager()
    	self.tcpReader = QueuedConnectionReader(self.tcpManager, 0)
    	self.tcpWriter = ConnectionWriter(self.tcpManager, 0)
    	self.tcpListener = QueuedConnectionListener(self.tcpManager, 0)

    	# TCP Socket
    	self.tcpSocket = self.tcpManager.openTCPServerRendezvous(self.cfg.HOSTNAME, self.cfg.TCPPORT,
    						self.cfg.BACKLOG)
        #self.tcpSocket.setNoDelay(True)
    	self.tcpListener.addConnection(self.tcpSocket)


    def setupUdp(self):
        # All udp 
        self.udpManager = QueuedConnectionManager()
        self.udpReader = QueuedConnectionReader(self.udpManager, 0)
        self.udpWriter = ConnectionWriter(self.udpManager, 0)
        self.udpSocket = self.udpManager.openUDPConnection(self.cfg.UDPPORT)


    def startTcpTasks(self):
    	taskMgr.add(self.pPacketModule.tcpListenerTask, "tcpListenerTask", 50)
        print "TCP Listener Started"
    	taskMgr.add(self.pPacketModule.tcpReaderTask, "tcpReaderTask", -40)
        print "TCP Reader Started"
        taskMgr.add(self.pPacketModule.handleDisconnects, "HandleDisconnects", 60)

    def startUdpTasks(self):
        taskMgr.add(self.pPacketModule.udpReaderTask, "udpReaderTask", -39)
        print "UDP Reader Started"


    # Single send
    def sendPacket(self, _packet, _connection):
    	self.tcpWriter.send(_packet, _connection)

    # Every client send
    def broadcastPacket(self, _packet):
        for client in self.server.streamMgr.clientManager.clients:
            conn = self.server.streamMgr.clientManager.clients[client].connection
            self.sendPacket(_packet, conn)

    # All except
    def sendPacketToAllExcept(self, _packet, _except):

        for client in self.server.streamMgr.clientManager.clients:
            if client != _except:
                conn = self.server.streamMgr.clientManager.clients[client].connection
                sendPacket(_packet, conn)

