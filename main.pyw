import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainWindowA import *
import win32gui

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        ahwnd = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
        ascreen = QApplication.primaryScreen()
        aimg = ascreen.grabWindow(ahwnd).toImage()
        # aimg.save("screenshot.jpg")
        print("good")
        desktop = QApplication.desktop()
        print("屏幕宽:" + str(desktop.width()))
        print("屏幕高:" + str(desktop.height()))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(desktop.width(),desktop.height()) #emmm
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, desktop.width(), desktop.height()))
        self.label.setObjectName("label")
        self.label.setPixmap(QPixmap.fromImage(aimg))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    hwnd = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(hwnd).toImage()
    myWin = MyWindow()
    myWin.showFullScreen()
    sys.exit(app.exec_())