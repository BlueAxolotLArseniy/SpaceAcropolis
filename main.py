import time
import pygame

from player import Player
from asteroid import Asteroid

pygame.init()

WIDTH, HEIGHT = 960, 540
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Базовое окно Pygame")

clock = pygame.time.Clock()

player = Player((WIDTH//2, HEIGHT-100))

asteroid_group = pygame.sprite.Group()

# Таймер для появления новых астероидов
last_spawn_time = 0
spawn_interval = 0.2  # Интервал между появлениями астероидов (в секундах)

running = True
while running:
    screen.fill((0, 0, 0))
    
    current_time = time.time()
    if current_time - last_spawn_time >= spawn_interval:
        asteroid_group.add(Asteroid(WIDTH))  # Добавляем нового астероида
        last_spawn_time = current_time  # Обновляем время последнего появления астероида

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление астероидов
    asteroid_group.update()

    # Рисуем астероиды
    for asteroid in asteroid_group:
        asteroid.draw(screen)
    
    player.update()
    player.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)  # Ограничиваем до 60 FPS
    
pygame.quit()
