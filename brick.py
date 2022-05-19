import pygame
from settings import *


class Brick(pygame.sprite.Sprite):
    def __init__(self,x,y,image,broken_image):
        super().__init__()

        self.image = image
        self.image = pygame.transform.scale(self.image,BRICK_SIZE)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.broken = False
        self.broken_image = broken_image

    def break_brick(self):
        self.broken = True

    def update(self):
        if self.broken:
            self.image = self.broken_image
            self.image = pygame.transform.scale(self.image, BRICK_SIZE)
