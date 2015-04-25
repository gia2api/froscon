'''
Created on 22.04.2015

@author: Zeeshan Islam
'''

import pygame

class Character(object):

    def __init__(self, sprite_img_path, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.image.load(sprite_img_path)
        self.sprite.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.sprite_group = pygame.sprite.GroupSingle(self.sprite)
                    
    def update(self):
        pass
    
    def render(self, screen):
        self.sprite.rect.left = self.x
        self.sprite.rect.top = self.y
        self.sprite_group.draw(screen)
        
    def checkCollision(self, char1, char2):
        return pygame.sprite.collide_rect(char1.sprite, char2.sprite)