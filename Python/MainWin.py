# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(456, 453)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(30, 20, 81, 31))
        self.pushButton_1.setObjectName("pushButton_1")
        self.filelistView_1 = QtWidgets.QListView(self.centralwidget)
        self.filelistView_1.setGeometry(QtCore.QRect(30, 70, 181, 192))
        self.filelistView_1.setObjectName("filelistView_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 20, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 20, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 20, 81, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.filelistView_2 = QtWidgets.QListView(self.centralwidget)
        self.filelistView_2.setGeometry(QtCore.QRect(230, 70, 181, 192))
        self.filelistView_2.setObjectName("filelistView_2")
        self.CloseWinBtn = QtWidgets.QPushButton(self.centralwidget)
        self.CloseWinBtn.setGeometry(QtCore.QRect(180, 280, 81, 31))
        self.CloseWinBtn.setObjectName("CloseWinBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 456, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_1.setText(_translate("MainWindow", "find the feature file"))
        self.pushButton_2.setText(_translate("MainWindow", "rename file"))
        self.pushButton_3.setText(_translate("MainWindow", "load json"))
        self.pushButton_4.setText(_translate("MainWindow", "write json"))
        self.CloseWinBtn.setText(_translate("MainWindow", "exit"))
