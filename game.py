import random
import time

import pygame

import sys as sus

from bullets_box import BulletsBox
pygame.init()

from asteroid import Asteroid
import consts


class Game:
    def __init__(self, screen, f1, player, asteroid_group, bullets_box_group, box_spawn_delay, last_spawn_time, last_box_spawn_time):
        self.screen = screen
        self.f1 = f1
        self.player = player
        self.asteroid_group = asteroid_group
        self.bullets_box_group = bullets_box_group
        self.box_spawn_delay = box_spawn_delay
        self.last_spawn_time = last_spawn_time
        self.last_box_spawn_time = last_box_spawn_time
    
    def update(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
        
        self.text1 = self.f1.render(str(self.player.bullets_quantity), True,
                  (255, 255, 255))
        
        
        current_time = time.time()
        if current_time - self.last_spawn_time >= consts.SPAWN_ASTEROIDS_INTERVAL:
            self.asteroid_group.add(Asteroid(consts.SCREEN_WIDTH))
            self.last_spawn_time = current_time
        
        
        hits = pygame.sprite.groupcollide(self.player.bullet_group, self.asteroid_group, True, True)

        for bullet, asteroids in hits.items():
            for asteroid in asteroids:
                print("Астероид уничтожен!")

                # 20% шанс появления коробки
                if random.random() < 0.2:
                    box = BulletsBox(asteroid.rect.centerx, asteroid.rect.centery)
                    self.bullets_box_group.add(box)
                    print("КОРОБКА!")

        
        # Проверяем, касается ли игрок коробки
        collisions = pygame.sprite.spritecollide(self.player, self.bullets_box_group, True)  # True удаляет коробку

        for box in collisions:
            self.player.bullets_quantity += 5  # Добавляем 5 пуль (можно изменить)
            print(f"Боеприпасы пополнены! Теперь у игрока {self.player.bullets_quantity} пуль.")


        self.asteroid_group.update()
        self.bullets_box_group.update()
        
        
        self.player.update()
        
        
        current_time = pygame.time.get_ticks()
        if current_time - self.last_box_spawn_time > self.box_spawn_delay:
            box = BulletsBox(random.randint(0, consts.SCREEN_WIDTH), 10)
            self.bullets_box_group.add(box)
            self.last_box_spawn_time = current_time
            print("Новая коробка с патронами появилась!")
        
        if pygame.sprite.spritecollide(self.player, self.asteroid_group, False):
            print("Игрок погиб! Столкновение с астероидом.")
            pygame.quit()
            sus.exit()
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        
        for asteroid in self.asteroid_group: asteroid.draw(self.screen)
        for bullet_box in self.bullets_box_group: bullet_box.draw(self.screen)
        
        self.player.draw(self.screen)
        
        self.screen.blit(self.text1, (10, 10))