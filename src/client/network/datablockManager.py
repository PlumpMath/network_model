#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys

### PANDA Imports ###
from direct.task.Task import Task

## Client Imports ##

########################################################################


class DatablockManager():
    
    def __init__(self, _streamManager):
    	print "Loaded Datablock Manager"

    	# Stream manager ref
    	self.streamManager = _streamManager

    def readStreamPacket(self, _data):
    	stringDataList = []

    	datablockLength = _data.getUint8()
    	for x in range(datablockLength):
    		stringData = _data.getString()
    		stringDataList.append(stringData)
            
        # Create objects depending on information
        self.streamManager.ghostManager.createGhostControlObject(stringDataList)