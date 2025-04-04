import time
import pygame

from player import Player
from asteroid import Asteroid

import consts

pygame.init()

screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
pygame.display.set_caption("Базовое окно Pygame")

clock = pygame.time.Clock()

player = Player((consts.SCREEN_WIDTH//2, consts.SCREEN_HEIGHT-100))

asteroid_group = pygame.sprite.Group()

# Таймер для появления новых астероидов
last_spawn_time = 0

running = True
while running:
    screen.fill((0, 0, 0))
    
    current_time = time.time()
    if current_time - last_spawn_time >= consts.SPAWN_ASTEROIDS_INTERVAL:
        asteroid_group.add(Asteroid(consts.SCREEN_WIDTH))  # Добавляем нового астероида
        last_spawn_time = current_time  # Обновляем время последнего появления астероида

    collisions = pygame.sprite.groupcollide(player.bullet_group, asteroid_group, True, True)

    for bullet, asteroids in collisions.items():
        for asteroid in asteroids:
            print("💥 Уничтожен астероид!")
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    # Обновление астероидов
    asteroid_group.update()

    # Рисуем астероиды
    for asteroid in asteroid_group: asteroid.draw(screen)
    
    player.update(consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT, screen)
    player.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)  # Ограничиваем до 60 FPS
    
pygame.quit()
