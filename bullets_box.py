import pygame
import random

import consts

pygame.init()

class BulletsBox(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.original_image = pygame.image.load('textures/bullets_box.png').convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (self.original_image.get_width() * 2, self.original_image.get_height() * 2))
        self.rect = self.original_image.get_rect(center=(x, y))
    
    def update(self):
        self.rect.centery += consts.ASTEROID_FALLING_SPEED
        
        if self.rect.top > pygame.display.get_surface().get_height(): self.kill()

    def draw(self, sc): 
        sc.blit(self.original_image, self.rect)