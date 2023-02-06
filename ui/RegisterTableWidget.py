import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QTableWidget, QWidget, QLabel, QVBoxLayout, QApplication

from util.MyUtil import flash


class RegisterItem(QWidget):
    """each register in register group"""
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
        return self._value.text()


class RegisterTableWidget(QTableWidget):
    """register group"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.last_item = None

    def init_ui(self, row_num, col_num, width):
        self.clear()
        self.verticalHeader().setVisible(False)  # Hide vertical headers
        self.horizontalHeader().setVisible(False)  # Hide horizontal headers
        self.setRowCount(row_num)
        self.setColumnCount(col_num)
        for row in range(row_num):
            # register's h:w = 4:3
            self.setRowHeight(row, 4 * width // 3)
            for i in range(col_num):
                self.setColumnWidth(i, width)
                new_item = RegisterItem()
                new_item.set_id(row * col_num + i)
                self.setCellWidget(row, i, new_item)

    def set_value(self, id, val):
        """use id to set value"""
        col_num = self.columnCount()
        cell_item = self.cellWidget(id // col_num, id % col_num)
        cell_item.set_value(str(val))
        self.last_item = cell_item

    def get_value(self, id):
        """use id to get value"""
        col_num = self.columnCount()
        cell_item = self.cellWidget(id // col_num, id % col_num)
        self.last_item = cell_item
        return cell_item.get_value()

    def _display_func(self):
        self.last_item.setStyleSheet("border: 1px solid red;")

    def _clear_func(self):
        self.last_item.setStyleSheet("")

    def display_set_value(self, id, val, flash_time):
        """set value animation"""
        self.set_value(id, val)
        flash(self._display_func, self._clear_func, flash_time)
        QCoreApplication.processEvents()

    def display_get_value(self, id, flash_time):
        """get value animation"""
        val = self.get_value(id)
        flash(self._display_func, self._clear_func, flash_time)
        QCoreApplication.processEvents()
        return val

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        # disable selected
        self.setCurrentCell(-1, -1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = RegisterTableWidget()
    table.init_ui(2, 5, 60)
    table.set_value(1, 1)
    table.show()
    app.exec_()
