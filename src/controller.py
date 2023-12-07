import sys
import pygame
import random
from src import menu
from src import UBMascot
from src import SBMascot

class Controller:
    def __init__(self):

        #SET UP SCREEN
        pygame.init()
        self.width = 900
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Bearcat Hunt")
        self.clock = pygame.time.Clock()
        pygame.font.init()

        #LOAD IMAGES
        self.images = {}  # Initialize the images dictionary
        self.load_image('stony_powerup', 'assets/stony_powerup.png')
        self.load_image('menu_screen', 'assets/menu_screen.png')
        self.load_image('start', 'assets/start.png')
        self.load_image('exit','assets/exit.png')
        self.load_image('background', 'assets/background.png')
        self.load_image('wood', 'assets/wood.png')
        self.load_image('waves', 'assets/waves.png')
        self.load_image('ub_mascot', 'assets/ub_mascot.png')
        self.load_image('ub_target', 'assets/ub_target.png')
        self.load_image('stony_mascot', 'assets/stony_mascot.png', True)
        self.load_image('stony_target', 'assets/stony_target.png', True)
        self.load_image('pole', 'assets/pole.png')
        self.load_image('paper', 'assets/crumpled_paper.png')
        self.load_image('score', 'assets/text_score_small.png')
        self.load_image('colon', 'assets/colon.png')
        self.load_image('gameover', 'assets/text_gameover.png')
        self.load_image('crosshair', 'assets/crosshair.png')
        self.load_image('timer', 'assets/timer.png')
        self.load_image('end_screen', 'assets/end_screen.png')
        # load the number images
        
        for i in range(10):
            self.load_image(str(i), f'assets/num_{i}.png')

        

        #LOAD SPRITES
        self.stony_group = pygame.sprite.Group()
        self.ub_group = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.power_sprites = pygame.sprite.Group()

        #GAME VARIABLES
        self.remaining_papers = 10
        self.score = 0
        self.timer = 6000

        self.STATE = "MENU"

         # add the mascots
        for i in range(4):
            mascot = UBMascot.UBMascot(i * (self.images['ub_mascot'].get_width() + 36) * 2, self.height, self.images, self.screen, self.ub_group, self.all_sprites)
            self.ub_group.add(mascot)
            self.all_sprites.add(mascot)

        for i in range(4):
            mascot = SBMascot.SBMascot(i * (self.images['stony_mascot'].get_width() + 36) * 2, self.height, self.images, self.screen, self.ub_group, self.all_sprites,self.remaining_papers, self.power_sprites)
            self.stony_group.add(mascot)
            self.all_sprites.add(mascot)

    def load_image(self, name, filename, flip_x = False):
        self.images[name] = pygame.image.load(filename).convert_alpha()
        # flip image on the x-axis
        if flip_x:
            self.images[name] = pygame.transform.flip(self.images[name], True, False)

    def mainLoop(self):
          while True:
            if(self.STATE == "MENU"):
                self.mainmenu()
            elif(self.STATE == "GAME"):
                self.gameLoop()
            elif(self.STATE == "GAMEOVER"):
                self.gameOver()

    def mainmenu(self):
        # MAIN MENU BUTTONS
        self.playButton = menu.Menu("Play", 690, 250, "assets/start.png")
        self.quitButton = menu.Menu("Quit", 690, 375, "assets/exit.png")
        
        self.menu_sprites = pygame.sprite.Group(self.playButton, self.quitButton)

        while self.STATE == "MENU":
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        if self.playButton.rect.collidepoint(pos):
                            self.STATE = "GAME"
                        if self.quitButton.rect.collidepoint(pos):
                            pygame.quit()
                            sys.exit()
            self.menu_sprites.update()
            
            # SET UP MAIN MENU BACKGROUND
            for background_x in range(0, self.width, self.images['menu_screen'].get_width()):
                for background_y in range(0, self.height, self.images['menu_screen'].get_height()):
                    self.screen.blit(self.images['menu_screen'], (background_x, background_y))
                
            # DRAW MENU SPRITES
            self.menu_sprites.draw(self.screen)
            pygame.display.flip()
    
    def gameLoop(self):
        # SET FPS
        clock = pygame.time.Clock()
        fps = 120
        
        while self.STATE == "GAME":

            clock.tick(fps)
            self.timer -= 1
            #print(self.timer)

            # SETS EVENTS
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # detect mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # decrement papers left
                    self.remaining_papers -= 1

                    # coordinates of the mouse click
                    click_x, click_y = event.pos

                    # check if a mascot was hit
                    for sprite in self.power_sprites:
                        if sprite.is_hit == False and sprite.rect.collidepoint(click_x, click_y):
                            sprite.is_hit = True
                            self.remaining_papers += 3
                            break
                
                    for sprite in self.all_sprites:
                        if sprite.is_hit == False and sprite.rect.collidepoint(click_x, click_y):
                            sprite.is_hit = True
                            self.score += sprite.points
                            break

            # draw the background
            for background_x in range(0, self.width, self.images['background'].get_width()):
                for background_y in range(0, self.height, self.images['background'].get_height()):
                    self.screen.blit(self.images['background'], (background_x, background_y))

            # draw the waves
            for waves in range(0, self.width, self.images['waves'].get_width()):
                self.screen.blit(self.images['waves'], (waves, self.height - 260))

            # draw the mascots
            self.stony_group.update()
            for mascot in self.stony_group:
                mascot.draw()


            # draw the waves
            for waves in range(0, self.width, self.images['waves'].get_width()):
                self.screen.blit(self.images['waves'], (waves, self.height - 180))

            # draw the mascots
            self.ub_group.update()
            for mascot in self.ub_group:
                mascot.draw()

            # draw the waves 
            for waves in range(-70, self.width, self.images['waves'].get_width()):
                self.screen.blit(self.images['waves'], (waves, self.height - 155))        

            # draw the wood
            for wood_x in range(0, self.width, self.images['wood'].get_width()):
                self.screen.blit(self.images['wood'], (wood_x, self.height - 80))

            # draw remaining papers
            for i in range(self.remaining_papers):
                self.screen.blit(self.images['paper'], (i * 30 + 100, self.height - 60))

            # draw the crosshair
            crosshair_x, crosshair_y = pygame.mouse.get_pos()
            crosshair_x -= self.images['crosshair'].get_width() / 2
            crosshair_y -= self.images['crosshair'].get_height() / 2
            self.screen.blit(self.images['crosshair'], (crosshair_x, crosshair_y))
            if(crosshair_x < self.width/2):
                self.screen.blit(self.images['stony_mascot'], (self.width/2, 450))
            else:
                self.screen.blit(self.images['ub_mascot'], (self.width/2, 450))

            self.display_score()
            self.display_timer()
            pygame.display.update()

            if(self.remaining_papers == 0 or self.timer <= 0):
                self.STATE = 'GAMEOVER'
   
    # function for displaying the current score
    def display_score(self):
        self.screen.blit(self.images['score'], (5, 5))
        self.screen.blit(self.images['colon'], (5 + self.images['score'].get_width(), 5))

        digit_x = self.images['score'].get_width() + self.images['colon'].get_width() + 20
        for digit in str(self.score):
            self.screen.blit(self.images[digit], (digit_x - 20, 5))
            digit_x += 25

    def display_timer(self):
        self.screen.blit(self.images['timer'], (505, 5))
        self.screen.blit(self.images['colon'], (5 + self.images['score'].get_width() + 500, 5))

        digit_x = self.images['score'].get_width() + self.images['colon'].get_width()
        self.display_new_time = str(self.timer)[:2]
        for digit in str(self.display_new_time):
            self.screen.blit(self.images[digit], (digit_x - 100, 5))
            digit_x += 25
    
    def gameOver(self):

        ''' Drawing End Screen '''
        # SET UP End screen
        for background_x in range(0, self.width, self.images['end_screen'].get_width()):
            for background_y in range(0, self.height, self.images['end_screen'].get_height()):
                self.screen.blit(self.images['end_screen'], (background_x, background_y))

        # load image sprites
        self.quitButton = menu.Menu("Quit", self.width/2, 350, "assets/exit.png")
        self.scoreContainer = menu.Menu("Score", self.width/2, 275, "assets/text_score_small.png")
        self.gameOverContainer = menu.Menu("text_gameover", self.width/2, 200, "assets/text_gameover.png")
        self.menu_sprites = pygame.sprite.Group(self.quitButton, self.scoreContainer,self.gameOverContainer)
            
        # load sprites
        self.menu_sprites.draw(self.screen)
        
        pygame.display.flip()

        # quit button logic
        while self.STATE == "GAMEOVER":

            pygame.mouse.set_visible(True)
            pygame.display.update()
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.quitButton.rect.collidepoint(pos):
                        pygame.quit()
                        sys.exit()