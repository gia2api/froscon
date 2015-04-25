'''
Created on 22.04.2015

@author: Zeeshan Islam
'''

from Player import Player
from Character import Character
from Controller import Controller
from Map import Map

class Game(object):

    def __init__(self):
        self.TITLE = "TEST (by zeeisl)"
        self.WIDTH = 800
        self.HEIGHT = 600
        
        self.controller = Controller()
        
        # game things
        self.char = Player("res//hero.png")
        self.map = Map()
        
        self.char1 = Character("res//hero.png", 100, 100, 32, 32)
        
    def key_input(self, event):
        self.controller.getButtonStates(event)
        self.char.key_input(event)
    
    def update(self, delta):
        self.map.update()
        self.char.update(self.char1)
        self.char1.update()
    
    def render(self, screen):
        self.map.render(screen)
        self.char.render(screen)
        self.char1.render(screen)
