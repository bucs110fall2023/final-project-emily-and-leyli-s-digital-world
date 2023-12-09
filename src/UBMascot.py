import pygame
from pygame.locals import *
import random

class UBMascot(pygame.sprite.Sprite):
    
    def __init__(self, x, height, images, screen, ub_group, all_sprites):
        '''
        general function description:
		This function initializes the UB mascot object

		arg: (type) description
        self: instance of class
        x: The x-coordinate position for the UB mascot 
        height: The height of the screen
        images: A doctionary holding the imaages of the UB mascots
        screen: the game screen
        ub_group: sprite group containing the UB mascots
        all_sprites: sprite group containing all sprites in game

		return: (type) description
        Does not return anything
	    '''
        pygame.sprite.Sprite.__init__(self)
        
        self.screen = screen
        self.height = height
        self.images = images
        self.ub_group = ub_group
        self.all_sprites = all_sprites

        self.x = x
        self.y = (height - 300) + random.randint(0, 5) * 10

        # keep track of whether this mascot has been hit or not
        self.is_hit = False

        self.speed = 1

        # mascots with a target are worth 2 points
        # 50% chance that this mascot has a target
        self.points = random.choice([1, 2])
        if self.points == 2:
            self.image = self.images['ub_target']
        else:
            self.image = self.images['ub_mascot']
            

    def update(self):
        '''
        general function description:
		This function updates the UB mascots when it moves off the screen

		arg: (type) description
        self: instance of class

		return: (type) description
        Does not return anything
	    '''
        self.x += self.speed

        # if this mascot goes off screen, remove and add a new mascot to the group
        if self.x > 1200 - self.image.get_width():
            mascot = UBMascot(0 - self.image.get_width(), self.height, self.images, self.screen,self.ub_group, self.all_sprites)
            self.ub_group.add(mascot)
            self.all_sprites.add(mascot)
            self.kill()
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        '''
        general function description:
		This function draws the pole and keeps the UB mascot on screen if it hasn't been hit

		arg: (type) description
        self: instance of class

		return: (type) description
        Does not return anything
	    '''
        # draw the mascot if it hasn't been hit yet
        if self.is_hit == False:
            self.screen.blit(self.image, (self.x, self.y))

        # draw the stick image
        stick_x = self.x + self.image.get_width() / 2 - self.images['pole'].get_width() / 2
        stick_y = self.y + self.image.get_height()
        self.screen.blit(self.images['pole'], (stick_x, stick_y))