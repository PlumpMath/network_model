#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys
import time

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase
from direct.task.Task import Task

## Client Imports ##


########################################################################

class Client(ShowBase):
    
    def __init__(self):
        ShowBase.__init__(self)


    def update(self, task):

        return Task.cont

client = Client()
base.run()