from os import walk, path
from datetime import datetime
from time import time


def moveImages(sourcePath, destinationPath):
    print(sourcePath)
    print(destinationPath)

    folders = []
    files = []

    for (dirpath, dirnames, filenames) in walk(destinationPath):
        folders.extend(dirpath)
        break

    for (dirpath, dirnames, filenames) in walk(sourcePath):
        for filename in filenames:
            files.append(dirpath + "/" + filename)

        break

    for onefile in files:
        print(onefile + ":" + str(formatTime(path.getctime(onefile))))


def formatTime(ctime):
    return datetime.strptime(ctime, "%a %b %d %H:%M:%S %Y")
