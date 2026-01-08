# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_iklan.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(757, 624)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(60, 0, 421, 311))
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
        self.kondisiComboBox.addItem("")
        self.kondisiComboBox.addItem("")
        self.kondisiComboBox.addItem("")
        self.kondisiComboBox.setObjectName(u"kondisiComboBox")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.kondisiComboBox)

        self.statusAktifLabel = QLabel(self.formLayoutWidget)
        self.statusAktifLabel.setObjectName(u"statusAktifLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.statusAktifLabel)

        self.statusAktifComboBox = QComboBox(self.formLayoutWidget)
        self.statusAktifComboBox.addItem("")
        self.statusAktifComboBox.addItem("")
        self.statusAktifComboBox.addItem("")
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

        self.simpanBtn = QPushButton(Form)
        self.simpanBtn.setObjectName(u"simpanBtn")
        self.simpanBtn.setGeometry(QRect(70, 360, 75, 24))
        self.ubahBtn = QPushButton(Form)
        self.ubahBtn.setObjectName(u"ubahBtn")
        self.ubahBtn.setGeometry(QRect(170, 360, 75, 24))
        self.hapusBtn = QPushButton(Form)
        self.hapusBtn.setObjectName(u"hapusBtn")
        self.hapusBtn.setGeometry(QRect(260, 360, 75, 24))
        self.cetakBtn = QPushButton(Form)
        self.cetakBtn.setObjectName(u"cetakBtn")
        self.cetakBtn.setGeometry(QRect(350, 360, 75, 24))
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
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
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(-60, 400, 821, 192))
        self.cariEdit = QLineEdit(Form)
        self.cariEdit.setObjectName(u"cariEdit")
        self.cariEdit.setGeometry(QRect(220, 550, 361, 22))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDMemberLabel.setText(QCoreApplication.translate("Form", u"ID Member", None))
        self.tanggalPasangLabel.setText(QCoreApplication.translate("Form", u"Tanggal Pasang", None))
        self.judulIklanLabel.setText(QCoreApplication.translate("Form", u"Judul Iklan", None))
        self.kondisiLabel.setText(QCoreApplication.translate("Form", u"Kondisi", None))
        self.kondisiComboBox.setItemText(0, QCoreApplication.translate("Form", u"Bagus", None))
        self.kondisiComboBox.setItemText(1, QCoreApplication.translate("Form", u"Kurang Bagus", None))
        self.kondisiComboBox.setItemText(2, QCoreApplication.translate("Form", u"Tidak Bagus", None))

#if QT_CONFIG(tooltip)
        self.kondisiComboBox.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>segar</p><p>bagus</p><p>wangi</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.statusAktifLabel.setText(QCoreApplication.translate("Form", u"Status Aktif", None))
        self.statusAktifComboBox.setItemText(0, QCoreApplication.translate("Form", u"2026-2027", None))
        self.statusAktifComboBox.setItemText(1, QCoreApplication.translate("Form", u"2027-2028", None))
        self.statusAktifComboBox.setItemText(2, QCoreApplication.translate("Form", u"2028-2029", None))

#if QT_CONFIG(tooltip)
        self.statusAktifComboBox.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>2026</p><p>2027</p><p>2028</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.namaJalanLabel.setText(QCoreApplication.translate("Form", u"Nama Jalan", None))
        self.gambar1Label.setText(QCoreApplication.translate("Form", u"Gambar1", None))
        self.gambar2Label.setText(QCoreApplication.translate("Form", u"Gambar2", None))
        self.gambar3Label.setText(QCoreApplication.translate("Form", u"Gambar3", None))
        self.hargaLabel.setText(QCoreApplication.translate("Form", u"Harga", None))
        self.deskripsiLabel.setText(QCoreApplication.translate("Form", u"Deskripsi", None))
        self.simpanBtn.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.ubahBtn.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.hapusBtn.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.cetakBtn.setText(QCoreApplication.translate("Form", u"CETAK", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"TANGGAL PASANG", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"JUDUL IKLAN", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"KONDISI", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"STATUS AKTIF", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"NAMA JALAN", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"GAMBAR1", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"GAMBAR2", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"GAMBAR3", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"DESKRIPSI", None));
        self.cariEdit.setText("")
    # retranslateUi

