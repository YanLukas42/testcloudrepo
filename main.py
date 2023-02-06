import pygame 
from pygame import *

pygame.init()

fps=60
screen_width = 711
screen_height = 424
pygame.display.set_caption("Lukas Interprise INC.")
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

#
menino_vel = 3
menino_x = 300 
menino_y = 282

img_back = pygame.image.load("background.jpg")


###
##   CLASSE DO PLAYER:
#

class Player():

    def __init__(self, x, y):
        self.list_rigth = []
        self.list_left = []
        self.index = 0
        self.counter = 0

        for i in range(1, 5):
            self.menino_img = pygame.image.load(f"Idle ({i})_resized.png")
            img_left = pygame.transform.flip(self.menino_img, True, False)

            self.list_rigth.append(self.menino_img)
            self.list_left.append(img_left)
            

        self.image = self.list_rigth[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.direction = 0

    def update(self):
        walk_cooldown = 20
        #get key pressed
        dx = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.x > 0:
            dx -= menino_vel
        if key[pygame.K_RIGHT] and self.rect.right -45 < screen_width:
            dx += menino_vel 

        self.rect.x += dx 

        #handle animation
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.list_rigth):
                self.index = 0
            self.image = self.list_rigth[self.index]

        #draw player onto screen
        screen.blit(self.menino_img, self.rect)


player = Player(menino_x, menino_y)


###
## LOOP PRINCIPAL
#

run = True 
while run:
    clock.tick(fps)
    screen.blit(img_back, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player.update()
    pygame.display.update()

pygame.quit()
