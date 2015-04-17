#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase
from direct.task.Task import Task

## Server Imports ##
from connectionLayer.connectionManager import ConnectionManager
from streamLayer.streamManager import StreamManager

########################################################################


class Server(ShowBase):
    
    def __init__(self):

        args = str(sys.argv)
        
        if "-window" in args:
            ShowBase.__init__(self)
        else:
            ShowBase(windowType = 'none')

        ### Setup the base modules ###
        # Connection Layer
        self.connectionMgr = ConnectionManager(self)
        self.connectionMgr.start()

        # Stream Layer
        self.streamMgr = StreamManager(self)
        # Simulation Layer

server = Server()
base.run()