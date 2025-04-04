import time
import pygame
import sys as sus

from player import Player
from asteroid import Asteroid

import consts

pygame.init()

screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
pygame.display.set_caption("Space Acropolis")

f1 = pygame.font.Font(None, 50)

clock = pygame.time.Clock()

player = Player((consts.SCREEN_WIDTH//2, consts.SCREEN_HEIGHT-100))

asteroid_group = pygame.sprite.Group()

last_spawn_time = 0

running = True
while running:
    
    text1 = f1.render(str(player.bullets_quantity), True,
                  (255, 255, 255))
    
    screen.fill((0, 0, 0))
    
    current_time = time.time()
    if current_time - last_spawn_time >= consts.SPAWN_ASTEROIDS_INTERVAL:
        asteroid_group.add(Asteroid(consts.SCREEN_WIDTH))
        last_spawn_time = current_time

    collisions = pygame.sprite.groupcollide(player.bullet_group, asteroid_group, True, True)

    for bullet, asteroids in collisions.items():
        for asteroid in asteroids:
            print("Уничтожен астероид!")
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    asteroid_group.update()

    for asteroid in asteroid_group: asteroid.draw(screen)
    
    player.update(consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT, screen)
    player.draw(screen)
    
    if pygame.sprite.spritecollide(player, asteroid_group, False):
        print("Игрок погиб! Столкновение с астероидом.")
        pygame.quit()
        sus.exit()
    
    screen.blit(text1, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)  # Ограничение до 60 FPS
    
pygame.quit()
