#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys

### PANDA Imports ###
from direct.task.Task import Task

## Client Imports ##
from ghostObject import GhostObject, GhostControlObject

########################################################################



class GhostManager():
    
    def __init__(self, _streamManager):
    	print "Loaded Ghost Manager"

    	# Stream manager ref
    	self.streamManager = _streamManager


    def createGhostObject(self):
    	pass

    def createGhostControlObject(self, _stringDataList):
    	print _stringDataList
    	client = self.streamManager.client

    	if self.streamManager.client.id == None:
    		client.game.playerControlObject = GhostControlObject(client)

    	else:pass
    		#client.game.otherPlayerControlObjects.append(GhostControlObject())



