#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys
import time

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

## Client Imports ##
from network.connectionManager import ConnectionManager, MovementManager
from network.streamManager import StreamManager
from game import Game
from gui.mainmenu import menuGUI

########################################################################

class Client(ShowBase):
    
    def __init__(self):
        ShowBase.__init__(self)

        #
        self.name = "default"
        self.id = None

        ### NETWORKING ###
        # Connection Layer
        self.connectionMgr = ConnectionManager(self)
        self.connectionMgr.start()

        # Movement Manager
        self.movementMgr = MovementManager(self)

        # Stream Layer
        self.streamMgr = StreamManager(self)

        # Temp Remove after testing!
        self.gui = menuGUI(self)
        self.gui.show()
        #self.connectionMgr.connectToServer('127.0.0.1', 5001)

        # Called when the game actually starts
        self.game = Game(self)


client = Client()
base.run()