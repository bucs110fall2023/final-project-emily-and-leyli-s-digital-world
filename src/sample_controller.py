import pygame
from pygame.locals import *
import random

pygame.init()

# create the window
game_width = 900
game_height = 500
screen_size = (game_width, game_height)
game_window = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Mascot Massacre')

# load images
images = {}
def load_image(name, filename, flip_x = False):
    images[name] = pygame.image.load(filename).convert_alpha()

    # flip image on the x-axis
    if flip_x:
        images[name] = pygame.transform.flip(images[name], True, False)

load_image('background', 'assets/background.png')
load_image('wood', 'assets/wood.png')
load_image('waves', 'assets/waves.png')
load_image('ub_mascot', 'assets/ub_mascot.png')
load_image('ub_target', 'assets/ub_target.png')
load_image('stony_mascot', 'assets/stony_mascot.png', True)
load_image('stony_target', 'assets/stony_target.png', True)
load_image('pole', 'assets/pole.png')
load_image('paper', 'assets/crumpled_paper.png')
load_image('score', 'assets/text_score_small.png')
load_image('colon', 'assets/colon.png')
load_image('gameover', 'assets/text_gameover.png')
load_image('crosshair', 'assets/crosshair.png')

# load the number images
for i in range(10):
    load_image(str(i), f'assets/num_{i}.png')

# function for displaying the current score
def display_score():
    game_window.blit(images['score'], (5, 5))
    game_window.blit(images['colon'], (5 + images['score'].get_width(), 5))

    digit_x = images['score'].get_width() + images['colon'].get_width() + 20
    for digit in str(score):
        game_window.blit(images[digit], (digit_x, 5))
        digit_x += 25

class Mascot(pygame.sprite.Sprite):
    
    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

        # randomly adjust the y coordinate to vary the heights of the mascots
        self.y += random.randint(0, 5) * 10

        # keep track of whether this mascot has been hit or not
        self.is_hit = False

    def draw(self):

        # draw the mascot if it hasn't been hit yet
        if self.is_hit == False:
            game_window.blit(self.image, (self.x, self.y))

        # draw the pole image
        pole_x = self.x + self.image.get_width() / 2 - images['pole'].get_width() / 2
        pole_y = self.y + self.image.get_height()
        game_window.blit(images['pole'], (pole_x, pole_y))

class UBMascot(Mascot):
    
    def __init__(self, x):

        super().__init__(x, game_height - 330)
        self.speed = 3

        # mascots with a target are worth 4 points
        # 25% chance that this mascot has a target
        self.points = random.choice([2, 2, 2, 4])

        if self.points == 4:
            self.image = images['stony_target']
        else:
            self.image = images['stony_mascot']

    def update(self):

        self.x -= self.speed

        # if this mascot goes off screen, remove and add a new mascot to the group
        if self.x < 0 - self.image.get_width():
            mas = UBMascot(1200 - self.image.get_width())
            UB_mas_group.add(mas)
            all_sprites.add(mas)
            self.kill()

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class SBMascot(Mascot):
    
    def __init__(self, x):

        super().__init__(x, game_height - 300)
        self.speed = 1.5

        # Mascots with a target are worth 2 points
        # 50% chance that this mascot has a target
        self.points = random.choice([1, 2])

        if self.points == 2:
            self.image = images['ub_target']
        else:
            self.image = images['ub_mascot']

    def update(self):

        self.x += self.speed

        # if this mascot goes off screen, remove and add a new mascot to the group
        if self.x > 1200 - self.image.get_width():
            mas = SBMascot(0 - self.image.get_width())
            stony_mas_group.add(mas)
            all_sprites.add(mas)
            self.kill()

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

# sprite groups
UB_mas_group = pygame.sprite.Group()
stony_mas_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# game variables
remaining_papers = 10
score = 0

def new_game():

    # hide the mouse cursor
    pygame.mouse.set_visible(False)

    UB_mas_group.empty()
    stony_mas_group.empty()
    all_sprites.empty()

    # add the mascots
    for i in range(4):
        mas = SBMascot(i * (images['ub_mascot'].get_width() + 36) * 2)
        stony_mas_group.add(mas)
        all_sprites.add(mas)

    # add the mascots
    for i in range(4):
        mas = UBMascot(i * (images['stony_mascot'].get_width() + 36) * 2)
        UB_mas_group.add(mas)
        all_sprites.add(mas)

new_game()

# game loop
clock = pygame.time.Clock()
fps = 120
running = True
while running:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        # detect mouse click
        if event.type == MOUSEBUTTONDOWN:

            # decrement papers left
            remaining_papers -= 1

            # coordinates of the mouse click
            click_x, click_y = event.pos

            # check if a mascot was hit
            for sprite in all_sprites:
                if sprite.is_hit == False and sprite.rect.collidepoint(click_x, click_y):
                    sprite.is_hit = True
                    score += sprite.points
                    break

    # draw the background
    for background_x in range(0, game_width, images['background'].get_width()):
        for background_y in range(0, game_height, images['background'].get_height()):
            game_window.blit(images['background'], (background_x, background_y))

    # draw the grass
    for waves in range(0, game_width, images['waves'].get_width()):
        game_window.blit(images['waves'], (waves, game_height - 260))

    # draw the mascots
    UB_mas_group.update()
    for mas in UB_mas_group:
        mas.draw()

    # draw the waves
    for waves in range(0, game_width, images['waves'].get_width()):
        game_window.blit(images['waves'], (waves, game_height - 180))

    # draw the mascots
    stony_mas_group.update()
    for mas in stony_mas_group:
        mas.draw()

    # draw the waves (front)
    for waves in range(-70, game_width, images['waves'].get_width()):
        game_window.blit(images['waves'], (waves, game_height - 155))

    # draw the table
    for wood_x in range(0, game_width, images['wood'].get_width()):
        game_window.blit(images['wood'], (wood_x, game_height - 80))

    # draw remaining papers
    for i in range(remaining_papers):
        game_window.blit(images['paper'], (i * 30 + 100, game_height - 60))

    # draw the crosshair
    crosshair_x, crosshair_y = pygame.mouse.get_pos()
    crosshair_x -= images['crosshair'].get_width() / 2
    crosshair_y -= images['crosshair'].get_height() / 2
    game_window.blit(images['crosshair'], (crosshair_x, crosshair_y))

    display_score()
    pygame.display.update()

    # display game over if there are no more papers remaining
    gameover = remaining_papers == 0
    while gameover:
        clock.tick(fps)

        # show the mouse cursor
        pygame.mouse.set_visible(True)

        gameover_x = game_width / 2 - images['gameover'].get_width() / 2
        gameover_y = 100
        game_window.blit(images['gameover'], (gameover_x, gameover_y))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                gameover = False
                running = False
            if event.type == MOUSEBUTTONDOWN:
                gameover = False
                running = True
                new_game()
                remaining_papers = 15
                score = 0

pygame.quit()