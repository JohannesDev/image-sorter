from uiHelper import UiHelper
from fileHelper import FileHelper, ConfigKeys
from tkinter import *

# load last paths
fileHelper = FileHelper()
sourcePath = fileHelper.loadConfig(ConfigKeys.LastSourcePath)
destinationPath = fileHelper.loadConfig(ConfigKeys.LastDestinationPath)

uiHelper = UiHelper(root=Tk(), sourcePath=sourcePath,
                    destinationPath=destinationPath)
