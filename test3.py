from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import win32gui
import sys

desktop = QApplication.desktop()
print("屏幕宽:" + str(desktop.width()))
print("屏幕高:" + str(desktop.height()))