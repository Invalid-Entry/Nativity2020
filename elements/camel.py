

class Camel():
    
    _spritedex = None
    _position = None

    _animation_position = None

    def __init__(self, spritedex, position, animation_offset):
        self._spritedex = spritedex
        self._position = position

        self._animation_position = animation_offset

        if "camel" not in self._spritedex.sheets:
            self._spritedex.load_sheet("assets/camel.json", "camel")
        

    def render(self, surface):

        self._animation_position += 1
        if self._animation_position > 5:
            self._animation_position = 0

        surface.blit(self._spritedex.image("camel", "CAMEL", "walk_%s" % self._animation_position), self._position)
