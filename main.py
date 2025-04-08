import random
import time
import pygame
pygame.init()


from game import Game

from menu import MainMenu
from player import Player

import consts


screen = pygame.display.set_mode((consts.SCREEN_WIDTH, 
                                  consts.SCREEN_HEIGHT))
pygame.display.set_caption("Space Acropolis")

f1 = pygame.font.Font(None, 50)

clock = pygame.time.Clock()

player = Player((consts.SCREEN_WIDTH//2, 
                 consts.SCREEN_HEIGHT-100))

menu = MainMenu()

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
            last_box_spawn_time,
            menu)

running = True
while running:
    
    game.update(clock)
    game.draw()
    
    pygame.display.flip()
    clock.tick(60)  # Ограничение до 60 FPS
    
pygame.quit()
