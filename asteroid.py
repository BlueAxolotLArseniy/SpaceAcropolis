import pygame
import random

import consts

pygame.init()

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        
        self.original_image = pygame.image.load(f'textures/asteroid{random.randint(1, 4)}.png').convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (self.original_image.get_width() * 4, self.original_image.get_height() * 4))  # Увеличиваем
        self.rect = self.original_image.get_rect(center=(random.randint(0, screen_width), 10))  # Случайное появление сверху
        
        # self.bullet = bullet
        
        self.rotation_angle = 0
        self.rotation_speed = random.randint(-5, 5)  # Случайная скорость вращения (в градусах)
    
    def update(self):
        self.rect.centery += consts.ASTEROID_FALLING_SPEED
        
        self.rotation_angle += self.rotation_speed
        self.image = pygame.transform.rotate(self.original_image, self.rotation_angle)  # Вращаем изображение
        self.rect = self.image.get_rect(center=self.rect.center)  # Перерасчёт позиции rect
        
        if self.rect.top > pygame.display.get_surface().get_height(): self.kill()
        
        # if self.rect.colliderect(self.bullet.rect): self.kill()
    
    def draw(self, sc): 
        sc.blit(self.image, self.rect)
        pygame.draw.rect(sc, (0, 255, 0), (self.rect.x, self.rect.y, self.rect.width, self.rect.height), 1)