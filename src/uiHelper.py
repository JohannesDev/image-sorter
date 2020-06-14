from fileHelper import FileHelper, ConfigKeys
from tkinter import *


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

    def addLabel(self, text, row, column):
        Label(self.root, text=text).grid(row=row, column=column, sticky=E)

    def addButton(self, text, row, column, command):
        Button(self.root, text=text, command=lambda: [command(), print(command.__name__)]).grid(
            row=row,  column=column, sticky=W, pady=10)

    def addLogBox(self, logBox):
        logBox.grid(row=4, column=0, columnspan=12)
        # self.logBox.configure(state="disabled")

    def log(self, message):
        self.logBox.insert(INSERT, message + '\n')

    def build(self):
        self.root.mainloop()
