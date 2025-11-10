# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_member.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(588, 406)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 230, 75, 24))
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(110, 10, 351, 211))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.namaMemberLabel = QLabel(self.formLayoutWidget)
        self.namaMemberLabel.setObjectName(u"namaMemberLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.namaMemberLabel)

        self.namaMemberLineEdit = QLineEdit(self.formLayoutWidget)
        self.namaMemberLineEdit.setObjectName(u"namaMemberLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.namaMemberLineEdit)

        self.emailLabel = QLabel(self.formLayoutWidget)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.emailLabel)

        self.emailLineEdit = QLineEdit(self.formLayoutWidget)
        self.emailLineEdit.setObjectName(u"emailLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.emailLineEdit)

        self.noTeleponLabel = QLabel(self.formLayoutWidget)
        self.noTeleponLabel.setObjectName(u"noTeleponLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.noTeleponLabel)

        self.noTeleponLineEdit = QLineEdit(self.formLayoutWidget)
        self.noTeleponLineEdit.setObjectName(u"noTeleponLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.noTeleponLineEdit)

        self.pINBBLabel = QLabel(self.formLayoutWidget)
        self.pINBBLabel.setObjectName(u"pINBBLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.pINBBLabel)

        self.pINBBLineEdit = QLineEdit(self.formLayoutWidget)
        self.pINBBLineEdit.setObjectName(u"pINBBLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.pINBBLineEdit)

        self.pathFotoLabel = QLabel(self.formLayoutWidget)
        self.pathFotoLabel.setObjectName(u"pathFotoLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.pathFotoLabel)

        self.pathFotoLineEdit = QLineEdit(self.formLayoutWidget)
        self.pathFotoLineEdit.setObjectName(u"pathFotoLineEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.pathFotoLineEdit)

        self.passwordLabel = QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.passwordLabel)

        self.passwordLineEdit = QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.passwordLineEdit)

        self.tanggalDaftarLabel = QLabel(self.formLayoutWidget)
        self.tanggalDaftarLabel.setObjectName(u"tanggalDaftarLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.tanggalDaftarLabel)

        self.tanggalDaftarDateEdit = QDateEdit(self.formLayoutWidget)
        self.tanggalDaftarDateEdit.setObjectName(u"tanggalDaftarDateEdit")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.tanggalDaftarDateEdit)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(200, 230, 75, 24))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(290, 230, 75, 24))
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(380, 230, 75, 24))
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(110, 260, 411, 192))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.namaMemberLabel.setText(QCoreApplication.translate("Form", u"Nama Member", None))
        self.emailLabel.setText(QCoreApplication.translate("Form", u"Email", None))
        self.noTeleponLabel.setText(QCoreApplication.translate("Form", u"No Telepon", None))
        self.pINBBLabel.setText(QCoreApplication.translate("Form", u"PIN BB", None))
        self.pathFotoLabel.setText(QCoreApplication.translate("Form", u"Path Foto", None))
        self.passwordLabel.setText(QCoreApplication.translate("Form", u"Password", None))
        self.tanggalDaftarLabel.setText(QCoreApplication.translate("Form", u"Tanggal Daftar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"CLEAR", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"NAMA", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"EMAIL", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"NO TLP", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"PIN BB", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"PATH FOTO", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"TANGGAL DAFTAR", None));
    # retranslateUi

