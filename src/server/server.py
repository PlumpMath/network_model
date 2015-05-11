#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

## Server Imports ##
from config.config import Config
from streamLayer.streamManager import StreamManager

########################################################################


class Server(ShowBase):
    
    def __init__(self):

        args = str(sys.argv)
        
        if "-window" in args:
            ShowBase.__init__(self)
        else:
            ShowBase(windowType = 'none')

        ## Load Config ##
        self.config = Config()

        # Stream Layer
        self.streamMgr = StreamManager(self)
        
        # Simulation Layer
        #self.gameMgr = GameManager(self)


server = Server()
base.run()