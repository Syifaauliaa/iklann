# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionFORM_IKLAN = QAction(MainWindow)
        self.actionFORM_IKLAN.setObjectName(u"actionFORM_IKLAN")
        self.actionFORM_MEMBER = QAction(MainWindow)
        self.actionFORM_MEMBER.setObjectName(u"actionFORM_MEMBER")
        self.actionFORM_PEMBAYARAN = QAction(MainWindow)
        self.actionFORM_PEMBAYARAN.setObjectName(u"actionFORM_PEMBAYARAN")
        self.actionFORM_PESAN_INBOX = QAction(MainWindow)
        self.actionFORM_PESAN_INBOX.setObjectName(u"actionFORM_PESAN_INBOX")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuHALAMAN_MENU = QMenu(self.menubar)
        self.menuHALAMAN_MENU.setObjectName(u"menuHALAMAN_MENU")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHALAMAN_MENU.menuAction())
        self.menuHALAMAN_MENU.addAction(self.actionFORM_IKLAN)
        self.menuHALAMAN_MENU.addAction(self.actionFORM_MEMBER)
        self.menuHALAMAN_MENU.addAction(self.actionFORM_PEMBAYARAN)
        self.menuHALAMAN_MENU.addAction(self.actionFORM_PESAN_INBOX)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionFORM_IKLAN.setText(QCoreApplication.translate("MainWindow", u"FORM IKLAN", None))
        self.actionFORM_MEMBER.setText(QCoreApplication.translate("MainWindow", u"FORM MEMBER", None))
        self.actionFORM_PEMBAYARAN.setText(QCoreApplication.translate("MainWindow", u"FORM PEMBAYARAN", None))
        self.actionFORM_PESAN_INBOX.setText(QCoreApplication.translate("MainWindow", u"FORM PESAN INBOX", None))
        self.menuHALAMAN_MENU.setTitle(QCoreApplication.translate("MainWindow", u"HALAMAN MENU", None))
    # retranslateUi

