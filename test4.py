from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('动画学习')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton('测试按钮',self)
        btn.move(100,100)
        btn.resize(200,200)
        btn.setStyleSheet('background-color: cyan;')

        # 1.创建一个动画对象，并且设置目标 属性

        # 有两种方式
        # 法一
        animation = QPropertyAnimation(self)
        animation.setTargetObject(btn)  # 设置动画对象
        animation.setPropertyName(b"pos")  # b代表字节；pos代表位置
        #法二
        # animation = QPropertyAnimation(btn, b'geometry',self)

        # 2.设置属性值： 开始 插值 结束
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(300, 300))

        # 3.动画时长
        animation.setDuration(3000)  # 时长单位毫秒

        animation.setEasingCurve(QEasingCurve.OutBounce)  # setEasingCurve动画曲线

        # 4.启东动画
        animation.start()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())
