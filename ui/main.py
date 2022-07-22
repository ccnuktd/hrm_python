from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QHBoxLayout, QVBoxLayout
from hrm_ui import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
import sys


class Win(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.u_op_droplist.init_op()


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 让程序支持高分辨率显示
    app = QApplication(sys.argv)
    w = Win()
    w.show()
    sys.exit(app.exec_())
