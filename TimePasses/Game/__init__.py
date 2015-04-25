'''
Created on 22.04.2015

@author: Zeeshan Islam
'''

import os, sys, random
import pygame
from pygame.locals import *
from Game import Game

game = Game()
pygame.init()
pygame.display.set_caption(game.TITLE)
screen = pygame.display.set_mode((game.WIDTH, game.HEIGHT))
finish = False

def key_input(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        finish = True
    else:
        game.key_input(event)
    
    
def update():
    game.update(0)
    
def render(screen):
    game.render(screen)

clock = pygame.time.Clock()
while finish != True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        else:
            key_input(event)
    update()
    screen.fill((0, 0, 0))
    render(screen)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
