# Engine class
# Xu Yi
# 2020

from FileName import FileName as FN
from JsonFile import JsonFile as JF
import os


class Engine(object):

    def __init__(self, Fdir):
        self.Fdir = Fdir
        self.Jdir = Fdir
        self.Jname = 'FNdata'
        self.Jencode = 'utf-8'
        self.Jpath = JF(self.Jdir, self.Jname, self.Jencode).Jpath
        self.Jindent = 4
        self.Jsort = True

    # generate part
    def genFNJson(self, ext, namesep):
        FNList = self.getFNList(ext, namesep)
        # clear existing file.
        with open(self.Jpath, 'w', encoding=self.Jencode) as f:
            pass
        self.FNList2J(FNList)

    def getFNList(self, ext, namesep):
        FNList = []
        with os.scandir(self.Fdir) as DEit:
            for entry in DEit:
                if entry.is_dir():
                    pass
                elif entry.is_file():
                    (dirnameTMP, extension) = os.path.splitext(entry.path)
                    if extension == ext:
                        FNdict = FN(entry.path, namesep).__dict__
                        FNList.append(FNdict)
        return FNList

    def FNList2J(self, FNList):  # store filename dict in a json file
        JFtmp = JF(self.Jdir, self.Jname, self.Jencode)
        JFtmp.writeJson(FNList, self.Jindent, self.Jsort)

    # rename part
    def reJsonFN(self, ext_src, ext_dst, namesep):
        i = 0
        FNList = self.J2FNList()
        with os.scandir(self.Fdir) as DEit:
            for entry in DEit:
                if entry.is_dir():
                    pass
                elif entry.is_file():
                    (dirname, extension) = os.path.splitext(entry.path)
                    if extension == ext_src:
                        FN_dst = FNList[i]['Name'] + ext_dst
                        os.rename(entry.path, FN_dst)
                        i += 1

    def J2FNList(self):  # extract a json file into a dict
        JFtmp = JF(self.Jdir, self.Jname, self.Jencode)
        FNList = JFtmp.readJson()
        return FNList
