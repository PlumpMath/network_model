from direct.gui.DirectGui import DirectButton
from direct.gui.DirectGui import DirectEntry
from panda3d.core import TextNode

class connectGUI():
    def __init__(self):
        # create a host button
        self.btnConnect = DirectButton(
            # Scale and position
            scale = 0.25,
            pos = (0,0,0),
            # Text
            text = "Connect",
            # Frame
            # Functionality
            command = self.connect)

        # create the IP input field
        self.txtIP = DirectEntry(
            # scale and position
            pos = (0, 0, -.35),
            scale = 0.25,
            width = 9,
            # Text
            text = "",
            text_align = TextNode.ACenter,
            initialText = "127.0.0.1",
            numLines = 1,
            # Functionality
            command = self.connect,
            focusInCommand = self.clearText)

        self.hide()

    def show(self):
        self.btnConnect.show()
        self.txtIP.show()

    def hide(self):
        self.btnConnect.hide()
        self.txtIP.hide()

    def clearText(self):
        """Function to clear the text that was previously entered in the
        IP input field"""
        self.txtIP.enterText("")
        #TODO: Do something with the ip


    def connect(self, ip=None):
        """Function which will be called by pressing the connect button
        or hit enter while the focus is on the inut field"""
        if ip == None: ip = self.txtIP.get(True)
        if ip == "": return

# TESTING
#import direct.directbase.DirectStart
#gui = connectGUI()
#gui.show()
#base.run()
