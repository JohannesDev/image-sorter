import os
import shutil
from datetime import datetime
import time
import json

# LastSourcePath and LastDestinationPath
configPath = "config.json"


class ConfigKeys:
    LastSourcePath = "LastSourcePath"
    LastDestinationPath = "LastDestinationPath"
    All = "All"


monthNames = {
    1: "01_Jänner",
    2: "02_Februar",
    3: "03_März",
    4: "04_April",
    5: "05_Mai",
    6: "06_Juni",
    7: "07_Juli",
    8: "08_August",
    9: "09_September",
    10: "10_Oktober",
    11: "11_November",
    12: "12_Dezember",
}


def moveImages(sourcePath, destinationPath):
    # print(sourcePath)
    # print(destinationPath)

    for sourceFile in os.scandir(sourcePath):
        if(sourceFile.is_file()):
            # create year folder if it doesn't exist
            year = getYear(sourceFile)
            creatDir(destinationPath + '/' + year)

            # create month folder if it doesn't exist
            month = getMonth(sourceFile)
            monthName = monthNames.get(month)
            creatDir(destinationPath + '/' + year + '/' + monthName)

            # move file to folder
            moveFile(sourceFile.path, destinationPath + '/' + year + '/' +
                     monthName + '/' + sourceFile.name)


def loadConfig(key):
    config = {ConfigKeys.LastSourcePath: "C:/",
              ConfigKeys.LastDestinationPath: "D:/"}

    if os.path.exists(configPath):
        config = json.load(open(configPath))

    if key != ConfigKeys.All:
        return config.get(key)
    else:
        return config


def saveConfig(key, data):
    config = loadConfig(ConfigKeys.All)

    if key != ConfigKeys.All:
        config[key] = data
    else:
        config = data

    json.dump(config, open(configPath, 'w'))


def getYear(sourceFile):
    fileTime = sourceFile.stat().st_mtime
    return str(datetime.utcfromtimestamp(fileTime).year)


def getMonth(sourceFile):
    fileTime = sourceFile.stat().st_mtime
    return datetime.utcfromtimestamp(fileTime).month


def creatDir(path):
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        print("CREATE ERROR: Path " +
              path + " already exists.")


def moveFile(sourcePath, destinationPath):
    if not os.path.exists(destinationPath):
        shutil.move(sourcePath, destinationPath)
    else:
        print("MOVE ERROR: Destination path " +
              destinationPath + " already exists. Skipping file.")


# moveImages("C:/",
#           "D:/")
