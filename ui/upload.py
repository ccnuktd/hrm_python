from PyQt5.QtWidgets import QMessageBox, QMainWindow, QWidget

from save.SaveInfo import SaveInfo
from upload_ui import Ui_Form
from util.DbOperation import upload_achieve, check_user


class UploadForm(QWidget, Ui_Form):
    def __init__(self, level_num, code_length, operation_count, set_up):
        super().__init__()
        self.setupUi(self)

        # 绑定槽函数，槽函数需要调用后上传关卡信息
        self.pushButton.clicked.connect(self.register_and_upload)
        self.level_num = level_num
        self.code_length = code_length
        self.operation_count = operation_count
        self.set_up = set_up

    def register_and_upload(self):
        user_name = self.plainTextEdit_name.toPlainText()
        try:
            if user_name:
                if check_user(user_name):
                    QMessageBox.warning(self, 'upload', 'User name already exist!')
                    return
                save_info = SaveInfo()
                save_info.register_user(user_name)
                info = {
                    'user_name': user_name,
                    'level_num': self.level_num,
                    'code_length': self.code_length,
                    'operation_count': self.operation_count
                }
                upload_achieve(info)
                msg_box = QMessageBox(None)
                msg_box.setWindowTitle("upload")
                msg_box.setText("Upload success!")
                next_level = msg_box.addButton("Next Level", QMessageBox.ActionRole)
                msg_box.exec_()
                if msg_box.clickedButton() == next_level:
                    self.set_up.level_up()
            else:
                QMessageBox.warning(None, 'username empty', 'Please input your user name!')
        except:
            QMessageBox.warning(None, 'upload', 'There is some problem about upload.')

        self.close()

    def upload(self):
        save_info = SaveInfo()
        user_name = save_info.get_user()
        try:
            info = {
                'user_name': user_name,
                'level_num': self.level_num,
                'code_length': self.code_length,
                'operation_count': self.operation_count
            }
            upload_achieve(info)
            msg_box = QMessageBox()
            msg_box.setWindowTitle("upload")
            msg_box.setText("Upload success!")
            next_level = msg_box.addButton("Next Level", QMessageBox.ActionRole)
            msg_box.exec_()
            if msg_box.clickedButton() == next_level:
                self.set_up.level_up()
        except Exception:
            raise Exception('upload error')
