#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys
import time

### PANDA Imports ###
from direct.task.Task import Task

## Server Imports ##

########################################################################


class GameManager():
    
    def __init__(self, _server):
    	print "Game Manager Loaded"

        self.server = _server

    	# Server tick rate
        self.tickTime = 1.0 / 20
        self.delay = 0
        self.oldTime = 0

        taskMgr.add(self.update, "Server Simulation")


    # Main for Simulation
    def update(self, task):
        nowTime = int(round(time.time() * 1000))

        self.delay += (nowTime - self.oldTime) / 10000.0 #10000
        self.oldTime = nowTime

        if self.delay > self.tickTime:
            #print "Do Simulation"
            self.delay = 0

            
            #print self.clients
        return Task.cont