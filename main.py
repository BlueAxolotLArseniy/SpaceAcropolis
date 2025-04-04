import random
import time
import pygame
import sys as sus

from bullets_box import BulletsBox
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
bullets_box_group = pygame.sprite.Group()

last_spawn_time = 0

last_box_spawn_time = pygame.time.get_ticks()  # Время последнего спавна коробки
box_spawn_delay = 10000  # 10 секунд (в миллисекундах)

running = True
while running:
    
    text1 = f1.render(str(player.bullets_quantity), True,
                  (255, 255, 255))
    
    screen.fill((0, 0, 0))
    
    current_time = time.time()
    if current_time - last_spawn_time >= consts.SPAWN_ASTEROIDS_INTERVAL:
        asteroid_group.add(Asteroid(consts.SCREEN_WIDTH))
        last_spawn_time = current_time

    hits = pygame.sprite.groupcollide(player.bullet_group, asteroid_group, True, True)

    for bullet, asteroids in hits.items():
        for asteroid in asteroids:
            print("Астероид уничтожен!")

            # 20% шанс появления коробки
            if random.random() < 0.2:
                box = BulletsBox(asteroid.rect.centerx, asteroid.rect.centery)
                bullets_box_group.add(box)
                print("КОРОБКА!")

    # Проверяем, касается ли игрок коробки
    collisions = pygame.sprite.spritecollide(player, bullets_box_group, True)  # True удаляет коробку

    for box in collisions:
        player.bullets_quantity += 5  # Добавляем 5 пуль (можно изменить)
        print(f"Боеприпасы пополнены! Теперь у игрока {player.bullets_quantity} пуль.")

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    asteroid_group.update()
    bullets_box_group.update()

    for asteroid in asteroid_group: asteroid.draw(screen)
    for bullet_box in bullets_box_group: bullet_box.draw(screen)
    
    player.update(consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT, screen)
    player.draw(screen)
    
    current_time = pygame.time.get_ticks()
    if current_time - last_box_spawn_time > box_spawn_delay:
        box = BulletsBox(random.randint(0, consts.SCREEN_WIDTH), 10)
        bullets_box_group.add(box)
        last_box_spawn_time = current_time
        print("Новая коробка с патронами появилась!")
    
    if pygame.sprite.spritecollide(player, asteroid_group, False):
        print("Игрок погиб! Столкновение с астероидом.")
        pygame.quit()
        sus.exit()
    
    screen.blit(text1, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)  # Ограничение до 60 FPS
    
pygame.quit()
