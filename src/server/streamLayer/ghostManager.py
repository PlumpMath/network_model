#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys

### PANDA Imports ###
from direct.task.Task import Task

## Server Imports ##

########################################################################
# The Ghost manager provides two key functions: the "ghosting" of 
# objects from one host to another, and the transferring of state 
# information between the original object and its ghost.  A ghost 
# is a copy of an object persisted and transmitted to a remote 
# host.

# Ghost manager talks to client ghosts. Regarding data from the server
# Control Objects


class GhostManager():
    
    def __init__(self, _streamManager):
    	print "Loaded Ghost Manager"

    	# Stream manager ref
    	self.streamManager = _streamManager

    def readStreamPacket(self, _data, _client):
    	pass