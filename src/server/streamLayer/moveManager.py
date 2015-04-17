#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys

### PANDA Imports ###
from direct.task.Task import Task

## Server Imports ##

########################################################################
# The Move manager guarantees "soonest possible" delivery of client 
# input moves to the server and "soonest possible" delivery of 
# control object state data.
# x, y and z translations, yaw, pitch and roll 
# rotations as well as an array of trigger states.


class MoveManager():
    
    def __init__(self, _streamManager):
    	print "Loaded Move Manager"

    	# Stream manager ref
    	self.streamManager = _streamManager

    def readStreamPacket(self, _data, _client):
    	pass