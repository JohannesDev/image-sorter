from uiHelper import UiHelper
from fileHelper import FileHelper, ConfigKeys
from tkinter import *

# load last paths
fileHelper = FileHelper()
sourcePath = fileHelper.loadConfig(ConfigKeys.LastSourcePath)
destinationPath = fileHelper.loadConfig(ConfigKeys.LastDestinationPath)

# setup
uiHelper = UiHelper(root=Tk(), fileHelper=fileHelper)
uiHelper.sourcePath = sourcePath
uiHelper.destinationPath = destinationPath

# add ui elements
uiHelper.addLabel("Source Path", row=0, column=0)
uiHelper.addLabel("Destination Path", row=1, column=0)
uiHelper.addTextBoxes()
uiHelper.addOpenButtons()

uiHelper.addButton('Switch Paths', row=0, column=11,
                   command=uiHelper.switchPaths)

uiHelper.addButton('Move Images', row=3, column=10,
                   command=lambda: fileHelper.moveImages(uiHelper.sourcePath.get(), uiHelper.destinationPath.get()))

uiHelper.addButton('Extract Images', row=3, column=1,
                   command=lambda: fileHelper.extractImages(uiHelper.sourcePath.get(), uiHelper.destinationPath.get()))

uiHelper.addLogBox()

uiHelper.build()
