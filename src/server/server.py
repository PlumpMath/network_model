#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys
import time

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase
from direct.task.Task import Task

## Server Imports ##
from connectionLayer.connectionManager import ConnectionManager
from streamLayer.streamManager import StreamManager
from connectionLayer.config import svrMOTD

########################################################################


class Server(ShowBase):
    
    def __init__(self):

        args = str(sys.argv)
        
        if "-window" in args:
            ShowBase.__init__(self)
        else:
            ShowBase(windowType = 'none')

        # Msg of the day
        self.motd = svrMOTD

        ## Clients ##
        self.clients = {}

        ### Setup the base modules ###
        # Connection Layer
        self.connectionMgr = ConnectionManager(self)
        self.connectionMgr.start()

        # Stream Layer
        self.streamMgr = StreamManager(self)
        
        # Simulation Layer

        # Server tick rate
        self.tickTime = 1.0 / 20
        self.delay = 0
        self.oldTime = 0

        taskMgr.add(self.update, "Server Simulation")


    def update(self, task):
        
        nowTime = int(round(time.time() * 1000))

        self.delay += (nowTime - self.oldTime) / 10000.0 #10000
        self.oldTime = nowTime

        if self.delay > self.tickTime:
            #print "Do Simulation"
            self.delay = 0

            
            #print self.clients
        return Task.cont

server = Server()
base.run()