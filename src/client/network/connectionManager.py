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
from panda3d.core import Vec3

## Client Imports ##
from platformPacketModule import PlatformPacketModule
from opcodes import MSG_SERVER_PACKET
from config import clTIMEOUT

########################################################################

class ConnectionManager():
    
    def __init__(self, _client):
        print "Connection Manager Loaded"

        # Ref to client
    	self.client = _client
    	self.tcpConnection = None


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
        if _opcode == MSG_SERVER_PACKET:
        	self.client.streamMgr.handlePacket(_opcode, _managerCode, _data)

        else:
            print "Client: BAD-opcode - %d" % _opcode
            print "Client: Opcode Data -", _data
            
        return


    # This should have a send rate limit!
    def sendPackets(self, _data, _connection):
    	pass


    def connectToServer(self, _serverAddress, _serverPort):
    	# This is just for the basics atm

        tcpConn = self.tcpManager.openTCPClientConnection(_serverAddress, _serverPort, clTIMEOUT)

        if tcpConn != None:
            self.tcpConnection = tcpConn
            self.tcpReader.addConnection(tcpConn)
            self.tcpConnection.setNoDelay(True)
    		# Send the first packet

            return True

        return False

    def motdReply(self, _clientName, _clientId):
        pkt = self.client.streamMgr.buildPacket(1, 3)
        pkt.addString(_clientName)
        pkt.addString(_clientId)
        self.tcpWriter.send(pkt, self.tcpConnection)



class MovementManager():

    def __init__(self, _client):

        self.client = _client


    def buildMovementPacket(self, _data=[]):
        pkt = self.client.streamMgr.buildPacket(1, 0)
        moveStr = ''.join(_data)
        pkt.addString(moveStr)

        return pkt

    def sendMovementPacket(self, pkt):
        conn = self.client.connectionMgr.tcpConnection
        self.client.connectionMgr.tcpWriter.send(pkt, conn)


    def readStreamPacket(self, _data):
        updateData = {}

        packetLength = _data.getUint8()

        if packetLength <= 1:
            return

        for x in range(packetLength):
            # Cliend Id
            cID = _data.getString()
            updateData[cID] = {}
            x = _data.getFloat32()
            y = _data.getFloat32()
            z = _data.getFloat32()
            updateData[cID]['pos'] = Vec3(x, y, z)

        self.client.game.serverStates(updateData)

