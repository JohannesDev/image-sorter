import os
import shutil
from datetime import datetime
import time
import json


class ConfigKeys:
    LastSourcePath = "LastSourcePath"
    LastDestinationPath = "LastDestinationPath"
    All = "All"


class FileHelper():
    def __init__(self):
        # LastSourcePath and LastDestinationPath
        self.configPath = "config.json"

        self.monthNames = {
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

    # private

    def __getYear(self, sourceFile):
        fileTime = sourceFile.stat().st_mtime
        return str(datetime.utcfromtimestamp(fileTime).year)

    def __getMonth(self, sourceFile):
        fileTime = sourceFile.stat().st_mtime
        return datetime.utcfromtimestamp(fileTime).month

    # public

    def moveImages(self, sourcePath, destinationPath):
        for sourceFile in os.scandir(sourcePath):
            if(sourceFile.is_file()):
                # create year folder if it doesn't exist
                year = self.__getYear(sourceFile)
                self.creatDir(destinationPath + '/' + year)

                # create month folder if it doesn't exist
                month = self.__getMonth(sourceFile)
                monthName = self.monthNames.get(month)
                self.creatDir(destinationPath + '/' + year + '/' + monthName)

                # move file to folder
                self.moveFile(sourceFile.path, destinationPath + '/' + year + '/' +
                              monthName + '/' + sourceFile.name)

    def extractImages(self, sourcePath, destinationPath):
        for sourceFile in os.scandir(sourcePath):
            if(sourceFile.is_file()):
                # move file to folder
                self.moveFile(sourceFile.path, destinationPath +
                              '/' + sourceFile.name)

    def loadConfig(self, key):
        config = {ConfigKeys.LastSourcePath: "C:/",
                  ConfigKeys.LastDestinationPath: "D:/"}

        if os.path.exists(self.configPath):
            config = json.load(open(self.configPath))

        if key != ConfigKeys.All:
            return config.get(key)
        else:
            return config

    def saveConfig(self, key, data):
        config = self.loadConfig(ConfigKeys.All)

        if key != ConfigKeys.All:
            config[key] = data
        else:
            config = data

        json.dump(config, open(self.configPath, 'w'))

    def creatDir(self, path):
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            print("CREATE ERROR: Path " +
                  path + " already exists.")

    def moveFile(self, sourcePath, destinationPath):
        if not os.path.exists(destinationPath):
            shutil.move(sourcePath, destinationPath)
        else:
            print("MOVE ERROR: Destination path " +
                  destinationPath + " already exists. Skipping file.")
