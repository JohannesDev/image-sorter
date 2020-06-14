# Good resource: https://realpython.com/working-with-files-in-python/
# https://www.python.org/dev/peps/pep-0471/#specifics-of-proposal

from fileHelper import FileHelper, ConfigKeys
from tkinter import *
from tkinter.filedialog import askdirectory


class UiHelper():
    def __init__(self, root, sourcePath, destinationPath):
        self.root = root
        self.root.geometry('800x400')
        self.root.title('Image Sorter')

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(12, weight=1)

        self.sourcePath = StringVar()
        self.sourcePath.set(sourcePath)
        self.destinationPath = StringVar()
        self.destinationPath.set(destinationPath)

        self.fileHelper = FileHelper()

        self.setupUI()

    def setupUI(self):
        root = self.root
        # SourcePath
        Label(root, text="Source Path").grid(row=0, column=0, sticky=E)

        tb_SourcePath = Entry(root, textvariable=self.sourcePath, width=80)
        tb_SourcePath.grid(row=0, column=1, columnspan=10)

        Button(root, text='Open', command=self.onClickBrowseSourcePath).grid(
            row=0, column=11, sticky=W, pady=5)

        # DestinationPath
        Label(root, text="Destination Path").grid(
            row=1, column=0, sticky=E)

        tb_DestinationPath = Entry(
            root, textvariable=self.destinationPath, width=80)
        tb_DestinationPath.grid(row=1, column=1, columnspan=10)

        Button(root, text='Open', command=self.onClickBrowseDestinationPath).grid(
            row=1, column=11, sticky=W, pady=5)

        # Actions
        Button(root, text='Switch Paths', command=self.switchPaths).grid(
            row=0, rowspan=2, column=12, sticky=W, pady=10)
        Button(root, text='Move Images', command=lambda: self.fileHelper.moveImages(self.sourcePath.get(), self.destinationPath.get())).grid(
            row=3, column=10, sticky=W, pady=10)

        Button(root, text='Extract Images', command=lambda: self.fileHelper.extractImages(self.sourcePath.get(), self.destinationPath.get())).grid(
            row=3, column=1, sticky=W, pady=10)

        root.mainloop()

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
