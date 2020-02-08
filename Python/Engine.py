# Engine class
# Xu Yi
# 2020

from FileName import FileName as FN
from JsonFile import JsonFile as JF
import os


class Engine(object):

    def __init__(self):
        self.Fdir = ''
        self.ext_src = ''
        self.ext_dst = ''
        self.namesep = '_'

        self.Jdir = ''
        self.Jname = 'FNdata'
        self.Jencode = 'utf-8'
        self.Jpath = JF(self.Jdir, self.Jname, self.Jencode).Jpath
        self.Jindent = 4
        self.Jsort = True

    # generate part
    def genFNJson(self):
        FNList = self.getFNList()
        # clear existing file.
        with open(self.Jpath, 'w', encoding=self.Jencode) as f:
            pass
        self.FNList2J(FNList)

    def getFNList(self):
        FNList = []
        FNList = self.DEIterator(FNList, 'gen')
        return FNList

    def FNList2J(self, FNList):  # store filename dict in a json file
        JFtmp = JF(self.Jdir, self.Jname, self.Jencode)
        JFtmp.writeJson(FNList, self.Jindent, self.Jsort)

    # rename part
    def reJsonFN(self):
        FNList = self.J2FNList()
        FNList = self.DEIterator(FNList, 're')

    def J2FNList(self):  # extract a json file into a dict
        JFtmp = JF(self.Jdir, self.Jname, self.Jencode)
        FNList = JFtmp.readJson()
        return FNList

    # DEIterator part
    def DEIterator(self, FNList, mtd):
        with os.scandir(self.Fdir) as DEit:
            for entry in DEit:
                if entry.is_dir():
                    pass
                elif entry.is_file():
                    (dirname, extension) = os.path.splitext(entry.path)
                    if extension == self.ext_src:
                        FNList = self.JsonFNfun(FNList, entry, mtd)
        return FNList

    def JsonFNfun(self, FNList, entry, mtd):
        if mtd == 'gen':
            FNdict = FN(entry.path, self.namesep).__dict__
            FNList.append(FNdict)
        elif mtd == 're':
            FN_dst = FNList.pop(0)['Name'] + self.ext_dst
            os.rename(entry.path, FN_dst)
        return FNList
