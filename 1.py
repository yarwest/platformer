# Import lib and classes
import pygame
from objects.player import Player
from objects.environment import Environment

# Init pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((1024,1024)#, pygame.FULLSCREEN, 16
    )

# Init the player
player = Player((130, 580), screen, 100, 10)
moving = 0

# Init the environment
environment = Environment(screen, "1", "gras-dirt")

# Loop until the user clicks the close button.
done = False

def resetCanvas():
    screen.fill((84, 149, 255))
    environment.draw()
    player.move(moving)
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
                moving = -1
            elif event.key == pygame.K_d:
                moving = 1
            elif event.key == pygame.K_w or event.key == pygame.K_SPACE:
                player.jump()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                moving = 0
        pygame.display.flip()
