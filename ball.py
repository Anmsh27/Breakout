import random
import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        self.image = pygame.image.load('Breakout_Tile_Set_Free/PNG/58-Breakout-Tiles.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(25,25))
        self.rect = self.image.get_rect(topleft=(x,y))
        directionx = random.choice([1,-1])
        directiony = random.choice([1,-1])
        self.direction = pygame.math.Vector2(directionx,directiony)
        self.speed = 8
        self.broken = False

    def reverse_x(self):
        self.direction.x = -self.direction.x

    def reverse_y(self):
        self.direction.y = -self.direction.y

    def update(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

