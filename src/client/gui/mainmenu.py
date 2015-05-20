#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys


### PANDA Imports ###
from direct.gui.DirectGui import DirectButton
from direct.gui.DirectGui import DirectEntry
from panda3d.core import TextNode

## Client Imports ##
from multiplayer import multiplayerGUI

########################################################################

class menuGUI():
    def __init__(self, _client=None):
        # Ref
        self.client = _client

        # create a singlePlayer button
        self.menubtn0 = DirectButton(
            # Scale and position
            scale = 0.10,
            pos = (0,0,0.5),
            # Text
            text = "Single-Player",
            # Frame
            # Functionality
            command = '')

       	# create a Lan button
        self.menubtn1 = DirectButton(
            # Scale and position
            scale = 0.10,
            pos = (0,0,0.3),
            # Text
            text = "Multi-Player",
            # Frame
            # Functionality
            command = self.handleMultiPlayer)

        # create a Options button
        self.menubtn2 = DirectButton(
            # Scale and position
            scale = 0.10,
            pos = (0,0,0.1),
            # Text
            text = "Options",
            # Frame
            # Functionality
            command = '')

        # create a Exit button
        self.menubtn3 = DirectButton(
            # Scale and position
            scale = 0.10,
            pos = (0,0,-0.1),
            # Text
            text = "Exit",
            # Frame
            # Functionality
            command = self.handleExit)

        self.hide()

    def show(self):
        self.menubtn0.show()
        self.menubtn1.show()
        self.menubtn2.show()
        self.menubtn3.show()

    def hide(self):
        self.menubtn0.hide()
        self.menubtn1.hide()
        self.menubtn2.hide()
        self.menubtn3.hide()


    def handleSinglePlayer(self):
        pass

    def handleMultiPlayer(self):
        # Move to Host / Join-Find games screen
        mGUI = multiplayerGUI(self)
        self.hide()
        mGUI.show()

    def handleOptions(self):
        pass

    def handleExit(self):
        sys.exit()



# TESTING
#import direct.directbase.DirectStart
#gui = menuGUI()
#gui.show()
#base.run()