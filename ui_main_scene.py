# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_scenejlzOpX.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QAction)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget, QMenu, QFileDialog)
from db import DB
import re
from smtp import Mail

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(979, 653)
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

        self.btn_tm_account = QPushButton(self.top_menu)
        self.btn_tm_account.setObjectName(u"btn_tm_account")
        self.btn_tm_account.setStyleSheet(u"background: rgb(242, 242, 242);")
        icon = QIcon()
        icon.addFile(u"./res/account_circle_black_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_tm_account.setIcon(icon)
        self.btn_tm_account.setIconSize(QSize(36, 36))
    
        self.menu_acc = QMenu()
        self.menu_acc.addAction('Войти', self.menu_log)
        self.menu_acc.addAction('Регистрация', self.menu_reg)
        self.btn_tm_account.setMenu(self.menu_acc)

        self.horizontalLayout.addWidget(self.btn_tm_account)

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
        self.btn_lm_ct = QPushButton(self.left_menu)
        self.btn_lm_ct.setObjectName(u"btn_lm_ct")
        self.btn_lm_ct.setStyleSheet(u"background: rgb(242, 242, 242);")
        self.btn_lm_ct.clicked.connect(self.page_ct)

        self.verticalLayout.addWidget(self.btn_lm_ct)

        self.btn_lm_mt = QPushButton(self.left_menu)
        self.btn_lm_mt.setObjectName(u"btn_lm_mt")
        self.btn_lm_mt.setStyleSheet(u"background: rgb(242, 242, 242);")
        self.btn_lm_mt.clicked.connect(self.page_mt)

        self.verticalLayout.addWidget(self.btn_lm_mt)

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
        self.greet = QWidget()
        self.greet.setObjectName(u"greet")
        self.verticalLayout_7 = QVBoxLayout(self.greet)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_2 = QWidget(self.greet)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_4 = QSpacerItem(20, 464, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.lbl_greet = QLabel(self.widget_2)
        self.lbl_greet.setObjectName(u"lbl_greet")
        self.lbl_greet.setStyleSheet(u"font-size: 48px;")

        self.verticalLayout_6.addWidget(self.lbl_greet)


        self.verticalLayout_7.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.greet)
        self.registration = QWidget()
        self.registration.setObjectName(u"registration")
        self.verticalLayout_4 = QVBoxLayout(self.registration)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget = QWidget(self.registration)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_r_ln = QLabel(self.widget)
        self.lbl_r_ln.setObjectName(u"lbl_r_ln")

        self.gridLayout.addWidget(self.lbl_r_ln, 1, 0, 1, 1)

        self.lbl_r_fn = QLabel(self.widget)
        self.lbl_r_fn.setObjectName(u"lbl_r_fn")

        self.gridLayout.addWidget(self.lbl_r_fn, 2, 0, 1, 1)

        self.le_r_fn = QLineEdit(self.widget)
        self.le_r_fn.setObjectName(u"le_r_fn")

        self.gridLayout.addWidget(self.le_r_fn, 2, 1, 1, 1)

        self.le_r_mn = QLineEdit(self.widget)
        self.le_r_mn.setObjectName(u"le_r_mn")

        self.gridLayout.addWidget(self.le_r_mn, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.lbl_r_mail = QLabel(self.widget)
        self.lbl_r_mail.setObjectName(u"lbl_r_mail")

        self.gridLayout.addWidget(self.lbl_r_mail, 4, 0, 1, 1)

        self.lbl_r_log = QLabel(self.widget)
        self.lbl_r_log.setObjectName(u"lbl_r_log")

        self.gridLayout.addWidget(self.lbl_r_log, 5, 0, 1, 1)

        self.le_r_mail = QLineEdit(self.widget)
        self.le_r_mail.setObjectName(u"le_r_mail")

        self.gridLayout.addWidget(self.le_r_mail, 4, 1, 1, 1)

        self.btn_reg = QPushButton(self.widget)
        self.btn_reg.setObjectName(u"btn_reg")
        self.btn_reg.clicked.connect(self.login_from_reg)

        self.gridLayout.addWidget(self.btn_reg, 8, 0, 1, 1)

        self.lbl_r_mn = QLabel(self.widget)
        self.lbl_r_mn.setObjectName(u"lbl_r_mn")

        self.gridLayout.addWidget(self.lbl_r_mn, 3, 0, 1, 1)

        self.le_r_ln = QLineEdit(self.widget)
        self.le_r_ln.setObjectName(u"le_r_ln")

        self.gridLayout.addWidget(self.le_r_ln, 1, 1, 1, 1)

        self.le_r_pwd = QLineEdit(self.widget)
        self.le_r_pwd.setObjectName(u"le_r_pwd")

        self.gridLayout.addWidget(self.le_r_pwd, 6, 1, 1, 1)

        self.lbl_r_pwd = QLabel(self.widget)
        self.lbl_r_pwd.setObjectName(u"lbl_r_pwd")

        self.gridLayout.addWidget(self.lbl_r_pwd, 6, 0, 1, 1)

        self.le_r_log = QLineEdit(self.widget)
        self.le_r_log.setObjectName(u"le_r_log")

        self.gridLayout.addWidget(self.le_r_log, 5, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.lbl_registration = QLabel(self.widget)
        self.lbl_registration.setObjectName(u"lbl_registration")
        self.lbl_registration.setStyleSheet(u"font-size: 24px;")

        self.gridLayout.addWidget(self.lbl_registration, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.widget)

        self.stackedWidget.addWidget(self.registration)
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.verticalLayout_5 = QVBoxLayout(self.login)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_4 = QWidget(self.login)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_2 = QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.le_l_log = QLineEdit(self.widget_4)
        self.le_l_log.setObjectName(u"le_l_log")

        self.gridLayout_2.addWidget(self.le_l_log, 1, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 3, 1, 1, 1)

        self.btn_log = QPushButton(self.widget_4)
        self.btn_log.setObjectName(u"btn_log")

        self.t_data = None
        self.btn_log.clicked.connect(self.login_to)


        self.gridLayout_2.addWidget(self.btn_log, 4, 0, 1, 1)

        self.le_l_pwd = QLineEdit(self.widget_4)
        self.le_l_pwd.setObjectName(u"le_l_pwd")

        self.gridLayout_2.addWidget(self.le_l_pwd, 2, 1, 1, 1)

        self.lbl_l_pwd = QLabel(self.widget_4)
        self.lbl_l_pwd.setObjectName(u"lbl_l_pwd")

        self.gridLayout_2.addWidget(self.lbl_l_pwd, 2, 0, 1, 1)

        self.lbl_l_log = QLabel(self.widget_4)
        self.lbl_l_log.setObjectName(u"lbl_l_log")

        self.gridLayout_2.addWidget(self.lbl_l_log, 1, 0, 1, 1)

        self.lbl_login = QLabel(self.widget_4)
        self.lbl_login.setObjectName(u"lbl_login")
        self.lbl_login.setStyleSheet(u"font-size: 24px;")

        self.gridLayout_2.addWidget(self.lbl_login, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.widget_4)

        self.smtp = QPushButton(self.widget_4)
        self.smtp.setObjectName(u"smtp")

        self.gridLayout_2.addWidget(self.smtp, 5, 0, 1, 1)
        self.smtp.setText(QCoreApplication.translate("MainWindow", "Новый пароль", None))
        self.smtp.clicked.connect(lambda: Mail().send_mail(self.le_l_log.text()))

        self.stackedWidget.addWidget(self.login)
        self.create_test = QWidget()
        self.create_test.setObjectName(u"create_test")
        self.verticalLayout_8 = QVBoxLayout(self.create_test)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.w_cr = QWidget(self.create_test)
        self.w_cr.setObjectName(u"w_cr")
        self.verticalLayout_9 = QVBoxLayout(self.w_cr)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.info = QWidget(self.w_cr)
        self.info.setObjectName(u"info")
        self.gridLayout_3 = QGridLayout(self.info)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.le_ct_time = QLineEdit(self.info)
        self.le_ct_time.setObjectName(u"le_ct_time")

        self.gridLayout_3.addWidget(self.le_ct_time, 1, 4, 1, 1)

        self.lbl_ct = QLabel(self.info)
        self.lbl_ct.setObjectName(u"lbl_ct")
        self.lbl_ct.setStyleSheet(u"font-size: 24px;")

        self.gridLayout_3.addWidget(self.lbl_ct, 0, 0, 1, 2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 3, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(216, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.le_ct_name = QLineEdit(self.info)
        self.le_ct_name.setObjectName(u"le_ct_name")

        self.gridLayout_3.addWidget(self.le_ct_name, 1, 1, 1, 1)

        self.lbl_ct_name = QLabel(self.info)
        self.lbl_ct_name.setObjectName(u"lbl_ct_name")

        self.gridLayout_3.addWidget(self.lbl_ct_name, 1, 0, 1, 1)

        self.lbl_ct_desc = QLabel(self.info)
        self.lbl_ct_desc.setObjectName(u"lbl_ct_desc")

        self.gridLayout_3.addWidget(self.lbl_ct_desc, 2, 0, 1, 1)

        self.lbl_ct_time = QLabel(self.info)
        self.lbl_ct_time.setObjectName(u"lbl_ct_time")

        self.gridLayout_3.addWidget(self.lbl_ct_time, 1, 3, 1, 1)

        self.btn_ct_create = QPushButton(self.info)
        self.btn_ct_create.setObjectName(u"btn_ct_create")
        self.gridLayout_3.addWidget(self.btn_ct_create, 0, 5, 1, 1)
        self.btn_ct_create.clicked.connect(self.create_test_db)
        self.btn_ct_create.clicked.connect(self.page_mt)
        self.btn_ct_create.clicked.connect(self.vt)

        self.textEdit = QTextEdit(self.info)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_3.addWidget(self.textEdit, 2, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.info)

        self.q_controls = QWidget(self.w_cr)
        self.q_controls.setObjectName(u"q_controls")
        self.horizontalLayout_3 = QHBoxLayout(self.q_controls)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_ct_add = QPushButton(self.q_controls)
        self.btn_ct_add.setObjectName(u"btn_ct_add")
        self.btn_ct_add.clicked.connect(self.add_q)

        self.horizontalLayout_3.addWidget(self.btn_ct_add)

        self.btn_ct_remove = QPushButton(self.q_controls)
        self.btn_ct_remove.setObjectName(u"btn_ct_remove")

        self.btn_ct_remove.clicked.connect(self.remove_q)

        self.horizontalLayout_3.addWidget(self.btn_ct_remove)


        self.verticalLayout_9.addWidget(self.q_controls)

#####################################################
        self.w_list = []
        self.hs_list = []
        self.gl_list = []
        self.q_le_list = []
        self.q_lbl_list = []
        self.a_le_list = []
        self.a_lbl_list = []
        self.img_list = {}
        self.img_b_list = []

        self.w_list.append(QWidget(self.w_cr))
        self.gl_list.append(QGridLayout(self.w_list[0]))
        self.hs_list.append(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.gl_list[0].addItem(self.hs_list[0], 0, 2, 1, 1)

        self.q_lbl_list.append(QLabel(self.w_list[0]))
        self.q_le_list.append(QLineEdit(self.w_list[0]))

        self.a_lbl_list.append(QLabel(self.w_list[0]))
        self.a_le_list.append(QLineEdit(self.w_list[0]))

        self.img_b_list.append(QPushButton(self.w_list[0]))
        self.img_b_list[0].clicked.connect(lambda: self.img_f_d(0))


        self.gl_list[0].addWidget(self.a_lbl_list[0], 1, 0, 1, 1)
        self.gl_list[0].addWidget(self.a_le_list[0], 1, 1, 1, 1)

        self.gl_list[0].addWidget(self.q_lbl_list[0], 0, 0, 1, 1)
        self.gl_list[0].addWidget(self.q_le_list[0], 0, 1, 1, 1)

        self.gl_list[0].addWidget(self.img_b_list[0], 2, 0, 1, 1)

        self.verticalLayout_9.addWidget(self.w_list[0])
######################################################
        
        self.verticalLayout_8.addWidget(self.w_cr)

        self.stackedWidget.addWidget(self.create_test)


        self.view_tests = QWidget()
        self.view_tests.setObjectName(u"view_tests")
        self.verticalLayout_10 = QVBoxLayout(self.view_tests)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")

        self.widget_3 = QWidget(self.view_tests)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_10.addWidget(self.widget_3)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.stackedWidget.addWidget(self.view_tests)

        self.horizontalLayout_2.addWidget(self.right_menu)


        self.verticalLayout_3.addWidget(self.down_menu)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)

        self.btn_lm_ct.setEnabled(False)
        self.btn_lm_mt.setEnabled(False)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_tm_account.setText("")
        self.btn_lm_ct.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0442\u0435\u0441\u0442", None))
        self.btn_lm_mt.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0438 \u0442\u0435\u0441\u0442\u044b", None))
        self.lbl_greet.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c", None))
        self.lbl_r_ln.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.lbl_r_fn.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.lbl_r_mail.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lbl_r_log.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.btn_reg.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u0441\u044f", None))
        self.lbl_r_mn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.lbl_r_pwd.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.lbl_registration.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.btn_log.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.lbl_l_pwd.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.lbl_l_log.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.lbl_login.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.lbl_ct.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0442\u0435\u0441\u0442", None))
        self.lbl_ct_name.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.lbl_ct_desc.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.lbl_ct_time.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0442\u0435\u0441\u0442\u0430 (\u043c\u0438\u043d\u0443\u0442)", None))
        self.btn_ct_create.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.btn_ct_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432\u043e\u043f\u0440\u043e\u0441", None))
        self.btn_ct_remove.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u043e\u043f\u0440\u043e\u0441", None))
        self.q_lbl_list[0].setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 1", None))
        self.a_lbl_list[0].setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0432\u0435\u0442 1", None))
        self.img_b_list[0].setText(QCoreApplication.translate("MainWindow", "Добавить фото", None))
    # retranslateUi

    def page_greet(self):
        self.stackedWidget.setCurrentIndex(0)
    def menu_reg(self):
        self.stackedWidget.setCurrentIndex(1)
    def menu_log(self):
        self.stackedWidget.setCurrentIndex(2)
    def page_ct(self):
        self.stackedWidget.setCurrentIndex(3)
    def page_mt(self):
        self.vt()
        self.stackedWidget.setCurrentIndex(4)

    def add_q(self):
        i = len(self.w_list)
        self.w_list.append(QWidget(self.w_cr))
        self.gl_list.append(QGridLayout(self.w_list[i]))
        self.hs_list.append(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.gl_list[i].addItem(self.hs_list[i], 0, 2, 1, 1)

        self.q_lbl_list.append(QLabel(self.w_list[i]))
        self.q_le_list.append(QLineEdit(self.w_list[i]))

        self.a_lbl_list.append(QLabel(self.w_list[i]))
        self.a_le_list.append(QLineEdit(self.w_list[i]))

        self.img_b_list.append(QPushButton(self.w_list[i]))
        self.img_b_list[i].clicked.connect(lambda: self.img_f_d(i))

        self.gl_list[i].addWidget(self.a_lbl_list[i], 1, 0, 1, 1)
        self.gl_list[i].addWidget(self.a_le_list[i], 1, 1, 1, 1)

        self.gl_list[i].addWidget(self.q_lbl_list[i], 0, 0, 1, 1)
        self.gl_list[i].addWidget(self.q_le_list[i], 0, 1, 1, 1)

        self.gl_list[i].addWidget(self.img_b_list[i], 2, 0, 1, 1)
        
        self.verticalLayout_9.addWidget(self.w_list[i])
        self.q_lbl_list[i].setText(QCoreApplication.translate("MainWindow", f"Вопрос {i + 1}", None))
        self.a_lbl_list[i].setText(QCoreApplication.translate("MainWindow", f"Ответ {i + 1}", None))
        self.img_b_list[i].setText(QCoreApplication.translate("MainWindow", f"Добавить фото", None))

    def remove_q(self):
        # TODO: надо сделать
        i = len(self.w_list) - 1
        self.verticalLayout_9.removeWidget(self.w_list[i])

    def create_test_db(self):
        questions = [n.text() for n in self.q_le_list]
        answers = [n.text() for n in self.a_le_list]

        db = DB()
        db.add_test(self.le_ct_name.text(), self.textEdit.toPlainText(), self.le_ct_time.text(), questions, answers, self.img_list, self.t_data[0])

    def img_f_d(self, i):
        a = QFileDialog.getOpenFileName()
        with open(a[0], 'rb') as f:
            self.img_list[i] = f.read()
        #print(self.img_list)

    def login_to(self):
        l = self.le_l_log.text()
        p = self.le_l_pwd.text()
        db = DB()
        self.t_data = db.login(l, p)
        self.page_greet()
        if self.t_data != None:
            self.btn_lm_ct.setEnabled(True)
            self.btn_lm_mt.setEnabled(True)
            self.lbl_greet.setText(QCoreApplication.translate("MainWindow", f"Добро пожаловать {self.t_data[3]} {self.t_data[4]}", None))

    def login_from_reg(self):
        if self.le_r_ln.text() == '':
            self.le_r_ln.clear()
            self.lbl_r_ln.setStyleSheet(u'color: red')
        elif self.le_r_fn.text() == '':
            self.lbl_r_ln.setStyleSheet(u'color: black')
            self.le_r_fn.clear()
            self.lbl_r_fn.setStyleSheet(u'color: red')
        elif self.le_r_log.text() == '':
            self.lbl_r_fn.setStyleSheet(u'color: black')
            self.le_r_log.clear()
            self.lbl_r_log.setStyleSheet(u'color: red')
        elif self.le_r_pwd.text() == '':
            self.lbl_r_log.setStyleSheet(u'color: black')
            self.le_r_pwd.clear()
            self.lbl_r_pwd.setStyleSheet(u'color: red')
        elif not (re.search(r'[^@]+@[^@]+\.[^@]+', self.le_r_mail.text())):
            self.lbl_r_pwd.setStyleSheet(u'color: black')
            self.le_r_mail.clear()
            self.lbl_r_mail.setStyleSheet(u'color: red')
        else:
            self.lbl_r_mail.setStyleSheet(u'color: black')
            l = self.le_r_log.text()
            p = self.le_r_pwd.text()
            db = DB()
            db.reg(self.le_r_ln.text(), self.le_r_fn.text(), self.le_r_mn.text(), self.le_r_mail.text(), self.le_r_log.text(), self.le_r_pwd.text())
            self.t_data = db.login(l, p)
            self.page_greet()
            if self.t_data != None:
                self.btn_lm_ct.setEnabled(True)
                self.btn_lm_mt.setEnabled(True)
                self.lbl_greet.setText(QCoreApplication.translate("MainWindow", f"Добро пожаловать {self.t_data[3]} {self.t_data[4]}", None))

    def vt(self):
        for i in reversed(range(self.verticalLayout_10.count())):
            try:
                self.verticalLayout_10.itemAt(i).widget().setParent(None)
            except:
                pass
        db = DB()
        data = db.view_tests(self.t_data[0])
        #print(data)

        self.vt_vs = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        

        self.vt_w_list = []
        self.vt_vl_list = []
        self.vt_l_list_0 = []
        self.vt_l_list_1 = []
        self.vt_l_list_2 = []

        for d in data:
            self.vt_w_list.append(QWidget(self.widget_3))
            self.vt_vl_list.append(QVBoxLayout(self.vt_w_list[len(self.vt_w_list) - 1]))
            self.vt_l_list_0.append(QLabel(f'Название: {d[0]}', self.vt_w_list[len(self.vt_w_list) - 1]))
            self.vt_l_list_1.append(QLabel(f'Описание: {d[1]}', self.vt_w_list[len(self.vt_w_list) - 1]))
            self.vt_l_list_2.append(QLabel(f'Время: {d[2]}', self.vt_w_list[len(self.vt_w_list) - 1]))

            self.vt_vl_list[len(self.vt_w_list) - 1].addWidget(self.vt_l_list_0[len(self.vt_w_list) - 1])
            self.vt_vl_list[len(self.vt_w_list) - 1].addWidget(self.vt_l_list_1[len(self.vt_w_list) - 1])
            self.vt_vl_list[len(self.vt_w_list) - 1].addWidget(self.vt_l_list_2[len(self.vt_w_list) - 1])
            self.verticalLayout_10.addWidget(self.vt_w_list[len(self.vt_w_list) - 1])

        self.verticalLayout_10.addItem(self.vt_vs)

