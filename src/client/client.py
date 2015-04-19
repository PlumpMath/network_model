#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys
import time

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase
from direct.task.Task import Task

## Client Imports ##
from network.connectionManager import ConnectionManager
from network.streamManager import StreamManager

########################################################################

class Client(ShowBase):
    
    def __init__(self):
        ShowBase.__init__(self)

        #
        self.name = "default"

        ### NETWORKING ###
        # Connection Layer
        self.connectionMgr = ConnectionManager(self)
        self.connectionMgr.start()
        self.connectionMgr.connectToServer('127.0.0.1', 5001)

        # Stream Layer
        self.streamMgr = StreamManager(self)


    def update(self, task):

        return Task.cont

client = Client()
base.run()