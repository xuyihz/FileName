# FileName class
# Xu Yi
# 2020

from PyQt5 import QtCore, QtGui, QtWidgets
from Engine import Engine as EG


class SignalSlot(object):
    def __init__(self, ViewObj):
        self.ModelObj = EG()
        self.ViewObj = ViewObj
        self.Connect()

    def Connect(self):
        self.ViewObj.pushButton_1.clicked.connect(self.openFile)  # find the feature file
        self.ViewObj.pushButton_2.clicked.connect(self.ModelObj.reJsonFN)  # rename
        self.ViewObj.pushButton_3.clicked.connect(self.loadJson)  # load json
        self.ViewObj.pushButton_4.clicked.connect(self.ModelObj.genFNJson)  # write json        
        self.ViewObj.CloseWinBtn.clicked.connect(self.ViewObj.MainWindow.close)  # exit
        QtCore.QMetaObject.connectSlotsByName(self.ViewObj.MainWindow)

    def openFile(self):
        openfileName, openfileType = QtWidgets.QFileDialog.getOpenFileName(None,'choose a file','','')
        self.ModelObj.Fdir = openfileName
        self.ModelObj.Jdir = self.ModelObj.Fdir
        self.ModelObj.ext_src = openfileType

    def loadJson(self):
        self.ModelObj.FNList = self.ModelObj.J2FNList
