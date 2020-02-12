# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWin.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(709, 500)
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_dir = QPushButton(self.centralwidget)
        self.pushButton_dir.setObjectName(u"pushButton_dir")
        self.pushButton_dir.setGeometry(QRect(30, 30, 141, 61))
        self.pushButton_dir.setFont(font)
        self.pushButton_rename = QPushButton(self.centralwidget)
        self.pushButton_rename.setObjectName(u"pushButton_rename")
        self.pushButton_rename.setGeometry(QRect(540, 120, 141, 61))
        self.pushButton_rename.setFont(font)
        self.pushButton_loadjson = QPushButton(self.centralwidget)
        self.pushButton_loadjson.setObjectName(u"pushButton_loadjson")
        self.pushButton_loadjson.setGeometry(QRect(200, 120, 141, 61))
        self.pushButton_loadjson.setFont(font)
        self.pushButton_writejson = QPushButton(self.centralwidget)
        self.pushButton_writejson.setObjectName(u"pushButton_writejson")
        self.pushButton_writejson.setGeometry(QRect(30, 120, 141, 61))
        self.pushButton_writejson.setFont(font)
        self.CloseWinBtn = QPushButton(self.centralwidget)
        self.CloseWinBtn.setObjectName(u"CloseWinBtn")
        self.CloseWinBtn.setGeometry(QRect(30, 410, 651, 41))
        self.CloseWinBtn.setFont(font)
        self.textBrowser_dir = QTextBrowser(self.centralwidget)
        self.textBrowser_dir.setObjectName(u"textBrowser_dir")
        self.textBrowser_dir.setGeometry(QRect(200, 30, 481, 61))
        self.textBrowser_dir.setFont(font)
        self.lineEdit_ext = QLineEdit(self.centralwidget)
        self.lineEdit_ext.setObjectName(u"lineEdit_ext")
        self.lineEdit_ext.setGeometry(QRect(370, 120, 141, 61))
        self.lineEdit_ext.setFont(font)
        self.lineEdit_ext.setAlignment(Qt.AlignCenter)
        self.tableView_src = QTableView(self.centralwidget)
        self.tableView_src.setObjectName(u"tableView_src")
        self.tableView_src.setGeometry(QRect(30, 210, 311, 171))
        self.tableView_src.setFont(font)
        self.tableView_dst = QTableView(self.centralwidget)
        self.tableView_dst.setObjectName(u"tableView_dst")
        self.tableView_dst.setGeometry(QRect(370, 210, 311, 171))
        self.tableView_dst.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 709, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Rename File", None))
        self.pushButton_dir.setText(QCoreApplication.translate("MainWindow", u"find dirpath", None))
        self.pushButton_rename.setText(QCoreApplication.translate("MainWindow", u"rename file", None))
        self.pushButton_loadjson.setText(QCoreApplication.translate("MainWindow", u"load json", None))
        self.pushButton_writejson.setText(QCoreApplication.translate("MainWindow", u"write json", None))
        self.CloseWinBtn.setText(QCoreApplication.translate("MainWindow", u"exit", None))
        self.textBrowser_dir.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial','Arial'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:9pt;\"><br /></p></body></html>", None))
        self.lineEdit_ext.setText(QCoreApplication.translate("MainWindow", u"ext", None))
    # retranslateUi

