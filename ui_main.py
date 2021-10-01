# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.top_bar.setStyleSheet("background-color: #1A1A1D;")
        self.top_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_menu = QtWidgets.QPushButton(self.top_bar)
        self.btn_menu.setEnabled(True)
        self.btn_menu.setMinimumSize(QtCore.QSize(46, 46))
        self.btn_menu.setMaximumSize(QtCore.QSize(46, 46))
        self.btn_menu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_menu.setStyleSheet("QPushButton {\n"
"    background: none;\n"
"    border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C3073F;\n"
"}\n"
"\n"
"QPUshButton:pressed {\n"
"    background-color: #1A1A1D;\n"
"}")
        self.btn_menu.setText("")
        self.btn_menu.setFlat(True)
        self.btn_menu.setObjectName("btn_menu")
        self.horizontalLayout.addWidget(self.btn_menu)
        spacerItem = QtWidgets.QSpacerItem(720, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.top_bar)
        self.central = QtWidgets.QFrame(self.centralwidget)
        self.central.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.central.setStyleSheet("background-color: #1A1A1D;")
        self.central.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.central.setFrameShadow(QtWidgets.QFrame.Raised)
        self.central.setObjectName("central")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.central)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.menu = QtWidgets.QFrame(self.central)
        self.menu.setMaximumSize(QtCore.QSize(50, 400))
        self.menu.setStyleSheet("background-color: #C3073F;\n"
"border-radius: 10px;")
        self.menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu.setObjectName("menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 244)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_home = QtWidgets.QPushButton(self.menu)
        self.btn_home.setMinimumSize(QtCore.QSize(46, 46))
        self.btn_home.setMaximumSize(QtCore.QSize(46, 46))
        self.btn_home.setStyleSheet("QPushButton {\n"
"    background: none;\n"
"    border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1A1A1D;\n"
"}\n"
"\n"
"QPUshButton:pressed {\n"
"    background-color: #C3073F;\n"
"}")
        self.btn_home.setText("")
        self.btn_home.setObjectName("btn_home")
        self.verticalLayout_2.addWidget(self.btn_home)
        self.btn_profile = QtWidgets.QPushButton(self.menu)
        self.btn_profile.setMinimumSize(QtCore.QSize(46, 46))
        self.btn_profile.setMaximumSize(QtCore.QSize(46, 46))
        self.btn_profile.setStyleSheet("QPushButton {\n"
"    background: none;\n"
"    border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1A1A1D;\n"
"}\n"
"\n"
"QPUshButton:pressed {\n"
"    background-color: #C3073F;\n"
"}")
        self.btn_profile.setText("")
        self.btn_profile.setObjectName("btn_profile")
        self.verticalLayout_2.addWidget(self.btn_profile)
        self.btn_code = QtWidgets.QPushButton(self.menu)
        self.btn_code.setMinimumSize(QtCore.QSize(46, 46))
        self.btn_code.setMaximumSize(QtCore.QSize(46, 46))
        self.btn_code.setStyleSheet("QPushButton {\n"
"    background: none;\n"
"    border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1A1A1D;\n"
"}\n"
"\n"
"QPUshButton:pressed {\n"
"    background-color: #C3073F;\n"
"}")
        self.btn_code.setText("")
        self.btn_code.setObjectName("btn_code")
        self.verticalLayout_2.addWidget(self.btn_code)
        self.horizontalLayout_3.addWidget(self.menu)
        self.content = QtWidgets.QFrame(self.central)
        self.content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.content)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.content)
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.home_page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.home_page)
        self.label_2.setStyleSheet("color: rgb(170, 189, 189);\n"
"font: 48pt \"Tw Cen MT Condensed Extra Bold\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.stackedWidget.addWidget(self.home_page)
        self.profile_page = QtWidgets.QWidget()
        self.profile_page.setObjectName("profile_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.profile_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.profile_page)
        self.label.setStyleSheet("color: rgb(170, 189, 189);\n"
"font: 48pt \"Tw Cen MT Condensed Extra Bold\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.stackedWidget.addWidget(self.profile_page)
        self.code_page = QtWidgets.QWidget()
        self.code_page.setObjectName("code_page")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.code_page)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.nums = QtWidgets.QTextEdit(self.code_page)
        self.nums.setMinimumSize(QtCore.QSize(25, 0))
        self.nums.setMaximumSize(QtCore.QSize(25, 16777215))
        self.nums.setStyleSheet("font: 16pt \"Tw Cen MT Condensed Extra Bold\";\n"
"color: rgb(113, 110, 119);")
        self.nums.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.nums.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.nums.setObjectName("nums")
        self.horizontalLayout_4.addWidget(self.nums)
        self.code = QtWidgets.QTextEdit(self.code_page)
        self.code.setMouseTracking(False)
        self.code.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"Tw Cen MT Condensed Extra Bold\";")
        self.code.setLineWidth(1)
        self.code.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.code.setObjectName("code")
        self.horizontalLayout_4.addWidget(self.code)
        self.stackedWidget.addWidget(self.code_page)
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setObjectName("settings_page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.settings_page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.settings_page)
        self.label_3.setStyleSheet("color: rgb(170, 189, 189);\n"
"font: 48pt \"Tw Cen MT Condensed Extra Bold\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.stackedWidget.addWidget(self.settings_page)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout_3.addWidget(self.content)
        self.verticalLayout.addWidget(self.central)
        self.buttom = QtWidgets.QFrame(self.centralwidget)
        self.buttom.setMaximumSize(QtCore.QSize(16777215, 46))
        self.buttom.setStyleSheet("background-color: #1A1A1D;")
        self.buttom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttom.setObjectName("buttom")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.buttom)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_settings = QtWidgets.QPushButton(self.buttom)
        self.btn_settings.setMinimumSize(QtCore.QSize(46, 46))
        self.btn_settings.setMaximumSize(QtCore.QSize(46, 46))
        self.btn_settings.setStyleSheet("QPushButton {\n"
"    background: none;\n"
"    border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C3073F;\n"
"}\n"
"\n"
"QPUshButton:pressed {\n"
"    background-color: #1A1A1D;\n"
"}")
        self.btn_settings.setText("")
        self.btn_settings.setObjectName("btn_settings")
        self.horizontalLayout_2.addWidget(self.btn_settings)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.buttom)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "HOME PAGE"))
        self.label.setText(_translate("MainWindow", "PROFILE PAGE"))
        self.nums.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tw Cen MT Condensed Extra Bold\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.code.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tw Cen MT Condensed Extra Bold\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "SETTINGS"))