# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets
from MainWin import Ui_MainWindow as MWU
from Engine import Engine
import os


class Ui_MainWindow(MWU):
    def __init__(self):
        self.ModelObj = Engine()

    def setupUi(self, MainWindow):
        super(Ui_MainWindow, self).setupUi(MainWindow)
        self.ModelObj.ext_dst = self.lineEdit_ext.text()

        self.pushButton_dir.clicked.connect(
            self.openFile)  # find the feature file
        self.pushButton_rename.clicked.connect(self.renameFile)  # rename
        self.pushButton_loadjson.clicked.connect(self.loadJson)  # load json
        self.pushButton_writejson.clicked.connect(
            self.ModelObj.genFNJson)  # write json
        self.CloseWinBtn.clicked.connect(MainWindow.close)  # exit

        self.lineEdit_ext.editingFinished.connect(self.changeExtDst)

    def openFile(self):
        openfileName, openfileType = QtWidgets.QFileDialog.getOpenFileName(
            None, 'choose a file', '', '')
        self.ModelObj.Fdir = os.path.dirname(openfileName)
        self.ModelObj.Jdir = self.ModelObj.Fdir
        self.textBrowser_dir.setText(self.ModelObj.Fdir)

        basename = os.path.basename(openfileName)
        (Name, Extension) = os.path.splitext(basename)
        self.ModelObj.ext_src = Extension
        self.ModelObj.ext_dst = Extension  # assume ext_dst == ext_src
        self.lineEdit_ext.setText(self.ModelObj.ext_dst[1:])

        FNList = self.ModelObj.getFNList()
        self.FileNameTable(self.tableView_src, FNList,
                           self.ModelObj.ext_src, 'src Name')

    def loadJson(self):
        self.ModelObj.FNList = self.ModelObj.J2FNList()
        self.FileNameTable(self.tableView_dst, self.ModelObj.FNList,
                           self.ModelObj.ext_dst, 'dst Name')

    def renameFile(self):
        self.ModelObj.reJsonFN()

    def changeExtDst(self):
        self.ModelObj.ext_dst = '.' + self.lineEdit_ext.text()  # get the text from lineEdit
        self.FileNameTable(self.tableView_dst, self.ModelObj.FNList,
                           self.ModelObj.ext_dst, 'dst Name')

    def FileNameTable(self, TableView, FNList, ext, Header):
        # create Model
        self.IM = QtGui.QStandardItemModel()
        # set Horizontal Header
        self.IM.setHorizontalHeaderItem(0, QtGui.QStandardItem(Header))
        # set Item
        for i in range(len(FNList)):
            self.IM.setItem(i, QtGui.QStandardItem(FNList[i]['Name']+ext))
        # sort
        # self.IM.sort(1, QtCore.Qt.DescendingOrder)
        # set Model
        TableView.setModel(self.IM)
        # set Section ResizeMode(Stretch)
        TableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
