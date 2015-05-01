# Movement handler for the player
from direct.task.Task import Task

# basic panda move codes, record movement keys and then send them to the server

from direct.showbase.InputStateGlobal import inputState

class LocalHandler():
    
    def __init__(self, _game):
        
        self.game = _game
        
        ## MOVEMENT INPUTS ## 
        inputState.watchWithModifiers('forward', 'w')
        inputState.watchWithModifiers('backward', 's')
        inputState.watchWithModifiers('left', 'a')
        inputState.watchWithModifiers('right', 'd')

        self.oldInputCmds = []

        #taskMgr.add(self.doMovement,"updateMovement")
        taskMgr.doMethodLater(0.1, self.catchInput, 'CatchInput')



    def doMovement(self):
    	#dt = globalClock.getDt()
        speed = 200
        player = self.game.playerControlObject

    	if inputState.isSet('forward'):
            player.model.setY(player.model, speed * globalClock.getDt())
            self.oldInputCmds.append("+FORWARD")

        if inputState.isSet('left'):
            player.model.setX(player.model, -speed * globalClock.getDt())
            self.oldInputCmds.append("+LEFT")

        if inputState.isSet('right'):
            player.model.setX(player.model, speed * globalClock.getDt())
            self.oldInputCmds.append("+RIGHT")

        if inputState.isSet('backward'):
            player.model.setY(player.model, -speed * globalClock.getDt())
            self.oldInputCmds.append("+BACKWARD")
    		
    	#return Task.cont

    def catchInput(self, task):
        #print "Send Input Cmds: ", self.oldInputCmds
        self.oldInputCmds = []

        return Task.again


