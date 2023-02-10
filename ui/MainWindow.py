from PyQt5 import QtCore
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


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
