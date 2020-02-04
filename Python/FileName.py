# FileName class
# Xu Yi
# 2020

class FileName(object):

    def __init__(self, path):
        self.path = path
        self.LastSlash = Position(self.path).LastSlash
        self.LastDot = Position(self.path).LastDot

        self.folder = self.getFolder()
        self.name = self.getName()
        self.suffix = self.getSuffix()

    def getFolder(self):
        # slice before LastSlash. i.e. no '/'
        return self.path[:self.LastSlash]

    def getName(self):
        return self.path[(self.LastSlash+1):self.LastDot]

    def getSuffix(self):
        return self.path[(self.LastDot+1):]


class Position(object):

    def __init__(self, path):
        self.path = path
        self.pathLen = len(path)
        self.LastSlash = self.getLastSlash()
        self.LastDot = self.getLastDot()

    def getLastSlash(self):
        return self.getLast('/')

    def getLastDot(self):
        return self.getLast('.')

    def getLast(self, xChar): # xChar: '/' or '.'
        val_char = ''
        iVal = 0
        while val_char != xChar:
            iVal += 1
            val_char = self.path[-iVal]
        return self.pathLen - iVal  # start from 0
