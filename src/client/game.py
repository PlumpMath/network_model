#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys
import time

### PANDA Imports ###
from direct.task.Task import Task

## Client Imports ##
from player.moveHandler import LocalHandler

########################################################################


class Game():
    
    def __init__(self, _client):
        print "Game Module Loaded"
        self.client = _client

    	# client tick rate
        self.tickTime = 1.0 / 20
        self.delay = 0
        self.oldTime = 0
        self.serverTime = 0
        self.pingTime = 0

        # This should only be called when the actual game starts.    
        taskMgr.add(self.update, "Client Simulation", -30)

        self.playerControlObject = None
        self.otherPlayerControlObjects = []
        self.ghostObjects = []

        # Load local handler
        self.localhandler = LocalHandler(self)

    def update(self, task):
        nowTime = int(round(time.time() * 1000))

        self.delay += (nowTime - self.oldTime) / 1000.0 #10000
        self.oldTime = nowTime

        if self.delay > self.tickTime:
            self.delay = 0
            
        return Task.cont

