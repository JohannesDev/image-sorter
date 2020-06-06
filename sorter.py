# Good resource: https://realpython.com/working-with-files-in-python/

from file import moveImages

from tkinter import *
from tkinter.filedialog import askdirectory

sourcePath: StringVar
destinationPath: StringVar


# callbacks
def getSourcePath():
    path = askdirectory()
    sourcePath.set(path)


def getDestinationPath():
    path = askdirectory()
    destinationPath.set(path)


root = Tk()

# SourcePath
Label(root, text="Source Path").grid(
    row=0, column=0, sticky=E)

sourcePath = StringVar()
sourcePath.set("C:/Users/Johannes/Desktop/test/Fortgehn")
tb_SourcePath = Entry(root, textvariable=sourcePath, width=70)
tb_SourcePath.grid(row=0, column=1, columnspan=10)

Button(root, text='Open', command=getSourcePath).grid(
    row=0, column=11, sticky=W, pady=5)

# DestinationPath
Label(root, text="Destination Path").grid(
    row=1, column=0, sticky=E)

destinationPath = StringVar()
destinationPath.set("C:/Users/Johannes/Desktop/test/Fotos")
tb_DestinationPath = Entry(root, textvariable=destinationPath, width=70)
tb_DestinationPath.grid(row=1, column=1, columnspan=10)

Button(root, text='Open', command=getDestinationPath).grid(
    row=1, column=11, sticky=W, pady=5)

#
#
# Actions
Button(root, text='Move Images', command=lambda: moveImages(sourcePath.get(), destinationPath.get())).grid(
    row=3, column=10, sticky=W, pady=10)

root.mainloop()
