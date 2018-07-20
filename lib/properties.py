from ast import literal_eval
# Object that stores certain properties like resolution and other user settings
class Properties(object):

    __fileLocation = "properties.txt"
    __resolutionIdentifier = "RESOLUTION"
    __fullscreenIdentifier = "FULLSCREEN"

    # Default values for properties
    __resolution = (0,0)
    __fullscreen = True

    # Load all properties from the file
    @classmethod
    def init(cls):
        with open(cls.__fileLocation, "r") as file:
            for line in file:
                if "=" in line:
                    identifier, property = line.split("=")
                    property = literal_eval(property)
                    if identifier == cls.__resolutionIdentifier:
                        cls.__resolution = property
                    elif identifier == cls.__fullscreenIdentifier:
                        cls.__fullscreen = property

    # Get current resolution
    @classmethod
    def getResolution(cls):
        return cls.__resolution

    # Set resolution
    @classmethod
    def setResolution(cls, resolution):
        cls.__resolution = resolution
        cls.createOrUpdateValue(cls.__resolutionIdentifier, cls.__resolution)

    # Get fullscreen property
    @classmethod
    def isFullscreen(cls):
        return cls.__fullscreen

    # Set fullscreen to oposit value
    @classmethod
    def toggleFullscreen(cls):
        cls.__fullscreen = cls.__fullscreen == False
        cls.createOrUpdateValue(cls.__fullscreenIdentifier, cls.__fullscreen)

    # Update a specific value by rewriting the entire file
    # TODO: optimize to not have the entire file rewritten each time
    @classmethod
    def createOrUpdateValue(cls, property, newValue):
        lines = []
        with open(cls.__fileLocation, "r+") as file:
            lines.append("\n")
            for line in file:
                if "=" in line:
                    identifier, value = line.split("=")
                    if identifier == property:
                        line = property + "=" + str(newValue) + "\n"
                    lines.append(line)
            file.truncate(0)
            for line in lines:
                file.write(line)
