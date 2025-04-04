import pygame
import random

pygame.init()

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        
        self.original_image = pygame.image.load('textures/asteroid.png').convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (self.original_image.get_width() * 4, self.original_image.get_height() * 4))  # Увеличиваем
        self.rect = self.original_image.get_rect(center=(random.randint(0, screen_width), 10))  # Случайное появление сверху
        
        
        self.speed = 3 # Скорость падения астероида
        self.rotation_angle = 0
        self.rotation_speed = random.randint(-5, 5)  # Случайная скорость вращения (в градусах)
    
    def update(self):
        # Падение астероида
        self.rect.centery += self.speed
        
        # Вращение астероида (увеличиваем угол по мере обновлений)
        self.rotation_angle += self.rotation_speed
        self.image = pygame.transform.rotate(self.original_image, self.rotation_angle)  # Вращаем изображение
        self.rect = self.image.get_rect(center=self.rect.center)  # Перерасчёт позиции rect
        
        
        # Убираем астероид, если он ушел за экран
        if self.rect.top > pygame.display.get_surface().get_height():
            self.kill()  # Удаляем астероид из группы, если он вышел за экран
    
    def draw(self, sc):
        sc.blit(self.image, self.rect)