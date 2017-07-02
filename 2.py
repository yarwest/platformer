# Import lib and classes
import pygame
from objects.gameMaster import GameMaster

# Init the environment
GameMaster.__init__("2", "gras-dirt",(1024,1024),(1024,1600))

GameMaster.play()
