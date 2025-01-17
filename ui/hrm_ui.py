# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hrm_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 950)
        MainWindow.setMinimumSize(QtCore.QSize(1350, 950))
        MainWindow.setMaximumSize(QtCore.QSize(1350, 950))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.u_code_droplist = CodeDropList(self.centralwidget)
        self.u_code_droplist.setGeometry(QtCore.QRect(1120, 120, 191, 671))
        self.u_code_droplist.setObjectName("u_code_droplist")
        self.u_op_droplist = OperationDropList(self.centralwidget)
        self.u_op_droplist.setGeometry(QtCore.QRect(950, 120, 140, 730))
        self.u_op_droplist.setObjectName("u_op_droplist")
        self.u_input_list = InputListWidget(self.centralwidget)
        self.u_input_list.setGeometry(QtCore.QRect(65, 270, 50, 500))
        self.u_input_list.setObjectName("u_input_list")
        self.u_output_list = OutputListWidget(self.centralwidget)
        self.u_output_list.setGeometry(QtCore.QRect(505, 270, 50, 500))
        self.u_output_list.setObjectName("u_output_list")
        self.u_register_group = RegisterTableWidget(self.centralwidget)
        self.u_register_group.setGeometry(QtCore.QRect(160, 440, 302, 162))
        self.u_register_group.setObjectName("u_register_group")
        self.u_register_group.setColumnCount(0)
        self.u_register_group.setRowCount(0)
        self.u_input_label = QtWidgets.QLabel(self.centralwidget)
        self.u_input_label.setGeometry(QtCore.QRect(70, 240, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.u_input_label.setFont(font)
        self.u_input_label.setObjectName("u_input_label")
        self.u_output_label = QtWidgets.QLabel(self.centralwidget)
        self.u_output_label.setGeometry(QtCore.QRect(510, 240, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.u_output_label.setFont(font)
        self.u_output_label.setObjectName("u_output_label")
        self.u_operation_label = QtWidgets.QLabel(self.centralwidget)
        self.u_operation_label.setGeometry(QtCore.QRect(990, 70, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.u_operation_label.setFont(font)
        self.u_operation_label.setObjectName("u_operation_label")
        self.u_code_label = QtWidgets.QLabel(self.centralwidget)
        self.u_code_label.setGeometry(QtCore.QRect(1180, 70, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.u_code_label.setFont(font)
        self.u_code_label.setObjectName("u_code_label")
        self.u_register_group_label = QtWidgets.QLabel(self.centralwidget)
        self.u_register_group_label.setGeometry(QtCore.QRect(280, 410, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.u_register_group_label.setFont(font)
        self.u_register_group_label.setObjectName("u_register_group_label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(139, 650, 331, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.u_next_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.u_next_btn.setFont(font)
        self.u_next_btn.setObjectName("u_next_btn")
        self.horizontalLayout.addWidget(self.u_next_btn)
        self.u_pause_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.u_pause_btn.setFont(font)
        self.u_pause_btn.setObjectName("u_pause_btn")
        self.horizontalLayout.addWidget(self.u_pause_btn)
        self.u_goon_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.u_goon_btn.setFont(font)
        self.u_goon_btn.setObjectName("u_goon_btn")
        self.horizontalLayout.addWidget(self.u_goon_btn)
        self.u_exit_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.u_exit_btn.setFont(font)
        self.u_exit_btn.setObjectName("u_exit_btn")
        self.horizontalLayout.addWidget(self.u_exit_btn)
        self.u_start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.u_start_btn.setGeometry(QtCore.QRect(1120, 820, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.u_start_btn.setFont(font)
        self.u_start_btn.setObjectName("u_start_btn")
        self.u_speed_slider = QtWidgets.QSlider(self.centralwidget)
        self.u_speed_slider.setGeometry(QtCore.QRect(267, 750, 171, 21))
        self.u_speed_slider.setMinimum(10)
        self.u_speed_slider.setMaximum(50)
        self.u_speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.u_speed_slider.setObjectName("u_speed_slider")
        self.u_speed_label = QtWidgets.QLabel(self.centralwidget)
        self.u_speed_label.setGeometry(QtCore.QRect(170, 750, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.u_speed_label.setFont(font)
        self.u_speed_label.setObjectName("u_speed_label")
        self.u_desc = QtWidgets.QTextBrowser(self.centralwidget)
        self.u_desc.setGeometry(QtCore.QRect(174, 80, 281, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.u_desc.setFont(font)
        self.u_desc.setObjectName("u_desc")
        self.stackedWidget = SlidingStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(620, 150, 291, 101))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(740, 270, 171, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonPrev = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButtonPrev.setObjectName("pushButtonPrev")
        self.horizontalLayout_2.addWidget(self.pushButtonPrev)
        self.pushButtonNext = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButtonNext.setEnabled(True)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout_2.addWidget(self.pushButtonNext)
        self.u_pointer_label = QtWidgets.QLabel(self.centralwidget)
        self.u_pointer_label.setGeometry(QtCore.QRect(294, 300, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.u_pointer_label.setFont(font)
        self.u_pointer_label.setObjectName("u_pointer_label")
        self.u_pointer = Pointer(self.centralwidget)
        self.u_pointer.setGeometry(QtCore.QRect(274, 320, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.u_pointer.setFont(font)
        self.u_pointer.setObjectName("u_pointer")
        self.bgmButton = QtWidgets.QPushButton(self.centralwidget)
        self.bgmButton.setGeometry(QtCore.QRect(70, 120, 42, 42))
        self.bgmButton.setText("")
        self.bgmButton.setObjectName("bgmButton")
        self.u_bgm_label = QtWidgets.QLabel(self.centralwidget)
        self.u_bgm_label.setGeometry(QtCore.QRect(80, 80, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.u_bgm_label.setFont(font)
        self.u_bgm_label.setObjectName("u_bgm_label")
        self.u_input_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.u_input_label_2.setGeometry(QtCore.QRect(250, 230, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        self.u_input_label_2.setFont(font)
        self.u_input_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.u_input_label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.u_input_label_2.setObjectName("u_input_label_2")
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_1.setGeometry(QtCore.QRect(40, 50, 540, 1))
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 800, 540, 1))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(40, 50, 1, 750))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(580, 50, 1, 750))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.u_story = QtWidgets.QLabel(self.centralwidget)
        self.u_story.setGeometry(QtCore.QRect(740, 110, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.u_story.setFont(font)
        self.u_story.setObjectName("u_story")
        self.u_story_2 = QtWidgets.QLabel(self.centralwidget)
        self.u_story_2.setGeometry(QtCore.QRect(700, 350, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.u_story_2.setFont(font)
        self.u_story_2.setObjectName("u_story_2")
        self.pushButton_inbox = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_inbox.setGeometry(QtCore.QRect(654, 400, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_inbox.setFont(font)
        self.pushButton_inbox.setObjectName("pushButton_inbox")
        self.pushButton_outbox = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_outbox.setGeometry(QtCore.QRect(780, 400, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_outbox.setFont(font)
        self.pushButton_outbox.setObjectName("pushButton_outbox")
        self.pushButton_label = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_label.setGeometry(QtCore.QRect(654, 450, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_label.setFont(font)
        self.pushButton_label.setObjectName("pushButton_label")
        self.pushButton_jump = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_jump.setGeometry(QtCore.QRect(780, 450, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_jump.setFont(font)
        self.pushButton_jump.setObjectName("pushButton_jump")
        self.pushButton_copyfrom = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_copyfrom.setGeometry(QtCore.QRect(654, 500, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_copyfrom.setFont(font)
        self.pushButton_copyfrom.setObjectName("pushButton_copyfrom")
        self.pushButton_copyto = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_copyto.setGeometry(QtCore.QRect(780, 500, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_copyto.setFont(font)
        self.pushButton_copyto.setObjectName("pushButton_copyto")
        self.pushButton_jumpz = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_jumpz.setGeometry(QtCore.QRect(654, 550, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_jumpz.setFont(font)
        self.pushButton_jumpz.setObjectName("pushButton_jumpz")
        self.pushButton_jumpn = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_jumpn.setGeometry(QtCore.QRect(780, 550, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_jumpn.setFont(font)
        self.pushButton_jumpn.setObjectName("pushButton_jumpn")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(654, 600, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_sub = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sub.setGeometry(QtCore.QRect(780, 600, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_sub.setFont(font)
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.pushButton_bumpup = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_bumpup.setGeometry(QtCore.QRect(654, 650, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_bumpup.setFont(font)
        self.pushButton_bumpup.setObjectName("pushButton_bumpup")
        self.pushButton_bumpdown = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_bumpdown.setGeometry(QtCore.QRect(780, 650, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_bumpdown.setFont(font)
        self.pushButton_bumpdown.setObjectName("pushButton_bumpdown")
        self.code_desc_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.code_desc_browser.setGeometry(QtCore.QRect(640, 710, 256, 121))
        self.code_desc_browser.setObjectName("code_desc_browser")
        self.u_story_3 = QtWidgets.QLabel(self.centralwidget)
        self.u_story_3.setGeometry(QtCore.QRect(620, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.u_story_3.setFont(font)
        self.u_story_3.setObjectName("u_story_3")
        self.user_name_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.user_name_browser.setGeometry(QtCore.QRect(700, 40, 191, 41))
        self.user_name_browser.setObjectName("user_name_browser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1350, 23))
        self.menubar.setObjectName("menubar")
        self.menulevel = QtWidgets.QMenu(self.menubar)
        self.menulevel.setObjectName("menulevel")
        self.menuranking = QtWidgets.QMenu(self.menubar)
        self.menuranking.setObjectName("menuranking")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionlevel1 = QtWidgets.QAction(MainWindow)
        self.actionlevel1.setObjectName("actionlevel1")
        self.actionlevel2 = QtWidgets.QAction(MainWindow)
        self.actionlevel2.setObjectName("actionlevel2")
        self.actionlevel3 = QtWidgets.QAction(MainWindow)
        self.actionlevel3.setObjectName("actionlevel3")
        self.actionlevel4 = QtWidgets.QAction(MainWindow)
        self.actionlevel4.setObjectName("actionlevel4")
        self.actionlevel5 = QtWidgets.QAction(MainWindow)
        self.actionlevel5.setObjectName("actionlevel5")
        self.actionlevel6 = QtWidgets.QAction(MainWindow)
        self.actionlevel6.setObjectName("actionlevel6")
        self.actionlevel7 = QtWidgets.QAction(MainWindow)
        self.actionlevel7.setObjectName("actionlevel7")
        self.actionlevel8 = QtWidgets.QAction(MainWindow)
        self.actionlevel8.setObjectName("actionlevel8")
        self.actionlevel9 = QtWidgets.QAction(MainWindow)
        self.actionlevel9.setObjectName("actionlevel9")
        self.actionlevel10 = QtWidgets.QAction(MainWindow)
        self.actionlevel10.setObjectName("actionlevel10")
        self.actionlevel11 = QtWidgets.QAction(MainWindow)
        self.actionlevel11.setObjectName("actionlevel11")
        self.actionlevel12 = QtWidgets.QAction(MainWindow)
        self.actionlevel12.setObjectName("actionlevel12")
        self.actionlevel13 = QtWidgets.QAction(MainWindow)
        self.actionlevel13.setObjectName("actionlevel13")
        self.actionmain_screen = QtWidgets.QAction(MainWindow)
        self.actionmain_screen.setObjectName("actionmain_screen")
        self.actionranking_list = QtWidgets.QAction(MainWindow)
        self.actionranking_list.setObjectName("actionranking_list")
        self.menulevel.addAction(self.actionmain_screen)
        self.menuranking.addAction(self.actionranking_list)
        self.menubar.addAction(self.menulevel.menuAction())
        self.menubar.addAction(self.menuranking.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.u_input_label.setText(_translate("MainWindow", "inbox"))
        self.u_output_label.setText(_translate("MainWindow", "outbox"))
        self.u_operation_label.setText(_translate("MainWindow", "op box"))
        self.u_code_label.setText(_translate("MainWindow", "code box"))
        self.u_register_group_label.setText(_translate("MainWindow", "register"))
        self.u_next_btn.setText(_translate("MainWindow", "next"))
        self.u_pause_btn.setText(_translate("MainWindow", "stop"))
        self.u_goon_btn.setText(_translate("MainWindow", "go on"))
        self.u_exit_btn.setText(_translate("MainWindow", "terminate"))
        self.u_start_btn.setText(_translate("MainWindow", "start"))
        self.u_speed_label.setText(_translate("MainWindow", "flash speed"))
        self.u_desc.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt;\"><br /></p></body></html>"))
        self.pushButtonPrev.setText(_translate("MainWindow", "Prev"))
        self.pushButtonNext.setText(_translate("MainWindow", "Next"))
        self.u_pointer_label.setText(_translate("MainWindow", "bus"))
        self.u_pointer.setText(_translate("MainWindow", "None"))
        self.u_bgm_label.setText(_translate("MainWindow", "bgm"))
        self.u_input_label_2.setText(_translate("MainWindow", "HRM"))
        self.u_story.setText(_translate("MainWindow", "story"))
        self.u_story_2.setText(_translate("MainWindow", "operation instruction"))
        self.pushButton_inbox.setText(_translate("MainWindow", "?"))
        self.pushButton_outbox.setText(_translate("MainWindow", "?"))
        self.pushButton_label.setText(_translate("MainWindow", "?"))
        self.pushButton_jump.setText(_translate("MainWindow", "?"))
        self.pushButton_copyfrom.setText(_translate("MainWindow", "?"))
        self.pushButton_copyto.setText(_translate("MainWindow", "?"))
        self.pushButton_jumpz.setText(_translate("MainWindow", "?"))
        self.pushButton_jumpn.setText(_translate("MainWindow", "?"))
        self.pushButton_add.setText(_translate("MainWindow", "?"))
        self.pushButton_sub.setText(_translate("MainWindow", "?"))
        self.pushButton_bumpup.setText(_translate("MainWindow", "?"))
        self.pushButton_bumpdown.setText(_translate("MainWindow", "?"))
        self.u_story_3.setText(_translate("MainWindow", "user_name"))
        self.menulevel.setTitle(_translate("MainWindow", "level"))
        self.menuranking.setTitle(_translate("MainWindow", "ranking"))
        self.actionlevel1.setText(_translate("MainWindow", "level1"))
        self.actionlevel2.setText(_translate("MainWindow", "level2"))
        self.actionlevel3.setText(_translate("MainWindow", "level3"))
        self.actionlevel4.setText(_translate("MainWindow", "level4"))
        self.actionlevel5.setText(_translate("MainWindow", "level5"))
        self.actionlevel6.setText(_translate("MainWindow", "level6"))
        self.actionlevel7.setText(_translate("MainWindow", "level7"))
        self.actionlevel8.setText(_translate("MainWindow", "level8"))
        self.actionlevel9.setText(_translate("MainWindow", "level9"))
        self.actionlevel10.setText(_translate("MainWindow", "level10"))
        self.actionlevel11.setText(_translate("MainWindow", "level11"))
        self.actionlevel12.setText(_translate("MainWindow", "level12"))
        self.actionlevel13.setText(_translate("MainWindow", "level13"))
        self.actionmain_screen.setText(_translate("MainWindow", "main screen"))
        self.actionranking_list.setText(_translate("MainWindow", "ranking list"))
from CodeOpListWidget import CodeDropList, OperationDropList
from IOListWidget import InputListWidget, OutputListWidget
from Pointer import Pointer
from RegisterTableWidget import RegisterTableWidget
from lib.SlidingStackedWidget import SlidingStackedWidget
