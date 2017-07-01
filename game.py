# Import lib and classes
import pygame
from objects.player import Player
from objects.object import Object
from UI.controller import InterfaceController

# Init pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((1000,800)#, pygame.FULLSCREEN, 16
    )
screen.fill((255,255,255))

# Init the player and draw him
player = Player((75, screen.get_height()-180), screen, 100, 20)

background = Object((0,0), screen, "sprites/background.png", screen.get_width(), screen.get_height())

# Loop until the user clicks the close button.
done = False

def resetCanvas():
    background.draw()
    player.draw()
    pygame.display.flip()

# -------- Main Program Loop -----------
while not done:
    resetCanvas()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.move(-1)
            elif event.key == pygame.K_d:
                player.move()
        pygame.display.flip()
