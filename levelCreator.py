# Import GameMaster
from lib.levelCreatorMaster import LevelCreatorMaster

# Init the creator
LevelCreatorMaster.initCreator((1024,1024))

LevelCreatorMaster.setLevelName("MyLevel")

LevelCreatorMaster.saveLevel()

#LevelCreatorMaster.play()