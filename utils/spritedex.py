import pygame
import json

class Spritedex(object):

    sheets = {}
    register = {}
    images = {}

    def __init__(self):
        pass

    def load_sheet(self, filename, shortname, override=None):
        try:
            with open(filename) as json_file:
                data = json.load(json_file)
            
            self.register[shortname] = data
            
            if override:
                override.seek(0)
                data['artfile'] = override

            self.sheets[shortname] = pygame.image.load(data['artfile']).convert_alpha()

            # destroy cache

            for tag in list(self.images.keys()):
                if tag.startswith(shortname):
                    del self.images[tag]

            #self.sheet = pygame.image.load(filename)
        except pygame.error as message:
            # FIXME: convert to logging
            print(message)
            print('Unable to load spritesheet image:', filename)
            
    def image(self, short_name, asset_tag, sprite_name):
        # tag_name
        tag_name = "%s.%s.%s" % (short_name,asset_tag, sprite_name)
        if tag_name not in self.images:
            # What if the sheet isnt loaded?
            # now load image
            data = self.register[short_name]['assets'][asset_tag][sprite_name]
            
            rect = pygame.Rect(data['coords'])
            
            ##print(rect)
            image = pygame.Surface(rect.size, pygame.SRCALPHA)
            #print(self.sheets)
            if 'alpha' in data:
                image.set_alpha(data['alpha'])
            image.blit(self.sheets[short_name], (0, 0), rect)
            
            self.images[tag_name] = image
        return self.images[tag_name]