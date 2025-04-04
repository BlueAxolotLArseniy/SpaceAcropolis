import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.image = pygame.image.load('textures/bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 1, self.image.get_height() * 1))  
        self.rect = self.image.get_rect(center=(x, y))
        
        self.speed = 8
    
    def update(self):
        self.rect.centery -= self.speed        
        
        if self.rect.bottom < 0:  # Убираем пулю, если она ушла за экран
            self.kill()
    
    def draw(self, sc):
        sc.blit(self.image, self.rect)
