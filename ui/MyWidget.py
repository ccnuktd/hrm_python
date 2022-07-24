import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QVBoxLayout, QHBoxLayout, QListWidget, \
    QListWidgetItem, QAbstractItemView, QInputDialog, QAction, QMessageBox
from PyQt5.QtCore import QSize, Qt, QRect
from PyQt5.QtGui import QFont, QDragMoveEvent
from deprecated.sphinx import deprecated
from MySignal import MySignal
import hrmengine.parser


class OperationWidget(QWidget):
    """operation widget"""

    def __init__(self, *operation):
        super(OperationWidget, self).__init__()
        self._opreation = QLabel(*operation)
        self._opreation.setFont(QFont("Arial", 15, QFont.Bold))
        self._opreation.setAlignment(QtCore.Qt.AlignCenter)
        self.init_ui()

    def get_operation(self):
        return self._opreation.text()

    def init_ui(self):
        layout = QHBoxLayout()
        layout.addWidget(self._opreation)
        self.setLayout(layout)


class OperationDropList(QListWidget):
    """支持拖拽的操作区"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.DragDrop)

        self.signal = MySignal()
        self.init_op()

    def init_op(self):
        list_op = hrmengine.parser.parse_op_list()
        for op in list_op:
            self.add_item(*op)

    def _setItem(self, *operation):
        item_widget = QListWidgetItem()
        item_widget.setSizeHint(QSize(0, 60))

        op = OperationWidget(*operation)
        self.addItem(item_widget)
        self.setItemWidget(item_widget, op)

    def add_item(self, *operation):
        self._setItem(*operation)

    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:
        self.now_row = self.currentRow()
        self.setCurrentRow(-1)
        if self.now_row != -1:
            now_item = self.itemWidget(self.item(self.now_row))
            if now_item != None:
                op = now_item.get_operation()
            # 如果QWidget无法获取，则通过QWidgetItem.text()获取
            else:
                op = self.item(self.now_row).text()
            self.signal.set_item(op)
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e: QtGui.QDropEvent) -> None:
        e.ignore()

    # def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
    #     self.setCurrentRow(-1)


class CodeWidget(QWidget):
    """a widget with code and param"""

    def __init__(self, code_text, param=None):
        """
        :param code_text:
        :param param:
        """
        super(CodeWidget, self).__init__()
        self.check_operation_type(code_text, param)
        self.mouseDoubleClickEvent = self.mouseDoubleClickEvent
        self.setAcceptDrops(True)
        self.init_ui()

    def check_operation_type(self, code_text, param):
        """
        将操作分为三种：0为无参operation，1为带参operation，2为label
        """
        if code_text == "LABEL" or hrmengine.parser.is_label(code_text):
            # label的情况
            self._code_text = QLabel(code_text)
            self._code_text.setFont(QFont("Arial", 10, QFont.Bold))
            self._param = None
            self._state = 2
        elif hrmengine.parser.needs_param(code_text):
            # 带参operation
            self._code_text = QLabel(code_text)
            self._code_text.setFont(QFont("Arial", 10, QFont.Bold))
            # 默认参数为0
            self._param = 0
            self._param = QLabel(param)
            self._code_text.setFont(QFont("Arial", 10, QFont.Bold))
            self._state = 1
        else:
            # 无参operation
            self._code_text = QLabel(code_text)
            self._code_text.setFont(QFont("Arial", 10, QFont.Bold))
            self._param = None
            self._state = 0

    def init_ui(self):
        """handle layout"""
        ly_main = QHBoxLayout()
        if self._state == 1:
            # 有参数的情况
            blank = QLabel()
            ly_main.addWidget(blank)
            ly_main.addWidget(self._code_text)
            ly_main.addWidget(self._param)
            # blank, code和param比例为1:4:1
            ly_main.setStretchFactor(blank, 1)
            ly_main.setStretchFactor(self._code_text, 3)
            ly_main.setStretchFactor(self._param, 1)
        elif self._state == 2:
            # label的情况
            ly_main.addWidget(self._code_text)
        else:
            blank = QLabel()
            ly_main.addWidget(blank)
            ly_main.addWidget(self._code_text)
            # blank, code比例为1:4
            ly_main.setStretchFactor(blank, 1)
            ly_main.setStretchFactor(self._code_text, 4)

        self.setLayout(ly_main)

    def get_code_text(self):
        return self._code_text.text()

    def get_param(self):
        if self._param != None:
            return self._param.text()

    def get_argv(self):
        param = self.get_param()
        if param == None:
            return [self.get_code_text()]
        else:
            return [self.get_code_text(), self.get_param()]

    def mouseDoubleClickEvent(self, event):
        """
        双击修改label和带参语句的参数
        :param event:
        :return:
        """
        if self._state == 1:
            # 修改带参语句的参数
            text, ok = QInputDialog().getText(QWidget(), '修改参数', '输入参数:')
            if ok and text:
                self._param.setText(text)
        elif self._state == 2:
            # 考虑label
            text, ok = QInputDialog().getText(QWidget(), '修改参数', '输入参数:')
            if ok:
                if text.endswith(':'):
                    self._code_text.setText(text)
                else:
                    self._code_text.setText(text + ':')
        else:
            event.ignore()


class CodeDropList(QListWidget):
    """支持拖拽的代码区"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # 拖拽设置
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.DragDrop)  # 设置拖放

        self.init_menu()
        self.last_row = None
        self.slot = MySignal()

    def get_code_list(self):
        code_list = []
        for code in self.get_code():
            code_list.append(code)

        return code_list

    def get_code(self):
        """
        从上到下迭代code widget的code
        """
        for i in range(self.count()):
            item = self.itemWidget(self.item(i))
            item_argv = item.get_argv()
            yield item_argv

    def init_menu(self):
        # 设置允许菜单弹出
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        delete_one = QAction("删除选中", self)
        delete_one.triggered.connect(self._delete)
        delete_all = QAction("删除所有", self)
        delete_all.triggered.connect(self._clear_all)
        self.addAction(delete_one)
        self.addAction(delete_all)

    def _delete(self):
        ok = QMessageBox().question(self, "询问", "是否删除所选的代码块？", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ok:
            self.takeItem(self.currentRow())

    def _clear_all(self):
        ok = QMessageBox().question(self, "询问", "是否删除所有代码？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ok:
            for row in range(self.count() - 1, -1, -1):
                self.takeItem(row)

    def _setItem(self, *argv):
        item_widget = QListWidgetItem()
        item_widget.setSizeHint(QSize(0, 40))

        code = CodeWidget(*argv)
        self.addItem(item_widget)
        self.setItemWidget(item_widget, code)

    def _insertItem(self, pos, *argv):
        item_widget = QListWidgetItem()
        item_widget.setSizeHint(QSize(0, 40))

        code = CodeWidget(*argv)
        self.insertItem(pos, item_widget)
        self.setItemWidget(item_widget, code)

    def insert_item(self, position, *argv):
        self._insertItem(position, *argv)

    def add_item(self, *argv):
        self._setItem(*argv)

    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:
        """进行拖拽的时候最先触发的函数"""
        self.now_row = self.row(self.itemAt(e.pos()))

        op = self.slot.get_item()
        if op != None:
            # print("op:" + op)
            item_argv = ([op])
            # code无内容时的插入
            if self.now_row == -1:
                self.now_row += 1
            self.insert_item(self.now_row, *item_argv)
            # 更新old_item
            self.old_item = self.itemWidget(self.item(self.now_row))
            # 更新currentRow
            if self.currentRow() != self.now_row:
                self.setCurrentRow(self.now_row)

        # 实现鼠标移动拖动块，交换块位置
        if self.last_row != self.currentRow():
            self.last_row = self.currentRow()
            self.old_item = self.itemWidget(self.item(self.last_row))

        e.accept()

    def dragMoveEvent(self, e: QDragMoveEvent):
        """拖拽移动过程中触发的事件"""
        # 鼠标移动拖动块，交换块位置
        if self.now_row != -1 and self.currentRow() != -1:
            # 删除上一个位置的item
            self.takeItem(self.last_row)

            # 插入新的item
            item_argv = self.old_item.get_argv()
            self.insert_item(self.now_row, *item_argv)

            # 更改指针位置
            self.old_item = self.itemWidget(self.item(self.now_row))
            self.last_row = self.now_row
            if self.currentRow() != self.last_row:
                self.setCurrentRow(self.last_row)
        e.accept()

    def dropEvent(self, e: QtGui.QDropEvent) -> None:
        e.ignore()


class OpCodeWidget(QWidget):
    @deprecated(version='1.0', reason="This class will be removed soon")
    def __init__(self, parent=None):
        super().__init__(parent)
        self.opeartion_list = None
        self.code_list = None
        self.setMouseTracking(True)
        self.init_ui()

    def init_ui(self):
        self.resize(835, 865)
        layout_main = QHBoxLayout()

        self.opeartion_list = OperationDropList(self)
        self.opeartion_list.setGeometry(QRect(430, 20, 150, 720))

        self.code_list = CodeDropList(self)
        self.code_list.setGeometry(QRect(620, 20, 150, 600))
        layout_main.addWidget(self.opeartion_list)
        layout_main.addWidget(self.code_list)

        self.setLayout(layout_main)

    def insert_code(self, position, *argv):
        self.code_list.insert_item(position, *argv)

    def add_code(self, *argv):
        self.code_list.add_item(*argv)

    def add_operation(self, *operation):
        self.opeartion_list.add_item(*operation)

    def get_code_list(self):
        code_list = []
        for code in self.code_list.get_code():
            code_list.append(code)

        return code_list


if __name__ == "__main__":
    list_op = hrmengine.parser.parse_op_list()
    file_path = "../resources/demo.txt"
    list_out = hrmengine.parser.parse_file(filepath=file_path)

    app = QApplication(sys.argv)
    main_window = OpCodeWidget()
    # for l in list_out:
    #     main_window.add_code(*l)
    for ll in list_op:
        main_window.add_operation(*ll)
    main_window.show()
    # print(main_window.get_code_list())
    app.exec_()
