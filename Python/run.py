# FileName class
# Xu Yi
# 2020

import sys
from PySide2 import QtWidgets
from MainWinCon import Ui_MainWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    View = Ui_MainWindow()                  # ui是Ui_MainWindow()类的实例化对象
    View.setupUi(MainWindow)                # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()                       # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())                    # 使用exit()或者点击关闭按钮退出QApplication
