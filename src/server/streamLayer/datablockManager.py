#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys

### PANDA Imports ###
from direct.task.Task import Task

## Server Imports ##

########################################################################
# The Datablock manager provides "latest state" delivery of 
# datablocks from the server to the client. Datablocks are objects 
# which contain relatively static data and the manager guarantees 
# delivery only of the latest state at a very low frequency. Like 
# the Ghost manager, the Datablock manager is asymmetric, and 
# datablocks are only transmitted from server to client. The most 
# common use of datablocks is to transmit initialization or 
# reference data for ghosts.

# For now datablocks will be used for the first initialization of game data
# also it would be the first talk between client and server and back to client


class DatablockManager():
    
    def __init__(self, _streamManager):
    	print "Loaded Datablock Manager"

    	# Stream manager ref
    	self.streamManager = _streamManager

    def readStreamPacket(self, _data, _client):
    	pass