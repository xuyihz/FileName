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
        self.pushButton_dir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dir.setGeometry(QtCore.QRect(30, 20, 81, 31))
        self.pushButton_dir.setObjectName("pushButton_dir")
        self.filelistView_1 = QtWidgets.QListView(self.centralwidget)
        self.filelistView_1.setGeometry(QtCore.QRect(30, 141, 181, 141))
        self.filelistView_1.setObjectName("filelistView_1")
        self.pushButton_rename = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rename.setGeometry(QtCore.QRect(330, 70, 81, 31))
        self.pushButton_rename.setObjectName("pushButton_rename")
        self.pushButton_loadjson = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_loadjson.setGeometry(QtCore.QRect(130, 70, 81, 31))
        self.pushButton_loadjson.setObjectName("pushButton_loadjson")
        self.pushButton_writejson = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_writejson.setGeometry(QtCore.QRect(30, 70, 81, 31))
        self.pushButton_writejson.setObjectName("pushButton_writejson")
        self.filelistView_2 = QtWidgets.QListView(self.centralwidget)
        self.filelistView_2.setGeometry(QtCore.QRect(230, 141, 181, 141))
        self.filelistView_2.setObjectName("filelistView_2")
        self.CloseWinBtn = QtWidgets.QPushButton(self.centralwidget)
        self.CloseWinBtn.setGeometry(QtCore.QRect(30, 300, 381, 31))
        self.CloseWinBtn.setObjectName("CloseWinBtn")
        self.textBrowser_dir = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_dir.setGeometry(QtCore.QRect(130, 20, 281, 31))
        self.textBrowser_dir.setObjectName("textBrowser_dir")
        self.textBrowser_src = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_src.setGeometry(QtCore.QRect(30, 110, 181, 21))
        self.textBrowser_src.setObjectName("textBrowser_src")
        self.textBrowser_des = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_des.setGeometry(QtCore.QRect(230, 110, 181, 21))
        self.textBrowser_des.setObjectName("textBrowser_des")
        self.lineEdit_ext = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ext.setGeometry(QtCore.QRect(230, 70, 81, 31))
        self.lineEdit_ext.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ext.setObjectName("lineEdit_ext")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 456, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_dir.setText(_translate("MainWindow", "find dirpath"))
        self.pushButton_rename.setText(_translate("MainWindow", "rename file"))
        self.pushButton_loadjson.setText(_translate("MainWindow", "load json"))
        self.pushButton_writejson.setText(_translate("MainWindow", "write json"))
        self.CloseWinBtn.setText(_translate("MainWindow", "exit"))
        self.textBrowser_dir.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.textBrowser_src.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">file name (source)</span></p></body></html>"))
        self.textBrowser_des.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">file name (destination)</span></p></body></html>"))
        self.lineEdit_ext.setText(_translate("MainWindow", "ext"))
