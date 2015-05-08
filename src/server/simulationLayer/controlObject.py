#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys

### PANDA Imports ###
from panda3d.core import Vec3

## Server Imports ##

########################################################################


class ControlObject():
    
    def __init__(self, _clientObject, _id):
    	print "Control Object Created " + _id

    	self.clientObject = _clientObject

    	self.id = _id

    	## Details ##
        self.gotCmdsFromClient = False
    	self.position = Vec3(0, 0, 0)
    	self.direction = (0, 0, 0)
    	self.triggers = []
    	self.lastMoveCmds = []
        self.needsDatablockUpdate = True # First time only then set to False
        self.time = 0

    def doMovement(self, _cmds, _timestep):
        dt = _timestep
        speed = 5

        for cmd in _cmds:
            if cmd == 'FORWARD':
                self.position.setY(self.position.getY()+ 0.1 + speed * dt)

            if cmd == 'LEFT':
                self.position.setX(self.position.getX()- 0.1 - speed * dt)

            if cmd == 'RIGHT':
                self.position.setX(self.position.getX()+ 0.1 + speed * dt)

            if cmd == 'BACKWARD':
                self.position.setY(self.position.getY()- 0.1 - speed * dt)

        #print self.position

