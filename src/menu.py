import pygame
import random
#model
class Menu(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        '''
        general function description:
		This function initializes the menu object

		arg: (type) description
        self: instance of class
        name: name attribute for the menu object
        x: x-position of the menu position
        y: y-position of the menu position
        img_file: the image file to represent the menu object

		return: (type) description
        Does not return anything
	    '''
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)
        
        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        
        #set other attributes
        self.name = name