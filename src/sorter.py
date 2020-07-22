from uiHelper import UiHelper
from fileHelper import FileHelper, ConfigKeys
from tkinter import *
from tkinter.filedialog import askdirectory


def openSourcePath():
    path = askdirectory()
    uiHelper.sourcePath = path
    fileHelper.saveConfig(ConfigKeys.LastSourcePath, path)


def openDestinationPath():
    path = askdirectory()
    uiHelper.destinationPath = path
    fileHelper.saveConfig(ConfigKeys.LastDestinationPath, path)


def switchPaths():
    helper = uiHelper.sourcePath.get()

    fileHelper.saveConfig(ConfigKeys.LastSourcePath, uiHelper.destinationPath.get())
    uiHelper.sourcePath.set(uiHelper.destinationPath.get())

    uiHelper.destinationPath.set(helper)
    fileHelper.saveConfig(ConfigKeys.LastDestinationPath, helper)


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
uiHelper.addButton("Open", row=0, column=10, command=openSourcePath)
uiHelper.addButton("Open", row=1, column=10, command=openDestinationPath)


uiHelper.addButton("Switch Paths", row=0, column=11, command=switchPaths)

uiHelper.addButton(
    "Move Images",
    row=3,
    column=10,
    command=lambda: fileHelper.moveImages(
        uiHelper.sourcePath.get(), uiHelper.destinationPath.get()
    ),
)

uiHelper.addButton(
    "Extract Images",
    row=3,
    column=1,
    command=lambda: fileHelper.extractImages(
        uiHelper.sourcePath.get(), uiHelper.destinationPath.get()
    ),
)

uiHelper.build()
