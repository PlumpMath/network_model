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

        self.delay += (nowTime - self.oldTime) / 1000.0 #10000
        self.oldTime = nowTime

        if self.delay > self.tickTime:
            dt = globalClock.getDt()
            #print "Do Simulation"
            # Should read input from queue
            # Process
            self.processControlObjects(dt)
            # Pack and send updates
            self.broadcastControlObjStates()
            self.delay = 0

            
            #print self.clients
        return Task.cont


    # Basically players.
    def processControlObjects(self, _timestep):
        
        for client in self.server.clients:
            # Update the movement
            self.server.clients[client].handleMovement(_timestep)

    def broadcastControlObjStates(self):
        states = self.getClientControlObjStates()
        self.server.streamMgr.moveManager.sendMovementUpdate(states)


    def serverStateSnapshot(self):
        pass


    def getClientControlObjStates(self):

        states = []

        for client in self.server.clients:
            s = self.server.clients[client].getState()
            states.append(s)

        return states