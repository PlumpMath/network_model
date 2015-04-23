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
    	client = self.streamManager.client
    	localClient = self.streamManager.client.id +","+ self.streamManager.client.name

    	for idx in _stringDataList:
    		if idx == localClient:#self.streamManager.client.id:
    			client.game.playerControlObject = GhostControlObject(client, idx, True)
    			print "We have a local client!"

    		else:
    			client.game.otherPlayerControlObjects.append(GhostControlObject(client, idx, False))
    			print "We have a remote client!"
