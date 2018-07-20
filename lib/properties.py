from ast import literal_eval
# For lack of a better name: master object that stores certain properties
class Properties(object):

    __fileLocation = "properties.txt"
    __resolution = (0,0)
    __fullscreen = True

    @classmethod
    def init(cls):
        with open(cls.__fileLocation, "r") as file:
            for line in file:
                identifier, property = line.split("=")
                property = literal_eval(property)
                if identifier == "RESOLUTION":
                    cls.__resolution = property
                elif identifier == "FULLSCREEN":
                    cls.__fullscreen = property

    @classmethod
    def getResolution(cls):
        return cls.__resolution

    @classmethod
    def isFullscreen(cls):
        return cls.__fullscreen
