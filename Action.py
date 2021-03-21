class MouseAction():
    # Create data Structures
    pos = None
    speed = None
    button = None
    
    # constructor
    def __init__ (self, actionType):
        self.actionType = actionType
    
    # Make setters
    def setPosition(self, x, y):
        self.pos = (x, y)  
    
    def setButton(self, button):
        self.button = button
        
    def setSpeed(self, dx, dy):
        self.speed = (dx, dy)
    
    # Make getters
    def getPosition(self):
        return self.pos
    
    def getButton(self):
        return self.button
    
    def getSpeed(self):
        return speed