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
        moveData = _data.getString()
        listMoveData = moveData.split('+')
        # Add new cmds (which are actually old?)
        del listMoveData[0]
        self.streamManager.clientManager.clientConnectionLink[_client].moveCmds = listMoveData


    def buildMovementPacket(self, _data=[]):
    	pkt = self.streamManager.buildPacket(2, 0)

        length = len(_data)
        pkt.addUint8(length)
        for d in _data:
            for i in d:
                for coord in d[i]:
                    # Add Client ID
                    pkt.addString(i)

                    pos =  d[i][coord]
                    # Add Pos X
                    pkt.addFloat32(pos.getX())
                    # Add Pos Y
                    pkt.addFloat32(pos.getY())
                    # Add Pos Z
                    pkt.addFloat32(pos.getZ())
        
        return pkt


    def sendMovementUpdate(self, _data=[]):
        pkt = self.buildMovementPacket(_data)
        self.streamManager.server.connectionMgr.broadcastPacket(pkt)

