#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys

### PANDA Imports ###

## Server Imports ##

########################################################################


class ControlObject():
    
    def __init__(self, _ref, _id, _connection):
    	print "Control Object Created"

    	self.ref = _ref

    	self.id = _id
    	self.connection = _connection

    	## Details ##
    	self.position = (0, 0, 0)
    	self.direction = (0, 0, 0)
    	self.trigger = []
    	self.lastMoveCmds = []