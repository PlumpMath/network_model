from direct.gui.DirectGui import DirectScrolledList
from direct.gui.DirectGui import DirectLabel
from direct.gui.DirectGui import DirectButton

class lobbyGUI():
    def __init__(self):
        self.lstLobby = DirectScrolledList(
            decButton_pos= (1.1, 0, -0.45),
            decButton_text = "up",
            decButton_text_scale = 0.06,
            decButton_borderWidth = (0.005, 0.005),

            incButton_pos= (1.1, 0, -0.55),
            incButton_text = "down",
            incButton_text_scale = 0.06,
            incButton_borderWidth = (0.005, 0.005),

            frameSize = (-1.05, 1.20, -1.16, 0.16),
            frameColor = (1,0,0,0.5),
            pos = (-0.075, 0, 0.5),
            numItemsVisible = 10,
            forceHeight = 0.11,
            itemFrame_frameSize = (-1, 1, -1.11, 0.11),
            itemFrame_pos = (0, 0, 0),
            )

        # create a start button
        self.btnStart = DirectButton(
            # Scale and position
            scale = 0.15,
            pos = (1,0,-0.90),
            # Text
            text = "Start",
            # Frame
            # Functionality
            command = self.start)

        # create a back button
        self.btnBack = DirectButton(
            # Scale and position
            scale = 0.15,
            pos = (-1,0,-0.90),
            # Text
            text = "back",
            # Frame
            # Functionality
            command = self.back)
        self.hide()

    def show(self):
        self.lstLobby.show()
        self.btnStart.show()
        self.btnBack.show()

    def hide(self):
        self.lstLobby.hide()
        self.btnStart.hide()
        self.btnBack.hide()

    def start(self):
        #TODO: Send event or whatever to let the other parts know we can
        #      start the game
        pass

    def back(self):
        #TODO: Send event or whatever to let the other parts know we
        #      want to move to the previous menu
        pass

    def updateList(self, newList):
        for item in newList:
            l = DirectLabel(text = item, text_scale=0.1)
            self.lstLobby.addItem(l)

# TESTING
import direct.directbase.DirectStart
gui = lobbyGUI()
playerList = []
for i in range(20):
    playerList.append("Player-%02d" % (i+1))
gui.updateList(playerList)
gui.show()
base.run()
