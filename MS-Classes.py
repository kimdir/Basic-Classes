"""
Manager class configuration for importing into other projcets
"""
import csv
import SQLAlchemy as sql
from importlib import import_module

class Manager:
    managerCount = 0

    def __new__(self):
        managerCount += 1

    def __init__(self):
        self.agentDict = {}
        self.handlerDict = {}

        self.lastAgentID = 0
        self.lastHandlerID = 0

    def addAgent(self,agentName):
        newAgent = globals()[agentName]
        newAgentName = concat("Agent ", self.lastAgentID)
        self.lastAgentID += 1

        self.agentDict[newAgentName] = newAgent()

    def addHandler(self,handlerName):
        newHandler = globals()[handlerName]
        newHandlerName = concat("Handler ", self.lastHandlerID)
        self.lastHandlerID += 1

        self.handlerDict[newHandlerName] = newAgent()


class Agent:
    """Base class for all internal operators."""
    agentCount = 0

    def __new__(self):
        agentCount += 1

    def __init__(self):
        self.agentID = agentCount
        self.agentName = ""
        self.agentType = self.__str__()


class Handler:
    """Base class for all external operators."""
    handlerCount = 0

    def __new__(self):
        handlerCount += 1

    def __init__(self):
        self.handlerID = handlerCount
        self.handlerName = ""
        self.handlerType = self.__str__()

        self.IOPaths = {}

    def AddIOPath(self,pathName,path):
        self.IOPaths[pathName,path]
        print("Successfully added ")


class PathAgent(Agent):
    def __init__(self):
        self.pathDict = {"root":""}

    def addPath(self, label, newPath):
        self.pathDict[label] = newPath
        print("Added %s path." % (label))

    def printPath(self, label=""):
        if label == "":
            print(self.pathDict)
        else:
            print(self.pathDict[label])

class ImportHandler(Handler):
    """Debugging and error checking handler related to library imports."""

    def __init__(self,modulePath):
        self.ModuleList = []
        self.AddIOPath("Modules",modulePath)

        self.GetModuleList()
        self.CheckImportedModules()

    def CheckImportedModules(self):
        for module in self.ModuleList:
            if module not in sys.modules:
                import_module(module)

    def PrintImportedModules(self):
        print(self.ModuleList)

class CSVHandler(Handler):
    """Data handler for CSV data."""
    def __init__(self):
        self.delimiter = ","
        self.rawLines = []
        self.cleanLines = []
        self.splitLines = []

    def ReadCSV(self,csvPath):
        """Reads CSV data into a list on a line-by-line basis"""
        with open(csvPath) as rFile:
            csvReader = csv.reader(csv_file, delimiter = self.delimiter)
            self.rawLines = csvReader.readlines()

    def CleanCSV(self):
        """Strips blank space from the end of CSV lines."""
        for line in self.rawLines:
            line.rstrip()
            if len(line) != 0:
                self.cleanLines.append(line)

    def SplitCSV(self):
        """Splits the CSV data based on pre-set delimiters."""
        for line in self.cleanLines:
            splitLines = line.split(self.delimiter)
            self.splitLines.append(splitLines)

    def ProcessCSV(self,csvPath):
        """Full method for processing CSV files into lists."""
        try:
            self.ReadCSV(csvPath)
            print("Successfully read CSV.")
            self.CleanCSV()
            print("Successfully cleaned CSV.")
            self.SplitCSV()
            print("Successfully split CSV.")
        except:
            print("Failed to complete import process.")

class SQLHandler(Handler):
    #TODO: Write SQL handler methods
    def __init__(self):
        pass

    def Select(self):
        pass

    def Insert(self):
        pass

    def Update(self):
        pass

    def Delete(self):
        pass


if __name__ == "__main__":
    pass
