from PyQt5.QtWidgets import QMainWindow, QApplication

from GameWindow import GameWindow
from MainWindow import MainWindow
from PyQt5 import QtCore
import sys


class SetUp:
    def __init__(self):
        pass
    # 跳转到主窗口
    def show_main_window(self):
        self.hello = MainWindow()
        self.hello.startButton.clicked.connect(self.show_game_level)
        self.hello.show()
    # 跳转到game窗口, 注意关闭原页面
    def show_game_level(self):
        self.level = GameWindow()
        self.level.show()
        self.hello.close()


if __name__ == '__main__':
    # make the program support high-resolution display
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    window = SetUp()
    window.show_main_window()
    sys.exit(app.exec_())
