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
from simulationLayer.gameManager import GameManager

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
        self.gameMgr = GameManager(self)


server = Server()
base.run()