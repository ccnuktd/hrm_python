import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QSize, Qt, QCoreApplication
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtWidgets import QTableWidget, QWidget, QLabel, QVBoxLayout, QApplication, QTableWidgetItem

from util.MyUtil import flash


class RegisterItem(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._value = QLabel()
        self._value.setFont(QFont("Arial", 12, QFont.Bold))
        self._value.setAlignment(QtCore.Qt.AlignCenter)
        self._id = QLabel()
        self._id.setFont(QFont("Arial", 8, QFont.Bold))
        self._id.setAlignment(QtCore.Qt.AlignCenter)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(self._id)
        layout.addWidget(self._value)
        layout.setStretchFactor(self._id, 1)
        layout.setStretchFactor(self._value, 3)
        self.setLayout(layout)

    def set_id(self, id):
        self._id.setText(str(id))

    def set_value(self, value):
        self._value.setText(str(value))
        self._value.setStyleSheet("color: rgb(255, 0, 0);")

    def get_value(self):
        return int(self._value.text())


class RegisterTableWidget(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.last_item = None

    def init_ui(self, row_num, col_num, width):
        self.verticalHeader().setVisible(False)  # 隐藏垂直表头
        self.horizontalHeader().setVisible(False)  # 隐藏水平表头
        self.setRowCount(row_num)
        self.setColumnCount(col_num)
        for row in range(row_num):
            self.setRowHeight(row, 4 / 3 * width)
            for i in range(col_num):
                self.setColumnWidth(i, width)
                new_item = RegisterItem()
                new_item.set_id(row * col_num + i)
                self.setCellWidget(row, i, new_item)

    def set_value(self, id, val):
        col_num = self.columnCount()
        cell_item = self.cellWidget(id // col_num, id % col_num)
        cell_item.set_value(str(val))
        self.last_item = cell_item

    def get_value(self, id):
        col_num = self.columnCount()
        cell_item = self.cellWidget(id // col_num, id % col_num)
        self.last_item = cell_item
        return int(cell_item.get_value())

    def display_func(self):
        self.last_item.setStyleSheet("border: 3px solid red;")

    def clear_func(self):
        self.last_item.setStyleSheet("")

    def display_set_value(self, id, val, flash_time):
        self.set_value(id, val)
        flash(self.display_func, self.clear_func, flash_time)
        QCoreApplication.processEvents()

    def display_get_value(self, id, flash_time):
        val = self.get_value(id)
        flash(self.display_func, self.clear_func, flash_time)
        QCoreApplication.processEvents()
        return val

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        # 无法通过点击选中
        self.setCurrentCell(-1, -1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = RegisterTableWidget()
    table.init_ui(2, 5, 60)
    table.set_value(1, 1, 1)
    table.show()
    app.exec_()
