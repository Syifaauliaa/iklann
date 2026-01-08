# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_pembayaran.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(590, 390)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(70, 30, 401, 161))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.kodeTransferLabel = QLabel(self.formLayoutWidget)
        self.kodeTransferLabel.setObjectName(u"kodeTransferLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.kodeTransferLabel)

        self.kodeTransferLineEdit = QLineEdit(self.formLayoutWidget)
        self.kodeTransferLineEdit.setObjectName(u"kodeTransferLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.kodeTransferLineEdit)

        self.noRekeningLabel = QLabel(self.formLayoutWidget)
        self.noRekeningLabel.setObjectName(u"noRekeningLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.noRekeningLabel)

        self.noRekeningLineEdit = QLineEdit(self.formLayoutWidget)
        self.noRekeningLineEdit.setObjectName(u"noRekeningLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.noRekeningLineEdit)

        self.namaPemilikRekLabel = QLabel(self.formLayoutWidget)
        self.namaPemilikRekLabel.setObjectName(u"namaPemilikRekLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.namaPemilikRekLabel)

        self.namaPemilikRekLineEdit = QLineEdit(self.formLayoutWidget)
        self.namaPemilikRekLineEdit.setObjectName(u"namaPemilikRekLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.namaPemilikRekLineEdit)

        self.nominalLabel = QLabel(self.formLayoutWidget)
        self.nominalLabel.setObjectName(u"nominalLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.nominalLabel)

        self.nominalLineEdit = QLineEdit(self.formLayoutWidget)
        self.nominalLineEdit.setObjectName(u"nominalLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.nominalLineEdit)

        self.iDIklanLabel = QLabel(self.formLayoutWidget)
        self.iDIklanLabel.setObjectName(u"iDIklanLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.iDIklanLabel)

        self.iDIklanLineEdit = QLineEdit(self.formLayoutWidget)
        self.iDIklanLineEdit.setObjectName(u"iDIklanLineEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.iDIklanLineEdit)

        self.simpanBtn = QPushButton(Form)
        self.simpanBtn.setObjectName(u"simpanBtn")
        self.simpanBtn.setGeometry(QRect(80, 240, 75, 24))
        self.ubahBtn = QPushButton(Form)
        self.ubahBtn.setObjectName(u"ubahBtn")
        self.ubahBtn.setGeometry(QRect(180, 240, 75, 24))
        self.ubahBtn_2 = QPushButton(Form)
        self.ubahBtn_2.setObjectName(u"ubahBtn_2")
        self.ubahBtn_2.setGeometry(QRect(280, 240, 75, 24))
        self.cetakBtn = QPushButton(Form)
        self.cetakBtn.setObjectName(u"cetakBtn")
        self.cetakBtn.setGeometry(QRect(390, 240, 75, 24))
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
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
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 280, 511, 192))
        self.cariEdit = QLineEdit(Form)
        self.cariEdit.setObjectName(u"cariEdit")
        self.cariEdit.setGeometry(QRect(110, 210, 331, 22))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.kodeTransferLabel.setText(QCoreApplication.translate("Form", u"Kode Transfer", None))
        self.noRekeningLabel.setText(QCoreApplication.translate("Form", u"No Rekening", None))
        self.namaPemilikRekLabel.setText(QCoreApplication.translate("Form", u"Nama Pemilik Rek", None))
        self.nominalLabel.setText(QCoreApplication.translate("Form", u"Nominal", None))
        self.iDIklanLabel.setText(QCoreApplication.translate("Form", u"ID Iklan", None))
        self.simpanBtn.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.ubahBtn.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.ubahBtn_2.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.cetakBtn.setText(QCoreApplication.translate("Form", u"CETAK", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"REKENING", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"KODE", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"NAMA", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"NOMINAL", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"ID IKLAN", None));
    # retranslateUi

