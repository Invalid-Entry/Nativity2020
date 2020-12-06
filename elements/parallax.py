import pygame
from pygame import transform

class Background():

    _asset = None
    _speed = None

    _offset = None
    _width = None

    def __init__(self, image_file, speed):
        self._asset = pygame.image.load(image_file).convert_alpha()
        self._asset = transform.scale(self._asset, (self._asset.get_width()//2, self._asset.get_height()//2))
        
        self._width = self._asset.get_width()

        self._speed = speed
        self._offset = 0
        

    def render(self, surface):
        self._offset -= self._speed
        
        right_edge = self._offset + self._width
        if right_edge <= 0:
            self._offset += self._width
            right_edge = self._offset + self._width

        surface.blit(self._asset, (self._offset, 0))
        surface.blit(self._asset, (right_edge, 0))
        
        
