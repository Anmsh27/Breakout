import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        self.image = pygame.Surface((200,15))
        self.image.fill('white')
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 12 

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def update(self):
        self.rect.x += self.direction.x * self.speed
        self.get_input()

        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        elif self.rect.left <= 0:
            self.rect.left = 0
