import glob
import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QMovie
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QSizePolicy
from .level10_5_ui import Ui_MainWindow
from PyQt5.QtCore import Qt


class Level10_5(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.filepath = 'resources/level/level10_5/'
        self.max_num = len(glob.glob(pathname='{}*.gif'.format(self.filepath)))
        self.num = 0
        # 无边框
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.pushButton.clicked.connect(self.next)
        # 隐藏
        self.nextButton.setVisible(False)

        self.centralwidget.setAutoFillBackground(True)
        self.movie_screen = QLabel(self.centralwidget)
        self.movie_screen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.movie_screen.setAlignment(QtCore.Qt.AlignCenter)

        self.movie_screen.setGeometry(QtCore.QRect(25, 50, 755, 300))

    def start_movie(self):
        self.movie = QMovie(self.filepath + str(self.num) + '.gif')
        self.movie_screen.setMovie(self.movie)
        self.movie.start()

    def next(self):
        self.num += 1
        if self.num == self.max_num:
            self.pushButton.setVisible(False)
            self.nextButton.setVisible(True)
        self.start_movie()
        self.show()


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    window = Level10_5()
    window.show()
    sys.exit(app.exec_())
