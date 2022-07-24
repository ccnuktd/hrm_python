from time import sleep

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QSize, QCoreApplication, QTimer, QTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QWidget, QLabel, QHBoxLayout
from util.MyUtil import read_file

class IOBlockWidget(QWidget):
    """inbox outbox block"""
    def __init__(self, number):
        super(IOBlockWidget, self).__init__()
        self._number = QLabel(str(number))
        self._number.setFont(QFont("Arial", 10, QFont.Black))
        self._number.setAlignment(QtCore.Qt.AlignCenter)
        self.init_ui()

    def get_number(self):
        return int(self._number.text())

    def init_ui(self):
        layout = QHBoxLayout()
        layout.addWidget(self._number)
        self.setLayout(layout)


class InputListWidget(QListWidget):
    """UI input list widget"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(False)
        self.setDragEnabled(False)

    def _setItem(self, number):
        item_widget = QListWidgetItem()
        item_widget.setSizeHint(QSize(0, 50))

        op = IOBlockWidget(number)
        self.addItem(item_widget)
        self.setItemWidget(item_widget, op)

    def add_item(self, number):
        self._setItem(number)

    def init_inbox(self, input_list):
        # 从某个地方获取input list内容
        for input in input_list:
            self.add_item(int(input))

    def on_activate(self, flash_time):
        # 选中队首元素，并使其闪烁4次
        timer = QTime()
        timer.start()
        flash_num = 1
        while timer.elapsed() < flash_time:
            if timer.elapsed() > flash_time * flash_num / 4:
                if self.currentRow() == -1:
                    self.setCurrentRow(0)
                else:
                    self.setCurrentRow(-1)
                flash_num += 1
            # 保持事件循环的继续运行
            QCoreApplication.processEvents()
        else:
            # 保证最后一次不会选中
            self.setCurrentRow(-1)
        # 删除队首元素
        self.takeItem(0)

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        self.setCurrentRow(-1)
        e.ignore()

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        self.setCurrentRow(-1)
        e.ignore()

    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:
        self.setCurrentRow(-1)
        e.ignore()


if __name__ == "__main__":
    # ops = parse_file(filepath)
    # inbox = iter([1, 5])
    # state = cpu.create_state(inbox, ops)
    #
    # next_state = cpu.tick(state)
    # while next_state.pc != -1:
    #     next_state = cpu.tick(next_state)
    #
    # print("OUTBOX:", next_state.outbox)
    pass
