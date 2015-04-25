'''
Created on 24.04.2015

@author: Zeeshan Islam
'''

import pygame

class Map(object):

    def __init__(self):
        self.BLACK = (0,   0,   0  )
        self.BROWN = (153, 76,  0  )
        self.GREEN = (0,   255, 0  )
        self.BLUE  = (0,   0,   255)
        
        #constants representing the different resources
        self.DIRT  = 0
        self.GRASS = 1
        self.WATER = 2
        self.COAL  = 3
        
        #a dictionary linking resources to colours
        self.colours =   {
                        self.DIRT  : self.BROWN,
                        self.GRASS : self.GREEN,
                        self.WATER : self.BLUE,
                        self.COAL  : self.BLACK
                    }
    
    #a list representing our tilemap
        self.tilemap = [
                [self.GRASS, self.COAL,  self.DIRT ],
                [self.WATER, self.WATER, self.GRASS],
                [self.COAL,  self.GRASS, self.WATER],
                [self.DIRT,  self.GRASS, self.COAL ],
                [self.GRASS, self.WATER, self.DIRT ]
              ]
        
        
    
    def update(self):
        pass
    
    def render(self, screen):
        for row in range(5):
        #loop through each column in the row
            for column in range(3):
                #draw the resource at that position in the tilemap, using the correct colour
                pygame.draw.rect(screen, self.colours[self.tilemap[row][column]], (column*40,row*40,40,40))
        