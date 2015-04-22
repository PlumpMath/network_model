#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys

### PANDA Imports ###

## Server Imports ##

########################################################################


class ControlObject():
    
    def __init__(self, _clientObject, _id):
    	print "Control Object Created"

    	self.clientObject = _clientObject

    	self.id = _id

    	## Details ##
    	self.position = (0, 0, 0)
    	self.direction = (0, 0, 0)
    	self.triggers = []
    	self.lastMoveCmds = []
        self.needsDatablockUpdate = True # First time only then set to False