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
        MainWindow.resize(456, 453)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_dir = QPushButton(self.centralwidget)
        self.pushButton_dir.setObjectName(u"pushButton_dir")
        self.pushButton_dir.setGeometry(QRect(30, 20, 81, 31))
        self.pushButton_rename = QPushButton(self.centralwidget)
        self.pushButton_rename.setObjectName(u"pushButton_rename")
        self.pushButton_rename.setGeometry(QRect(330, 70, 81, 31))
        self.pushButton_loadjson = QPushButton(self.centralwidget)
        self.pushButton_loadjson.setObjectName(u"pushButton_loadjson")
        self.pushButton_loadjson.setGeometry(QRect(130, 70, 81, 31))
        self.pushButton_writejson = QPushButton(self.centralwidget)
        self.pushButton_writejson.setObjectName(u"pushButton_writejson")
        self.pushButton_writejson.setGeometry(QRect(30, 70, 81, 31))
        self.CloseWinBtn = QPushButton(self.centralwidget)
        self.CloseWinBtn.setObjectName(u"CloseWinBtn")
        self.CloseWinBtn.setGeometry(QRect(30, 300, 381, 31))
        self.textBrowser_dir = QTextBrowser(self.centralwidget)
        self.textBrowser_dir.setObjectName(u"textBrowser_dir")
        self.textBrowser_dir.setGeometry(QRect(130, 20, 281, 31))
        self.textBrowser_src = QTextBrowser(self.centralwidget)
        self.textBrowser_src.setObjectName(u"textBrowser_src")
        self.textBrowser_src.setGeometry(QRect(30, 110, 181, 21))
        self.textBrowser_dst = QTextBrowser(self.centralwidget)
        self.textBrowser_dst.setObjectName(u"textBrowser_dst")
        self.textBrowser_dst.setGeometry(QRect(230, 110, 181, 21))
        self.lineEdit_ext = QLineEdit(self.centralwidget)
        self.lineEdit_ext.setObjectName(u"lineEdit_ext")
        self.lineEdit_ext.setGeometry(QRect(230, 70, 81, 31))
        self.lineEdit_ext.setAlignment(Qt.AlignCenter)
        self.tableView_src = QTableView(self.centralwidget)
        self.tableView_src.setObjectName(u"tableView_src")
        self.tableView_src.setGeometry(QRect(30, 140, 181, 141))
        self.tableView_dst = QTableView(self.centralwidget)
        self.tableView_dst.setObjectName(u"tableView_dst")
        self.tableView_dst.setGeometry(QRect(230, 140, 181, 141))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 456, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_dir.setText(QCoreApplication.translate("MainWindow", u"find dirpath", None))
        self.pushButton_rename.setText(QCoreApplication.translate("MainWindow", u"rename file", None))
        self.pushButton_loadjson.setText(QCoreApplication.translate("MainWindow", u"load json", None))
        self.pushButton_writejson.setText(QCoreApplication.translate("MainWindow", u"write json", None))
        self.CloseWinBtn.setText(QCoreApplication.translate("MainWindow", u"exit", None))
        self.textBrowser_dir.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textBrowser_src.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">file name (source)</p></body></html>", None))
        self.textBrowser_dst.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">file name (destination)</p></body></html>", None))
        self.lineEdit_ext.setText(QCoreApplication.translate("MainWindow", u"ext", None))
    # retranslateUi

