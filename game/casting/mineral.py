from game.casting.actor import Actor


class mineral(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of a mineral is to provied a point to the player associated with the mineral. 

    Attributes:
        _message (string): A short description about the artifact.
    """
    x = int(MAX_X = 6)
    y = int(MAX_Y = 900)
    position = Point(x, y)

    def __init__(self):
        super().__init__()
        self._message = ""
        
    def getPoints(self):
        """Gets the points from the mineral for the player. 
        
        Returns:
            points for the player that is .
        """
        return self.getPoints
    
   