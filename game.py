# Import lib and classes
import pygame
from objects.player import Player
from objects.environment import Environment
from objects.environmentObject import EnvironmentObject

# Init pygame
pygame.init()

TOP_LEFT = 0
TOP_MIDDLE = 1
TOP_RIGHT = 2
MIDDLE_LEFT = 3
CENTER = 4
MIDDLE_RIGHT = 5
BOTTOM_LEFT = 6
BOTTOM_MIDDLE = 7
BOTTOM_RIGHT = 8
INNER_BOTTOM_LEFT = 9
INNER_BOTTOM_RIGHT = 10
INNER_TOP_LEFT = 11
INNER_TOP_RIGHT = 12

# Set up the screen
screen = pygame.display.set_mode((1024,1024)#, pygame.FULLSCREEN, 16
    )

# Init the player
player = Player((130, 580), screen, 100, 20)

# Init the environment
pixels = 64
environmentWH = screen.get_height()/pixels
environmentObjects = []
# Frame left, bottom and right
for i in range(environmentWH):
    offset = 0 + (pixels*i)
    environmentObjects.append(
        EnvironmentObject((0,offset),screen,CENTER)
    )
    environmentObjects.append(
        EnvironmentObject((offset,screen.get_height()-pixels),screen,CENTER)
    )
    environmentObjects.append(
        EnvironmentObject((screen.get_width()-pixels,offset),screen,CENTER)
    )

environmentObjects.extend([
    # Left column
    EnvironmentObject((64,0),screen,INNER_TOP_LEFT),
    EnvironmentObject((128,0),screen,BOTTOM_RIGHT),
    EnvironmentObject((64,64),screen,MIDDLE_RIGHT),
    EnvironmentObject((64,128),screen,MIDDLE_RIGHT),
    EnvironmentObject((64,192),screen,MIDDLE_RIGHT),
    EnvironmentObject((64,256),screen,MIDDLE_RIGHT),
    EnvironmentObject((64,320),screen,MIDDLE_RIGHT),
    EnvironmentObject((64,384),screen,MIDDLE_RIGHT),
    EnvironmentObject((64,448),screen,MIDDLE_RIGHT),
    EnvironmentObject((64,512),screen,MIDDLE_RIGHT),
    EnvironmentObject((64,576),screen,MIDDLE_RIGHT),
    EnvironmentObject((64,640),screen,MIDDLE_RIGHT),

    # Left bottom block
    EnvironmentObject((0,704),screen,TOP_MIDDLE),
    EnvironmentObject((64,704),screen,TOP_MIDDLE),
    EnvironmentObject((128,704),screen,TOP_MIDDLE),
    EnvironmentObject((192,704),screen,TOP_RIGHT),
    EnvironmentObject((192,768),screen,MIDDLE_RIGHT),
    EnvironmentObject((192,832),screen,MIDDLE_RIGHT),
    EnvironmentObject((192,896),screen,INNER_BOTTOM_LEFT),
    EnvironmentObject((128,768),screen,CENTER),
    EnvironmentObject((128,832),screen,CENTER),
    EnvironmentObject((128,896),screen,CENTER),
    EnvironmentObject((64,768),screen,CENTER),
    EnvironmentObject((64,832),screen,CENTER),
    EnvironmentObject((64,896),screen,CENTER),

    # Middle bottom section
    EnvironmentObject((256,896),screen,TOP_MIDDLE),
    EnvironmentObject((320,896),screen,TOP_MIDDLE),
    EnvironmentObject((384,896),screen,TOP_MIDDLE),
    EnvironmentObject((448,896),screen,TOP_MIDDLE),
    EnvironmentObject((512,896),screen,TOP_MIDDLE),
    EnvironmentObject((576,896),screen,TOP_MIDDLE),
    EnvironmentObject((640,896),screen,INNER_BOTTOM_RIGHT),

    # Right bottom block
    EnvironmentObject((640,832),screen,MIDDLE_LEFT),
    EnvironmentObject((640,768),screen,MIDDLE_LEFT),
    EnvironmentObject((640,704),screen,MIDDLE_LEFT),
    EnvironmentObject((640,640),screen,MIDDLE_LEFT),
    EnvironmentObject((640,576),screen,MIDDLE_LEFT),
    EnvironmentObject((640,512),screen,MIDDLE_LEFT),
    EnvironmentObject((704,896),screen,CENTER),
    EnvironmentObject((704,832),screen,CENTER),
    EnvironmentObject((704,768),screen,CENTER),
    EnvironmentObject((704,704),screen,CENTER),
    EnvironmentObject((704,640),screen,CENTER),
    EnvironmentObject((704,576),screen,CENTER),
    EnvironmentObject((704,512),screen,CENTER),
    EnvironmentObject((768,896),screen,CENTER),
    EnvironmentObject((768,832),screen,CENTER),
    EnvironmentObject((768,768),screen,CENTER),
    EnvironmentObject((768,704),screen,CENTER),
    EnvironmentObject((768,640),screen,CENTER),
    EnvironmentObject((768,576),screen,CENTER),
    EnvironmentObject((768,512),screen,CENTER),
    EnvironmentObject((832,896),screen,CENTER),
    EnvironmentObject((832,832),screen,CENTER),
    EnvironmentObject((832,768),screen,CENTER),
    EnvironmentObject((832,704),screen,CENTER),
    EnvironmentObject((832,640),screen,CENTER),
    EnvironmentObject((832,576),screen,CENTER),
    EnvironmentObject((832,512),screen,CENTER),
    EnvironmentObject((896,896),screen,CENTER),
    EnvironmentObject((896,832),screen,CENTER),
    EnvironmentObject((896,768),screen,CENTER),
    EnvironmentObject((896,704),screen,CENTER),
    EnvironmentObject((896,640),screen,CENTER),
    EnvironmentObject((896,576),screen,CENTER),
    EnvironmentObject((896,512),screen,CENTER),
    EnvironmentObject((640,448),screen,TOP_LEFT),
    EnvironmentObject((704,448),screen,TOP_MIDDLE),
    EnvironmentObject((768,448),screen,TOP_MIDDLE),
    EnvironmentObject((832,448),screen,TOP_MIDDLE),
    EnvironmentObject((896,448),screen,INNER_BOTTOM_RIGHT),

    # Right column
    EnvironmentObject((512,0),screen,MIDDLE_LEFT),
    EnvironmentObject((576,0),screen,CENTER),
    EnvironmentObject((640,0),screen,CENTER),
    EnvironmentObject((704,0),screen,CENTER),
    EnvironmentObject((768,0),screen,CENTER),
    EnvironmentObject((832,0),screen,CENTER),
    EnvironmentObject((896,0),screen,CENTER),
    EnvironmentObject((512,64),screen,BOTTOM_LEFT),
    EnvironmentObject((576,64),screen,BOTTOM_MIDDLE),
    EnvironmentObject((640,64),screen,BOTTOM_MIDDLE),
    EnvironmentObject((704,64),screen,BOTTOM_MIDDLE),
    EnvironmentObject((768,64),screen,BOTTOM_MIDDLE),
    EnvironmentObject((832,64),screen,BOTTOM_MIDDLE),
    EnvironmentObject((896,64),screen,INNER_TOP_RIGHT),
    EnvironmentObject((896,128),screen,MIDDLE_LEFT),
    EnvironmentObject((896,192),screen,MIDDLE_LEFT),
    EnvironmentObject((896,256),screen,MIDDLE_LEFT),
    EnvironmentObject((896,320),screen,MIDDLE_LEFT),
    EnvironmentObject((896,384),screen,MIDDLE_LEFT),

    # Island
    EnvironmentObject((300,550),screen,TOP_LEFT),
    EnvironmentObject((364,550),screen,TOP_MIDDLE),
    EnvironmentObject((428,550),screen,TOP_MIDDLE),
    EnvironmentObject((492,550),screen,TOP_RIGHT),
    EnvironmentObject((300,614),screen,BOTTOM_LEFT),
    EnvironmentObject((364,614),screen,BOTTOM_MIDDLE),
    EnvironmentObject((428,614),screen,BOTTOM_MIDDLE),
    EnvironmentObject((492,614),screen,BOTTOM_RIGHT)
])
environment = Environment(screen, environmentObjects, "gras-dirt")

# Loop until the user clicks the close button.
done = False

def resetCanvas():
    screen.fill((84, 149, 255))
    environment.draw()
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
