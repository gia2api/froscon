'''
Created on 24.04.2015

@author: Zeeshan Islam
'''

import pygame
from Character import Character

class Player(Character):

    def __init__(self, sprite_img_path):
        Character.__init__(self, sprite_img_path, 0, 100, 16, 16)
        
        self.speed = 4
        
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
    
    def key_input(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.move_down = True
        else:
            self.move_down = False
            
        if keys[pygame.K_w]:
            self.move_up = True
        else:
            self.move_up = False
        
        if keys[pygame.K_d]:
            self.move_right = True
        else:
            self.move_right = False
        
        if keys[pygame.K_a]:
            self.move_left = True
        else:
            self.move_left = False
        
        if pygame.mouse.get_pressed()[0] == 1:
            print(pygame.mouse.get_pos())
            self.x, self.y = pygame.mouse.get_pos()
            
    def update(self, geg):
        if Character.checkCollision(self, self, geg) == True:
             print("col")
        if self.move_down == True:
            self.y += self.speed
        if self.move_up == True:
            self.y -= self.speed
        if self.move_left == True:
            self.x -= self.speed
        if self.move_right == True:
            self.x += self.speed
    
    def render(self, screen):
        Character.render(self, screen)