class Action():
    # Create data Structures
    pos = None
    speed = None
    button = None
    key = None
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
        
    def setKey(self, key):
        self.key = key
    
    # Make getters
    def getPosition(self):
        return self.pos
    
    def getButton(self):
        return self.button
    
    def getSpeed(self):
        return self.speed

    def getKey(self):
        return self.key