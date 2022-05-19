import pygame
from sys import exit
from settings import *
from player import Player
from brick import Brick
from support import import_folder
from random import *
from ball import Ball
pygame.init()

class Game():
    def __init__(self):

        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption("Breakout")
        icon = pygame.image.load('breakout-room.ico').convert_alpha()
        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()

        self.player = pygame.sprite.GroupSingle(Player(0, 0))
        self.player.sprite.rect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT - SCREEN_HEIGHT/15)

        self.broken_bricks = import_folder('Breakout_Tile_Set_Free/PNG/bricks_broken/')
        self.unbroken_bricks = import_folder('Breakout_Tile_Set_Free/PNG/bricks_unbroken/')

        self.bricks = pygame.sprite.Group()
        self.make_bricks()

        self.ball = pygame.sprite.GroupSingle(Ball(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))

        self.gui_is_active = True

    def make_bricks(self):
        for i in range(int(SCREEN_WIDTH/BRICK_SIZE[0])):
            for x in range(7):
                x_coord = i * BRICK_SIZE[0]
                y = x * BRICK_SIZE[1]
                index = randint(0,len(self.unbroken_bricks)-1)
                self.bricks.add(Brick(x_coord,y,self.unbroken_bricks[index], self.broken_bricks[index]))

    def check_collisions(self):
        ball = self.ball.sprite
        player = self.player.sprite
        bricks = self.bricks.sprites()
        if ball.rect.colliderect(player.rect):
            if ball.rect.bottom >= player.rect.top:
                ball.reverse_y()
        if ball.rect.right >= SCREEN_WIDTH:
            ball.reverse_x()
        if ball.rect.left <= 0:
            ball.reverse_x()
        for brick in bricks:
            if ball.rect.colliderect(brick.rect):
                if not brick.broken:
                    brick.break_brick()
                else:
                    self.bricks.remove(brick)
                if ball.rect.top <= brick.rect.bottom:
                    ball.reverse_y()
                elif ball.rect.bottom >= brick.rect.top:
                    ball.reverse_y()
                elif ball.rect.right >= brick.rect.left:
                    ball.reverse_x()
                elif ball.rect.left <= brick.rect.right:
                    ball.reverse_x()

    def gui(self):
        surf = pygame.font.Font(None,200).render("Breakout", True, 'white')
        rect = surf.get_rect(topleft=(0,0))
        rect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/3)
        self.screen.blit(surf, rect)

        surf2 = pygame.font.Font(None,150).render("Play", True, 'black')
        rect2 = surf2.get_rect(topleft=(0,0))
        play_butt = pygame.Surface((300,175))
        play_butt.fill('white')
        butt_rect = play_butt.get_rect(topleft=(0,0))
        butt_rect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 100)
        self.screen.blit(play_butt,butt_rect)
        rect2.center = butt_rect.center
        self.screen.blit(surf2,rect2)

        mouse_pressed = pygame.mouse.get_pressed()
        mousex,mousey = pygame.mouse.get_pos()

        if (butt_rect.collidepoint(mousex,mousey) and mouse_pressed[0]) or pygame.key.get_pressed()[pygame.K_SPACE]:
            self.gui_is_active = False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

            self.screen.fill('black')

            if self.gui_is_active:
                self.gui()

            if not self.gui_is_active:

                self.player.draw(self.screen)
                self.player.update()

                self.bricks.draw(self.screen)
                self.bricks.update()

                self.ball.draw(self.screen)
                self.ball.update()

                self.check_collisions()

            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()

