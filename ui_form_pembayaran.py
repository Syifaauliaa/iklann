# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_pembayaran.ui'
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

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 200, 75, 24))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(180, 200, 75, 24))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(270, 200, 75, 24))
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(370, 200, 75, 24))
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
        self.tableWidget.setGeometry(QRect(70, 240, 511, 192))

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
        self.pushButton.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"CLEAR", None))
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

