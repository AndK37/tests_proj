# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_sceneENHXEC.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
from db import DB
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(979, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.top_menu = QWidget(self.centralwidget)
        self.top_menu.setObjectName(u"top_menu")
        self.top_menu.setStyleSheet(u"background: rgb(217, 195, 169);")
        self.horizontalLayout = QHBoxLayout(self.top_menu)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalSpacer = QSpacerItem(904, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.top_menu)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background: rgb(242, 242, 242);")
        icon = QIcon()
        icon.addFile(u"../res/account_circle_black_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(36, 36))
        

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.top_menu)

        self.down_menu = QWidget(self.centralwidget)
        self.down_menu.setObjectName(u"down_menu")
        self.down_menu.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.down_menu)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QWidget(self.down_menu)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setStyleSheet(u"background: rgb(64, 64, 64);")
        self.verticalLayout = QVBoxLayout(self.left_menu)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.pushButton_2 = QPushButton(self.left_menu)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background: rgb(242, 242, 242);")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.verticalSpacer = QSpacerItem(20, 487, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.left_menu)

        self.right_menu = QWidget(self.down_menu)
        self.right_menu.setObjectName(u"right_menu")
        self.right_menu.setStyleSheet(u"background: rgb(64, 64, 64);")
        self.verticalLayout_2 = QVBoxLayout(self.right_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.stackedWidget = QStackedWidget(self.right_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: rgb(242, 242, 242);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_ln = QLabel(self.widget)
        self.lbl_ln.setObjectName(u"lbl_ln")

        self.gridLayout.addWidget(self.lbl_ln, 0, 0, 1, 1)

        self.lbl_log = QLabel(self.widget)
        self.lbl_log.setObjectName(u"lbl_log")

        self.gridLayout.addWidget(self.lbl_log, 4, 0, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_reg = QPushButton(self.widget_2)
        self.btn_reg.setObjectName(u"btn_reg")
        self.btn_reg.clicked.connect(self.register)

        self.horizontalLayout_3.addWidget(self.btn_reg)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.gridLayout.addWidget(self.widget_2, 7, 0, 1, 2)

        self.lbl_mn = QLabel(self.widget)
        self.lbl_mn.setObjectName(u"lbl_mn")

        self.gridLayout.addWidget(self.lbl_mn, 2, 0, 1, 1)

        self.lineEdit_log = QLineEdit(self.widget)
        self.lineEdit_log.setObjectName(u"lineEdit_log")

        self.gridLayout.addWidget(self.lineEdit_log, 4, 1, 1, 1)

        self.lbl_fn = QLabel(self.widget)
        self.lbl_fn.setObjectName(u"lbl_fn")

        self.gridLayout.addWidget(self.lbl_fn, 1, 0, 1, 1)

        self.lineEdit_fn = QLineEdit(self.widget)
        self.lineEdit_fn.setObjectName(u"lineEdit_fn")

        self.gridLayout.addWidget(self.lineEdit_fn, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 0, 1, 1)

        self.lineEdit_ln = QLineEdit(self.widget)
        self.lineEdit_ln.setObjectName(u"lineEdit_ln")

        self.gridLayout.addWidget(self.lineEdit_ln, 0, 1, 1, 1)

        self.lineEdit_mail = QLineEdit(self.widget)
        self.lineEdit_mail.setObjectName(u"lineEdit_mail")

        self.gridLayout.addWidget(self.lineEdit_mail, 3, 1, 1, 1)

        self.lineEdit_mn = QLineEdit(self.widget)
        self.lineEdit_mn.setObjectName(u"lineEdit_mn")

        self.gridLayout.addWidget(self.lineEdit_mn, 2, 1, 1, 1)

        self.lbl_mail = QLabel(self.widget)
        self.lbl_mail.setObjectName(u"lbl_mail")

        self.gridLayout.addWidget(self.lbl_mail, 3, 0, 1, 1)

        self.lineEdit_pwd = QLineEdit(self.widget)
        self.lineEdit_pwd.setObjectName(u"lineEdit_pwd")

        self.gridLayout.addWidget(self.lineEdit_pwd, 5, 1, 1, 1)

        self.lbl_pwd = QLabel(self.widget)
        self.lbl_pwd.setObjectName(u"lbl_pwd")

        self.gridLayout.addWidget(self.lbl_pwd, 5, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.widget)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_3 = QWidget(self.page_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_3 = QSpacerItem(20, 432, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.lbl_greet = QLabel(self.widget_3)
        self.lbl_greet.setObjectName(u"lbl_greet")
        self.lbl_greet.setStyleSheet(u"font-size: 24pt;")

        self.verticalLayout_5.addWidget(self.lbl_greet)


        self.verticalLayout_6.addWidget(self.widget_3)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.right_menu)


        self.verticalLayout_3.addWidget(self.down_menu)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0442\u0435\u0441\u0442", None))
        self.lbl_ln.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.lbl_log.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.btn_reg.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u0441\u044f", None))
        self.lbl_mn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.lbl_fn.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.lbl_mail.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lbl_pwd.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.lbl_greet.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u041f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi
    def register(self):
        db = DB()
        db.reg(self.lineEdit_ln.text(), self.lineEdit_fn.text(), self.lineEdit_mn.text(), self.lineEdit_mail.text(), self.lineEdit_log.text(), self.lineEdit_pwd.text())
        self.stackedWidget.setCurrentIndex(1)