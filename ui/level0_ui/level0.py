import glob
import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QMovie
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QSizePolicy
from .level0_ui import Ui_MainWindow
from PyQt5.QtCore import Qt


class Level0(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.filepath = 'resources/level/level0/'
        self.max_num = len(glob.glob(pathname='{}*.gif'.format(self.filepath)))
        self.num = 0
        self.bell = None
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
        if self.num + 1 < self.max_num:
            self.start_movie()
            self.show()
        elif self.num + 1 == self.max_num:
            self.pushButton.setText("OP Theme")
            self.start_movie()
            self.show()
        else:
            self.pushButton.setVisible(False)
            self.nextButton.setVisible(True)
            # 播放视频
            self.movie = QMovie(self.filepath + str(self.num) + '.gif')
            self.movie_screen.setMovie(self.movie)
            self.movie.start()
            self.show()
            # 播放音乐
            self.bell = QSound('resources/music/level0.wav')
            self.bell.play()

    def stop_bell(self):
        if self.bell is not None:
            self.bell.stop()


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    window = Level0()
    window.show()
    sys.exit(app.exec_())
