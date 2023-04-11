from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

from ranking_ui import Ui_MainWindow

from util.DbOperation import fetch


class Ranking(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.textBrowser_user.setReadOnly(False)
        self.textBrowser_level.setReadOnly(False)
        # 默认显示第一关的数据
        self.textBrowser_level.setText("1")
        self.get_data()
        self.pushButton.clicked.connect(self.get_data)

    def get_data(self):
        user_name = self.textBrowser_user.toPlainText()
        level_num = str(self.textBrowser_level.toPlainText())
        if not level_num.isdigit():
            QMessageBox().information(self, 'search error', 'Please input correct level_num!')
            return
        as_code_length = None
        as_operation_count = None
        if self.code_length_as.isChecked():
            as_code_length = True
        elif self.code_length_de.isChecked():
            as_code_length = False
        else:
            as_code_length = None

        if self.operation_count_as.isChecked():
            as_operation_count = True
        elif self.operation_count_as.isChecked():
            as_operation_count = False
        else:
            as_operation_count = None

        datas = fetch(user_name, level_num, as_code_length, as_operation_count)

        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)

        for data in datas:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)

            self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(level_num)))
            self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(data[0]))
            self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(str(data[1])))
            self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(str(data[2])))


if __name__ == "__main__":
    pass
