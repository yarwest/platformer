# Import GameMaster
import pygame
from lib import LevelCreatorMaster

# Init the creator
LevelCreatorMaster.init()

LevelCreatorMaster.setLevelName("MyLevel")

LevelCreatorMaster.saveLevel()

# Loop until the user clicks the close button.
done = False

# -------- Main Program Loop -----------
while not done:
    LevelCreatorMaster.resetCanvas()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse click")
        elif event.type == pygame.KEYDOWN:
            print("key down")
            if event.key == pygame.K_ESCAPE:
                done = True
        elif event.type == pygame.KEYUP:
            print("key up")
        pygame.display.flip()
