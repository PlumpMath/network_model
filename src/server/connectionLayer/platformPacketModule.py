#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys

### PANDA Imports ###
from pandac.PandaModules import PointerToConnection, NetAddress, NetDatagram
from panda3d.core import Datagram
from panda3d.core import DatagramIterator
from direct.task.Task import Task

## Server Imports ##
from opcodes import *
from utils.util import generateUUID
from simulationLayer.clientObject import Client

########################################################################
# The Connection Manager should handle reliable stuff with some custom udp /tcp mix,
# but for now it will handle/use basic tcp stuff


class PlatformPacketModule():
    
    def __init__(self, _connectionManager):
    	print "Loaded Platform Packet Module"

    	# ConnectionManager ref
    	self.connectionManager = _connectionManager


        # TCP Listener Task
    def tcpListenerTask(self, task):
        """
        Accept new incoming connection from clients, related to TCP
        """
        # Handle new connection
        if self.connectionManager.tcpListener.newConnectionAvailable():
            rendezvous = PointerToConnection()
            netAddress = NetAddress()
            newConnection = PointerToConnection()

            if self.connectionManager.tcpListener.getNewConnection(rendezvous, netAddress, newConnection):
                newConnection = newConnection.p()
                self.connectionManager.tcpReader.addConnection(newConnection)

                clientId = generateUUID()
                self.connectionManager.streamMgr.clientManager.clients[newConnection] = Client(clientId, \
                                        self.connectionManager.streamMgr.server, newConnection, netAddress)
                print "Server: New Connection from -", str(netAddress.getIpString()), clientId

            else:
                print "Server: Connection Failed from -", str(netAddress.getIpString())

        return Task.cont


    # TCP Reader Task
    def tcpReaderTask(self, task):
        """
        Handle any data from clients by sending it to the Handlers.
        """
        while 1:
            (datagram, data, opcode) = self.tcpNonBlockingRead(self.connectionManager.tcpReader)
            if opcode is MSG_NONE:
                # Do nothing or use it as some 'keep_alive' thing.
                break 
            else:
                # Handle it
                self.connectionManager.streamMgr.unpackPacket(opcode, data, datagram.getConnection())
                
        return Task.cont


    # TCP NonBlockingRead
    def tcpNonBlockingRead(self, qcr):
        """
        Return a datagram collection and type if data is available on
        the queued connection tcpReader
        """
        if self.connectionManager.tcpReader.dataAvailable():
            datagram = NetDatagram()
            if self.connectionManager.tcpReader.getData(datagram):
                data = DatagramIterator(datagram)
                opcode = data.getUint8()
                
            else:
                data = None
                opcode = MSG_NONE
            
        else:
            datagram = None
            data = None
            opcode = MSG_NONE
            
        # Return the datagram to keep a handle on the data
        return (datagram, data, opcode)


    # Handle Disconnects TCP
    def handleDisconnects(self, task):
        """This is just a basic idea, and pretty brutal
        TODO: Maybe get the ip of the connection that did the disconnect along with
        removing any ingame objects belonging to that connection
        """
        # Handle Disconnections
        
        if self.connectionManager.tcpManager.resetConnectionAvailable():
            clients = self.connectionManager.streamMgr.clientManager.clients
            connection = PointerToConnection()
            if self.connectionManager.tcpManager.getResetConnection(connection):
                connection = connection.p()
                for client in clients:
                    if clients[client].connection == connection:
                        self.connectionManager.tcpManager.closeConnection(clients[client].connection)
                        print clients[client].netAddress.getIpString(), "Disconnected"
                        del clients[client] # This will change, should clean out everything first
                        break

        return Task.again


    ## UDP ##

    # UDP Reader Task
    def udpReaderTask(self, task):
        """
        Handle any data from clients by sending it to the Handlers.
        """
        while 1:
            (datagram, data, opcode) = self.udpNonBlockingRead(self.connectionManager.udpReader)
            if opcode is MSG_NONE:
                # Do nothing or use it as some 'keep_alive' thing.
                break 
            else:
                # Handle it
                self.connectionManager.streamMgr.unpackPacket(opcode, data, datagram.getConnection())
                
        return Task.cont


    # UDP NonBlockingRead??
    def udpNonBlockingRead(self, qcr):
        """
        Return a datagram collection and type if data is available on
        the queued connection udpReader
        """
        if self.connectionManager.udpReader.dataAvailable():
            datagram = NetDatagram()
            if self.connectionManager.udpReader.getData(datagram):
                data = DatagramIterator(datagram)
                opcode = data.getUint8()
                
            else:
                data = None
                opcode = MSG_NONE
            
        else:
            datagram = None
            data = None
            opcode = MSG_NONE
            
        # Return the datagram to keep a handle on the data
        return (datagram, data, opcode)


