import pygame
from bullet import Bullet
import consts

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, center: tuple):
        super().__init__()
        
        self.image = pygame.image.load('textures/player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.rect = self.image.get_rect(center=center)
        
        self.speed_x = 0
        self.speed_y = 0
        
        self.bullet_group = pygame.sprite.Group()
        self.last_shot_time = 0  # Время последнего выстрела
        self.bullets_quantity = 10
    
    def update(self):
        keys = pygame.key.get_pressed()
        
        # Горизонтальное движение
        if keys[pygame.K_a] and 0 < self.rect.topleft[0]: self.speed_x -= consts.PLAYER_ACCELERATION
        if keys[pygame.K_d] and self.rect.topright[0] < consts.SCREEN_WIDTH: self.speed_x += consts.PLAYER_ACCELERATION

        # Вертикальное движение
        if keys[pygame.K_w] and 0 < self.rect.topleft[1]: self.speed_y -= consts.PLAYER_ACCELERATION
        if keys[pygame.K_s] and self.rect.bottomleft[1] < consts.SCREEN_HEIGHT: self.speed_y += consts.PLAYER_ACCELERATION

        current_time = pygame.time.get_ticks()
        if keys[pygame.K_SPACE] and current_time - self.last_shot_time > consts.DELAYED_FIRING and self.bullets_quantity > 0:
            self.last_shot_time = current_time
            bullet = Bullet(self.rect.centerx, self.rect.top)
            self.bullet_group.add(bullet)
            self.bullets_quantity -= 1
        
        self.bullet_group.update()
            
        if self.rect.topleft[0] < 0: self.rect.centerx += 0 - self.rect.topleft[0]
        if self.rect.topright[0] > consts.SCREEN_WIDTH: self.rect.centerx -= self.rect.topright[0] - consts.SCREEN_WIDTH
            
        if self.rect.topleft[1] < 0: self.rect.centery += 0 - self.rect.topleft[1]
        if self.rect.bottomleft[1] > consts.SCREEN_HEIGHT: self.rect.centery -= self.rect.bottomleft[1] - consts.SCREEN_HEIGHT
        
        # Применение трения
        self.speed_x *= consts.PLAYER_FRICTION
        self.speed_y *= consts.PLAYER_FRICTION
        
        # Остановка при малой скорости
        if abs(self.speed_x) < 0.1: self.speed_x = 0
        if abs(self.speed_y) < 0.1: self.speed_y = 0
        
        self.rect.centerx += self.speed_x
        self.rect.centery += self.speed_y
    
    def draw(self, sc):
        sc.blit(self.image, self.rect)
        for bullet in self.bullet_group: bullet.draw(sc)
        pygame.draw.rect(sc, (255, 255, 255), (self.rect.x, self.rect.y, self.rect.width, self.rect.height), 1)