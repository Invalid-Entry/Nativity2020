

class Star():
    
    _spritedex = None
    _position = None

    _animation_position = None

    _progress = None

    def __init__(self, spritedex, position):
        self._spritedex = spritedex
        self._position = position

        self._animation_position = 0
        self._progress = False

        if "star" not in self._spritedex.sheets:
            self._spritedex.load_sheet("assets/star.json", "star")

        

    def render(self, surface):
        
        if self._progress:
            self._animation_position += 1
            if self._animation_position > 15:
                self._animation_position = 0
            
            self._progress = False
        else:
            self._progress = True

        surface.blit(self._spritedex.image("star", "STAR", "%s" % self._animation_position), self._position)
        