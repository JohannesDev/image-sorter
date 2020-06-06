import os
import datetime
import time


def moveImages(sourcePath, destinationPath):
    print(sourcePath)
    print(destinationPath)

    folders = []
    files = []

    for entry in os.scandir(sourcePath):
        if(entry.is_file()):
            files.append(entry)

    for mfile in files:
        print(getLastModified(mfile))


def getLastModified(mfile):
    return datetime.utcfromtimestamp(mfile.stat().st_mtime)


moveImages("C:/Users/Johannes/Desktop/test/Fortgehn",
           "C:/Users/Johannes/Desktop/test/Fotos")
