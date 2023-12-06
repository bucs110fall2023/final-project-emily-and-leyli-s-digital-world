import pygame
from pygame.locals import *
import random
#from Duck import Duck

class UBMascot(pygame.sprite.Sprite):
    
    def __init__(self, x, height, images, screen, ub_group, all_sprites):

        pygame.sprite.Sprite.__init__(self)
        
        self.screen = screen
        self.height = height
        self.images = images
        self.ub_group = ub_group
        self.all_sprites = all_sprites

       # self.rect = self.image.get_rect()

        self.x = x
        self.y = (height - 300) + random.randint(0, 5) * 10

        # keep track of whether this duck has been hit or not
        self.is_hit = False

        self.speed = 1

        # yellow ducks with a target are worth 2 points
        # 50% chance that this yellow duck has a target
        self.points = random.choice([1, 2])
        if self.points == 2:
            self.image = self.images['ub_target']
        else:
            self.image = self.images['ub_mascot']
            

    def update(self):
        self.x += self.speed

        # if this duck goes off screen, remove and add a new duck to the group
        if self.x > 1200 - self.image.get_width():
            duck = UBMascot(0 - self.image.get_width(), self.height, self.images, self.screen,self.ub_group, self.all_sprites)
            self.ub_group.add(duck)
            self.all_sprites.add(duck)
            self.kill()
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):

        # draw the duck if it hasn't been hit yet
        if self.is_hit == False:
            self.screen.blit(self.image, (self.x, self.y))

        # draw the stick image
        stick_x = self.x + self.image.get_width() / 2 - self.images['pole'].get_width() / 2
        stick_y = self.y + self.image.get_height()
        self.screen.blit(self.images['pole'], (stick_x, stick_y))