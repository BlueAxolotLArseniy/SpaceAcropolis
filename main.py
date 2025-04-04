import random
import time
import pygame
import sys as sus

from game import Game

from bullets_box import BulletsBox
from player import Player
from asteroid import Asteroid

import consts

pygame.init()

screen = pygame.display.set_mode((consts.SCREEN_WIDTH, 
                                  consts.SCREEN_HEIGHT))
pygame.display.set_caption("Space Acropolis")

f1 = pygame.font.Font(None, 50)

clock = pygame.time.Clock()

player = Player((consts.SCREEN_WIDTH//2, 
                 consts.SCREEN_HEIGHT-100))

asteroid_group = pygame.sprite.Group()
bullets_box_group = pygame.sprite.Group()

last_spawn_time = 0

last_box_spawn_time = pygame.time.get_ticks()  # Время последнего спавна коробки
box_spawn_delay = 10000  # 10 секунд (в миллисекундах)

game = Game(screen, 
            f1, 
            player, 
            asteroid_group, 
            bullets_box_group, 
            box_spawn_delay, 
            last_spawn_time, 
            last_box_spawn_time)

running = True
while running:

    game.update()
    
    game.draw()
    
    pygame.display.flip()
    clock.tick(60)  # Ограничение до 60 FPS
    
pygame.quit()
