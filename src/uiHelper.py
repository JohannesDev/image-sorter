from fileHelper import FileHelper, ConfigKeys
from tkinter import *
from tkinter.filedialog import askdirectory


class UiHelper():
    def __init__(self, root, fileHelper):
        # basic style
        self.root = root
        self.root.geometry('800x600')
        self.root.title('Image Sorter')
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(12, weight=1)

        # propetries
        self.__sourcePath = StringVar()
        self.__destinationPath = StringVar()
        self.logBox = Text(self.root)

        self.fileHelper = fileHelper

    @property
    def sourcePath(self):
        return self.__sourcePath

    @sourcePath.setter
    def sourcePath(self, sourcePath):
        self.__sourcePath.set(sourcePath)

    @property
    def destinationPath(self):
        return self.__destinationPath

    @destinationPath.setter
    def destinationPath(self, destinationPath):
        self.__destinationPath.set(destinationPath)

    def addTextBoxes(self):
        tb_SourcePath = Entry(
            self.root, textvariable=self.sourcePath, width=80)
        tb_SourcePath.grid(row=0, column=1, columnspan=9)

        tb_DestinationPath = Entry(
            self.root, textvariable=self.destinationPath, width=80)
        tb_DestinationPath.grid(row=1, column=1, columnspan=9)

    def addOpenButtons(self):
        Button(self.root, text='Open', command=self.onClickBrowseSourcePath).grid(
            row=0, column=10, sticky=W, pady=5)
        Button(self.root, text='Open', command=self.onClickBrowseDestinationPath).grid(
            row=1, column=10, sticky=W, pady=5)

    def addLabel(self, text, row, column):
        Label(self.root, text=text).grid(row=row, column=column, sticky=E)

    def addButton(self, text, row, column, command):
        Button(self.root, text=text, command=lambda: [command(), print("donee")]).grid(
            row=row,  column=column, sticky=W, pady=10)

    def addLogBox(self):
        self.logBox.grid(row=4, column=0, columnspan=12)
        self.logBox.configure(state="disabled")

    def build(self):
        self.root.mainloop()

    # ------------------------
    # ------------------------
    # ------------------------
    # ------------------------
    # helper

    def switchPaths(self):
        helper = self.sourcePath.get()
        self.fileHelper.saveConfig(
            ConfigKeys.LastSourcePath, self.destinationPath.get())
        self.sourcePath.set(self.destinationPath.get())

        self.destinationPath.set(helper)
        self.fileHelper.saveConfig(
            ConfigKeys.LastDestinationPath, helper)

    def onClickBrowseSourcePath(self):
        path = askdirectory()
        self.fileHelper.saveConfig(ConfigKeys.LastSourcePath, path)
        self.sourcePath.set(path)

    def onClickBrowseDestinationPath(self):
        path = askdirectory()
        self.fileHelper.saveConfig(ConfigKeys.LastDestinationPath, path)
        self.destinationPath.set(path)
