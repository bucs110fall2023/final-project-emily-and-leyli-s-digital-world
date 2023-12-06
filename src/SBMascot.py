import pygame
from pygame.locals import *
import random

class SBMascot(pygame.sprite.Sprite):
    
    def __init__(self, x, height, images, screen, stony_group, all_sprites, remaining_papers, power_sprites):

        pygame.sprite.Sprite.__init__(self)
        
        self.screen = screen
        self.height = height
        self.images = images
        self.stony_group = stony_group
        self.all_sprites = all_sprites
        self.remaining_papers = remaining_papers
        self.power_sprites = power_sprites

       # self.rect = self.image.get_rect()

        self.x = x
        self.y = (height - 300) + random.randint(0, 5) * 10

        # keep track of whether this mascot has been hit or not
        self.is_hit = False

        self.speed = 2

        # brown mascots with a target are worth 2 points
        # 50% chance that this brown mascot has a target
        self.points = random.choice([2, 2, 2, 4])
        x =random.choice([0,1,2])
        if self.points == 4:
            self.image = self.images['stony_target']
        else:
            if(x == 1):
                self.image = self.images['stony_powerup']
                self.power_sprites.add(self)

            else:
                self.image = self.images['stony_mascot']
            

    def update(self):
        self.x -= self.speed

        # if this mascot goes off screen, remove and add a new mascot to the group
        if self.x < 0 - self.image.get_width():
            mascot = SBMascot(1200 - self.image.get_width(), self.height, self.images, self.screen,self.stony_group, self.all_sprites, self.remaining_papers, self.power_sprites)
            self.stony_group.add(mascot)
            self.all_sprites.add(mascot)
            self.kill()
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):

        # draw the mascot if it hasn't been hit yet
        if self.is_hit == False:
            self.screen.blit(self.image, (self.x, self.y))

        # draw the stick image
        stick_x = self.x + self.image.get_width() / 2 - self.images['pole'].get_width() / 2
        stick_y = self.y + self.image.get_height()
        self.screen.blit(self.images['pole'], (stick_x, stick_y))