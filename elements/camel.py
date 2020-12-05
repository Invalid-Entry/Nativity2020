

class Camel():
    
    _spritedex = None
    _position = None

    _animation_position = None
    _king_specifier = None

    def __init__(self, spritedex, position, animation_offset, king_specifer):
        self._spritedex = spritedex
        self._position = position

        self._animation_position = animation_offset
        self._king_specifier = king_specifer

        if "camel" not in self._spritedex.sheets:
            self._spritedex.load_sheet("assets/camel.json", "camel")

        if "kings" not in self._spritedex.sheets:
            self._spritedex.load_sheet("assets/kings.json", "kings")
        

    def render(self, surface):

        self._animation_position += 1
        if self._animation_position > 5:
            self._animation_position = 0

        surface.blit(self._spritedex.image("camel", "CAMEL", "walk_%s" % self._animation_position), self._position)
        
        king_position = (self._position[0]+50, self._position[1]+44)
        surface.blit(self._spritedex.image("kings", self._king_specifier, "walk_%s" % self._animation_position), king_position)