import pygame
from pygame import transform, Surface
from pygame.draw import line, rect
import random

class SnowConfig():
    number_of_flakes = None
    flake_size = None
    flake_color = None

    def __init__(self, number_of_flakes, flake_size, flake_color):
        self.number_of_flakes = number_of_flakes
        self.flake_size = flake_size
        self.flake_color = flake_color


class Background():

    _asset = None
    _speed = None

    _offset = None
    _width = None

    _snow_config = None
    _snow_baseline = None
    _snow_height = None

    _flakes = None

    sub_surf = None

    def __init__(self, image_file, speed, snowconfig=None):
        self._asset = pygame.image.load(image_file).convert_alpha()
        self._asset = transform.scale(self._asset, (self._asset.get_width()//2, self._asset.get_height()//2))
        
        self._width = self._asset.get_width()

        self._speed = speed
        self._offset = 0

        if snowconfig:
            self._snow_config = snowconfig
            self._snow_baseline = []
            self._snow_height = []
            self._flakes = []
            
            for i in range(self._width):
                height = 0
                color = self._asset.get_at((i,0))[3]
                j = 0
                found = False
                while j < self._asset.get_height() and found==False:
                    
                    sample = self._asset.get_at((i,j))[3]
                    if sample != color:
                        found = True
                    else:
                        j+=1

                if found:
                    self._snow_baseline.append(j)
                    self._snow_height.append(j)

            for i in range(snowconfig.number_of_flakes):
                x = random.randint(0,self._width-1)
                y = random.randint(0,self._snow_height[x])

                self._flakes.append([x,y])

        self.sub_surf = Surface(self._asset.get_size(), pygame.SRCALPHA)


    def render(self, surface, wind):
        self._offset -= self._speed
        
        self.sub_surf.fill((0,0,0,0))
        
        self.sub_surf.blit(self._asset, (0,0))

        choices = (-4, -3, -2, -2, -1, -1, -1, 0,0,0,0, 1, 1, 1, 2 ,2 , 3, 4)

        if self._snow_config:
            

            for flake in self._flakes:
                flake[0] += (random.choice(choices) + wind)
                if flake[0] >= self._width:
                    flake[0] -= self._width

                if flake[0] < 0:
                    flake[0] += self._width

                flake[1] += random.choice((0,0,1,1,1,2))

                if flake[1] > self._snow_height[flake[0]]:
                    flake[1] = 0
                    self._snow_height[flake[0]] -= 1

                rect(self.sub_surf, self._snow_config.flake_color, (flake[0], flake[1], self._snow_config.flake_size, self._snow_config.flake_size))

            for i in range(self._width):
                if self._snow_height[i] < self._snow_baseline[i]:

                    if i == 0:
                        if self._snow_height[i] < self._snow_height[self._width-1]-2:
                            self._snow_height[i] += 1
                            self._snow_height[i-1] -= 1
                    else:
                        if self._snow_height[i] < self._snow_height[i-1]-2:
                            self._snow_height[i] += 1
                            self._snow_height[i-1] -= 1
                    if i == self._width -1:
                        if self._snow_height[i] < self._snow_height[0]-2:
                            self._snow_height[i] += 1
                            self._snow_height[i-1] -= 1
                    else:
                        if self._snow_height[i] < self._snow_height[i+1]-2:
                            self._snow_height[i] += 1
                            self._snow_height[i-1] -= 1

                
                   

            for snow_position in range(self._width):
                line(self.sub_surf, self._snow_config.flake_color, (snow_position, self._snow_height[snow_position]), (snow_position, self._snow_baseline[snow_position]))

        right_edge = self._offset + self._width
        if right_edge <= 0:
            self._offset += self._width
            right_edge = self._offset + self._width

        surface.blit(self.sub_surf, (self._offset, 0))
        surface.blit(self.sub_surf, (right_edge, 0))
        
        
