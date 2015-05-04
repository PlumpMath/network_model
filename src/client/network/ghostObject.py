#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys

### PANDA Imports ###

## Server Imports ##

########################################################################


class GhostObject():
    
    def __init__(self, _ref, _id):
    	print "Ghost Object Created"

    	self.ref = _ref

    	self.id = _id

    	## Details ##
    	self.position = (0, 0, 0)
    	self.direction = (0, 0, 0)
    	self.triggers = []
    	self.lastMoveCmds = []
        self.needsDatablockUpdate = True # First time only then set to False


# This will be used for players
class GhostControlObject():

    def __init__(self,_ref, _id, _local=False):
        # This will be used for player/s

        self.ref = _ref

        # Split the id and name
        tempIdName = _id.split(',')

        print "Ghost Control Object Created " + tempIdName[0] + " With name: " + tempIdName[1]

        
        self.id = tempIdName[0]
        self.isLocal = _local
        self.name = None

        # Details
        self.position = (0, 0, 0)
        self.direction = (0, 0, 0)
        self.triggers = []
        self.lastMoveCmds = []
        self.needsDatablockUpdate = True

        if self.isLocal:
            self.name = self.ref.name
        else:
            self.name = tempIdName[1]


        self.model = None
        self.loadModel()


    def loadModel(self, _model='player'):

        model = loader.loadModel('assets/'+_model)
        model.reparentTo(render)
        self.model = model

    def doMovement(self, _cmds, _timestep):
        dt = _timestep
        speed = 5

        for cmd in _cmds:
            if cmd == 'FORWARD':
                self.position.setY(self.position.getY() + speed * dt)

            if cmd == 'LEFT':
                self.position.setX(self.position.getX() - speed * dt)

            if cmd == 'RIGHT':
                self.position.setX(self.position.getX() + speed * dt)

            if cmd == 'BACKWARD':
                self.position.setY(self.position.getY() - speed * dt)


        