"""
Manager class configuration for importing into other projcets
"""

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
    agentCount = 0

    def __new__(self):
        agentCount += 1

    def __init__(self):
        self.agentID = agentCount
        self.agentName = ""
        self.agentType = self.__str__()


class Handler:
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
    def __init__(self,modulePath):
        self.ModuleList = []
        self.AddIOPath("Modules",modulePath)

        self.GetModuleList()
        self.CheckImportedModules()

    def CheckImportedModules(self):
        for module in self.ModuleList:
            if module not in sys.modules:
                import_module(module)



class CSVHandler(Handler):
    def __init__(self):
        pass

class SQLHandler(Handler):
    def __init__(self):
        pass


if __name__ == "__main__":
    pass
