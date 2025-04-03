import pygame
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, center: tuple):
        super().__init__()
        
        self.image = pygame.image.load('player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.rect = self.image.get_rect(center=center)
        
        self.speed_x = 0
        self.speed_y = 0
        self.acceleration = 5  # Ускорение
        self.friction = 0.7  # Трение (потеря скорости за тик)
    
    def update(self):
        keys = pygame.key.get_pressed()
        
        # Горизонтальное движение
        if keys[pygame.K_a]:
            self.speed_x -= self.acceleration
        if keys[pygame.K_d]:
            self.speed_x += self.acceleration

        # Вертикальное движение
        if keys[pygame.K_w]:
            self.speed_y -= self.acceleration
        if keys[pygame.K_s]:
            self.speed_y += self.acceleration
        
        # Применение трения для плавного замедления
        self.speed_x *= self.friction
        self.speed_y *= self.friction
        
        # Добавление гравитации (для замедления вверх)
        
        # Остановка при малой скорости
        if abs(self.speed_x) < 0.1:
            self.speed_x = 0
        if abs(self.speed_y) < 0.1:
            self.speed_y = 0
        
        # Обновляем позицию
        self.rect.centerx += self.speed_x
        self.rect.centery += self.speed_y
    
    def draw(self, sc):
        sc.blit(self.image, self.rect)
