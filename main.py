import pygame
from src import Controller

#import your controller

def main():
    #Create an instance on your controller object
    #Call your mainloop
    pygame.init()
    control = Controller()
    control.mainLoop()

if __name__ == '__main__':
    main()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE #####