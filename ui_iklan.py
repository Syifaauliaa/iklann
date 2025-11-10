# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'iklan.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(657, 449)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(60, 0, 421, 304))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDMemberLabel = QLabel(self.formLayoutWidget)
        self.iDMemberLabel.setObjectName(u"iDMemberLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDMemberLabel)

        self.iDMemberLineEdit = QLineEdit(self.formLayoutWidget)
        self.iDMemberLineEdit.setObjectName(u"iDMemberLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.iDMemberLineEdit)

        self.tanggalPasangLabel = QLabel(self.formLayoutWidget)
        self.tanggalPasangLabel.setObjectName(u"tanggalPasangLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.tanggalPasangLabel)

        self.tanggalPasangDateEdit = QDateEdit(self.formLayoutWidget)
        self.tanggalPasangDateEdit.setObjectName(u"tanggalPasangDateEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.tanggalPasangDateEdit)

        self.judulIklanLabel = QLabel(self.formLayoutWidget)
        self.judulIklanLabel.setObjectName(u"judulIklanLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.judulIklanLabel)

        self.judulIklanLineEdit = QLineEdit(self.formLayoutWidget)
        self.judulIklanLineEdit.setObjectName(u"judulIklanLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.judulIklanLineEdit)

        self.kondisiLabel = QLabel(self.formLayoutWidget)
        self.kondisiLabel.setObjectName(u"kondisiLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.kondisiLabel)

        self.kondisiComboBox = QComboBox(self.formLayoutWidget)
        self.kondisiComboBox.setObjectName(u"kondisiComboBox")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.kondisiComboBox)

        self.statusAktifLabel = QLabel(self.formLayoutWidget)
        self.statusAktifLabel.setObjectName(u"statusAktifLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.statusAktifLabel)

        self.statusAktifComboBox = QComboBox(self.formLayoutWidget)
        self.statusAktifComboBox.setObjectName(u"statusAktifComboBox")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.statusAktifComboBox)

        self.namaJalanLabel = QLabel(self.formLayoutWidget)
        self.namaJalanLabel.setObjectName(u"namaJalanLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.namaJalanLabel)

        self.namaJalanLineEdit = QLineEdit(self.formLayoutWidget)
        self.namaJalanLineEdit.setObjectName(u"namaJalanLineEdit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.namaJalanLineEdit)

        self.gambar1Label = QLabel(self.formLayoutWidget)
        self.gambar1Label.setObjectName(u"gambar1Label")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.gambar1Label)

        self.gambar1LineEdit = QLineEdit(self.formLayoutWidget)
        self.gambar1LineEdit.setObjectName(u"gambar1LineEdit")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.gambar1LineEdit)

        self.gambar2Label = QLabel(self.formLayoutWidget)
        self.gambar2Label.setObjectName(u"gambar2Label")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.gambar2Label)

        self.gambar2LineEdit = QLineEdit(self.formLayoutWidget)
        self.gambar2LineEdit.setObjectName(u"gambar2LineEdit")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.gambar2LineEdit)

        self.gambar3Label = QLabel(self.formLayoutWidget)
        self.gambar3Label.setObjectName(u"gambar3Label")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.gambar3Label)

        self.gambar3LineEdit = QLineEdit(self.formLayoutWidget)
        self.gambar3LineEdit.setObjectName(u"gambar3LineEdit")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.gambar3LineEdit)

        self.hargaLabel = QLabel(self.formLayoutWidget)
        self.hargaLabel.setObjectName(u"hargaLabel")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.hargaLabel)

        self.hargaLineEdit = QLineEdit(self.formLayoutWidget)
        self.hargaLineEdit.setObjectName(u"hargaLineEdit")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.hargaLineEdit)

        self.deskripsiLabel = QLabel(self.formLayoutWidget)
        self.deskripsiLabel.setObjectName(u"deskripsiLabel")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.deskripsiLabel)

        self.deskripsiLineEdit = QLineEdit(self.formLayoutWidget)
        self.deskripsiLineEdit.setObjectName(u"deskripsiLineEdit")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.FieldRole, self.deskripsiLineEdit)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(70, 310, 75, 24))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(170, 310, 75, 24))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(260, 310, 75, 24))
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(370, 310, 75, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDMemberLabel.setText(QCoreApplication.translate("Form", u"ID Member", None))
        self.tanggalPasangLabel.setText(QCoreApplication.translate("Form", u"Tanggal Pasang", None))
        self.judulIklanLabel.setText(QCoreApplication.translate("Form", u"Judul Iklan", None))
        self.kondisiLabel.setText(QCoreApplication.translate("Form", u"Kondisi", None))
        self.statusAktifLabel.setText(QCoreApplication.translate("Form", u"Status Aktif", None))
        self.namaJalanLabel.setText(QCoreApplication.translate("Form", u"Nama Jalan", None))
        self.gambar1Label.setText(QCoreApplication.translate("Form", u"Gambar1", None))
        self.gambar2Label.setText(QCoreApplication.translate("Form", u"Gambar2", None))
        self.gambar3Label.setText(QCoreApplication.translate("Form", u"Gambar3", None))
        self.hargaLabel.setText(QCoreApplication.translate("Form", u"Harga", None))
        self.deskripsiLabel.setText(QCoreApplication.translate("Form", u"Deskripsi", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"CLEAR", None))
    # retranslateUi

