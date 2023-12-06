import pygame
from src.controller import Controller

def main():
    pygame.init()
    control = Controller()
    control.mainLoop()

if __name__ == '__main__':
    main()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE #####