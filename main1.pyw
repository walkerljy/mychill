import random
import PIL.Image
import PIL.ImageQt
from mainWindowA import *

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication

global wholeDeskWidth
global wholeDeskHeight
sys.path.append(r'pathname')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        print("good")
        desktop = QApplication.desktop()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(desktop.width(), desktop.height())
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
        self.label.setPixmap(QPixmap.fromImage(img))
        MainWindow.setCentralWidget(self.centralwidget)

        global wholeDeskWidth, wholeDeskHeight
        wholeDeskWidth = self.deskWidth()
        wholeDeskHeight = self.deskHeight()

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 初始化一个定时器
        self.timer = QTimer(self)
        # 定义时间超时连接start_app
        self.timer.timeout.connect(self.start)
        # 定义时间任务是一次性任务
        self.timer.setSingleShot(True)
        # 启动时间任务
        self.timer.start()
        # 实例化一个线程
        self.work = WorkThread()
        # 多线程的信号触发连接到UpText
        # noinspection PyUnresolvedReferences
        self.work.trigger.connect(self.UpImage)

    def deskWidth(self):
        return self.label.width()

    def deskHeight(self):
        return self.label.height()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def start(self):
        self.work.start()

    def UpImage(self, img):
        self.label.setPixmap(img)


class WorkThread(QThread):
    # 定义一个信号
    trigger = pyqtSignal(QPixmap)

    def __int__(self):
        # 初始化函数，默认
        super(WorkThread, self).__init__()

    def pil2_pixmap(self, pil_img):
        # print("PIL格式转QPixmap格式")
        pil_img.save(r"./1.png")
        global wholeDeskWidth, wholeDeskHeight
        pixmap = QPixmap(r"./1.png").scaled(wholeDeskWidth, wholeDeskHeight)
        return pixmap

    def run(self):
        pilimg = PIL.ImageQt.fromqimage(img)
        errimga = pilimg
        errorimg = PIL.Image.open(r"png/vbs.png")
        global wholeDeskWidth, wholeDeskHeight
        p = 100
        while p > 0:
            errimga.paste(errorimg, (random.randint(1, wholeDeskWidth - 520), random.randint(1, wholeDeskHeight - 95)))
            # noinspection PyUnresolvedReferences
            self.trigger.emit(self.pil2_pixmap(errimga))
            p = p - 1


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    hwnd = win32gui.FindWindow(None, 'C:\zhe_ge_cheng_xu_bu_cun_zai.exe')
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(hwnd).toImage()
    myWin = MyWindow()
    myWin.showFullScreen()
    sys.exit(app.exec_())
