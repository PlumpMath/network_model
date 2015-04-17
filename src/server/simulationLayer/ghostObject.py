#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys

### PANDA Imports ###

## Server Imports ##

########################################################################


class GhostObject():
    
    def __init__(self, _ref, _id, _connection):
    	print "Ghost Object Created"

    	self.ref = _ref

    	self.id = _id

    	## Details ##
    	self.position = (0, 0, 0)
    	self.direction = (0, 0, 0)
    	self.triggers = []
    	self.lastMoveCmds = []
        self.needsDatablockUpdate = True # First time only then set to False