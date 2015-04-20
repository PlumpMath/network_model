#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys
import time

### PANDA Imports ###
from panda3d.core import Datagram, NetDatagram
from panda3d.core import DatagramIterator
from direct.task.Task import Task

## Client Imports ##
from opcodes import MSG_NONE


########################################################################

class PlatformPacketModule():
    
    def __init__(self, _connectionManager):
        print "Platform Packet Module Loaded"

        # ConnectionManager ref
    	self.connectionManager = _connectionManager


    # TCP Reader Task
    def tcpReaderTask(self, task):
        """
        Handle any data from server by sending it to the Handlers.
        """
        while 1:
            (datagram, data, opcode, managerCode) = self.tcpNonBlockingRead(self.connectionManager.tcpReader)
            if opcode is MSG_NONE:
                # Do nothing or use it as some 'keep_alive' thing.
                break 
            else:
                # Handle it
                self.connectionManager.passPacketToStreamMgr(data, opcode, managerCode)
                
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
                managerCode = data.getUint8()
                
            else:
                data = None
                opcode = MSG_NONE
                managerCode = None
            
        else:
            datagram = None
            data = None
            opcode = MSG_NONE
            managerCode = None
            
        # Return the datagram to keep a handle on the data
        return (datagram, data, opcode, managerCode)