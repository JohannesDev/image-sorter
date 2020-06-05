from tkinter import *
from tkinter.filedialog import askdirectory


def setup():
    root = Tk()

    # SourcePath
    Label(root, text="Source Path").grid(row=0, column=0)

    global sourcePath
    sourcePath = StringVar()
    tb_SourcePath = Entry(root, textvariable=sourcePath)
    tb_SourcePath.grid(row=0, column=1)

    Button(root, text='Open', command=getSourcePath).grid(
        row=0, column=2, sticky=W, pady=4)

    # DestinationPath
    Label(root, text="Destination Path").grid(row=1, column=0)

    global destinationPath
    destinationPath = StringVar()
    tb_DestinationPath = Entry(root, textvariable=destinationPath)
    tb_DestinationPath.grid(row=1, column=1)

    Button(root, text='Open', command=getDestinationPath).grid(
        row=1, column=2, sticky=W, pady=4)

    root.mainloop()


def getSourcePath():
    path = askdirectory()
    sourcePath.set(path)


def getDestinationPath():
    path = askdirectory()
    destinationPath.set(path)
