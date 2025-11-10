# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_pesan_inbox.ui'
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
        Form.resize(400, 300)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(90, 10, 241, 136))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.tanggalKirimLabel = QLabel(self.formLayoutWidget)
        self.tanggalKirimLabel.setObjectName(u"tanggalKirimLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.tanggalKirimLabel)

        self.tanggalKirimDateEdit = QDateEdit(self.formLayoutWidget)
        self.tanggalKirimDateEdit.setObjectName(u"tanggalKirimDateEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.tanggalKirimDateEdit)

        self.namaPengirimLabel = QLabel(self.formLayoutWidget)
        self.namaPengirimLabel.setObjectName(u"namaPengirimLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaPengirimLabel)

        self.namaPengirimLineEdit = QLineEdit(self.formLayoutWidget)
        self.namaPengirimLineEdit.setObjectName(u"namaPengirimLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.namaPengirimLineEdit)

        self.emailPengirimLabel = QLabel(self.formLayoutWidget)
        self.emailPengirimLabel.setObjectName(u"emailPengirimLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.emailPengirimLabel)

        self.emailPengirimLineEdit = QLineEdit(self.formLayoutWidget)
        self.emailPengirimLineEdit.setObjectName(u"emailPengirimLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.emailPengirimLineEdit)

        self.isiPesanLabel = QLabel(self.formLayoutWidget)
        self.isiPesanLabel.setObjectName(u"isiPesanLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.isiPesanLabel)

        self.isiPesanLineEdit = QLineEdit(self.formLayoutWidget)
        self.isiPesanLineEdit.setObjectName(u"isiPesanLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.isiPesanLineEdit)

        self.iDMemberLabel = QLabel(self.formLayoutWidget)
        self.iDMemberLabel.setObjectName(u"iDMemberLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.iDMemberLabel)

        self.iDMemberLineEdit = QLineEdit(self.formLayoutWidget)
        self.iDMemberLineEdit.setObjectName(u"iDMemberLineEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.iDMemberLineEdit)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 150, 75, 24))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 150, 75, 24))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(220, 150, 75, 24))
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(300, 150, 75, 24))
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
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
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(70, 200, 256, 192))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.tanggalKirimLabel.setText(QCoreApplication.translate("Form", u"Tanggal Kirim", None))
        self.namaPengirimLabel.setText(QCoreApplication.translate("Form", u"Nama Pengirim", None))
        self.emailPengirimLabel.setText(QCoreApplication.translate("Form", u"Email Pengirim", None))
        self.isiPesanLabel.setText(QCoreApplication.translate("Form", u"Isi Pesan", None))
        self.iDMemberLabel.setText(QCoreApplication.translate("Form", u"ID Member", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
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
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"ISI PESAN", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"ID MEMBER", None));
    # retranslateUi

