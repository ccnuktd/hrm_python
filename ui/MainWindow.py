from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication
from MainWindow_ui import Ui_MainWindow
from PyQt5.QtCore import Qt
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 无边框
        self.setWindowFlag(Qt.FramelessWindowHint)
        # self.resolution_adaptation()

    def resolution_adaptation(self):
        # 分辨率字体适配
        self.app = QApplication.instance()  # Calculate the ratio. Design screen is [3200, 2000]
        screen_resolution = self.app.desktop().screenGeometry()
        if screen_resolution.width() != 3200 or screen_resolution.height() == 2000:
            font = QFont()
            font.setFamily('SimSun')
            font.setPointSize(9)
            font.setWeight(400)
            self.startButton.setFont(font)
            self.restartButton.setFont(font)
            self.exitButton.setFont(font)

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
