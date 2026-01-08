from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidgetItem,
    QMessageBox, QFileDialog, QLineEdit, QPushButton, QTableWidget
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from db import DB
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class FormPembayaran(QWidget):
    def __init__(self):
        super().__init__()

        # ===== LOAD UI =====
        loader = QUiLoader()
        ui_file = QFile("form_pembayaran.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        layout = QVBoxLayout(self)
        layout.addWidget(self.ui)

        self.db = DB()

        # ===== AMBIL WIDGET (PASTI ADA) =====
        self.kodeEdit = self.ui.findChild(QLineEdit, "kodeTransferLineEdit")
        self.rekeningEdit = self.ui.findChild(QLineEdit, "noRekeningLineEdit")
        self.namaEdit = self.ui.findChild(QLineEdit, "namaPemilikRekLineEdit")
        self.nominalEdit = self.ui.findChild(QLineEdit, "nominalLineEdit")
        self.idIklanEdit = self.ui.findChild(QLineEdit, "iDIklanLineEdit")

        self.simpanBtn = self.ui.findChild(QPushButton, "simpanBtn")
        self.ubahBtn = self.ui.findChild(QPushButton, "ubahBtn")
        self.hapusBtn = self.ui.findChild(QPushButton, "ubahBtn_2")
        self.cetakBtn = self.ui.findChild(QPushButton, "cetakBtn")

        self.cariEdit = self.ui.findChild(QLineEdit, "cariEdit")
        self.table = self.ui.findChild(QTableWidget, "tableWidget")

        # ===== KONEKSI =====
        self.simpanBtn.clicked.connect(self.simpan)
        self.ubahBtn.clicked.connect(self.ubah)
        self.hapusBtn.clicked.connect(self.hapus)
        self.cetakBtn.clicked.connect(self.cetak_pdf)
        self.cariEdit.textChanged.connect(self.filter_data)

        self.load_data()

    # ================= LOAD DATA =================
    def load_data(self, data=None):
        if data is None:
            data = self.db.cariDataPembayaran()

        self.table.setRowCount(len(data))
        for r, row in enumerate(data):
            for c, val in enumerate(row):
                self.table.setItem(r, c, QTableWidgetItem(str(val)))

    # ================= SIMPAN =================
    def simpan(self):
        kode = self.kodeEdit.text()
        rekening = self.rekeningEdit.text()
        nama = self.namaEdit.text()
        nominal = self.nominalEdit.text()
        id_iklan = self.idIklanEdit.text()

        if kode == "" or rekening == "" or nominal == "":
            QMessageBox.warning(
                self, "Validasi",
                "Kode Transfer, No Rekening, dan Nominal wajib diisi"
            )
            return

        sukses = self.db.simpanPembayaran(
            kode, rekening, "2026-01-08", nominal, id_iklan
        )

        if sukses:
            QMessageBox.information(self, "Sukses", "Pembayaran berhasil disimpan")
            self.load_data()
            self.clear_form()
        else:
            QMessageBox.critical(self, "Gagal", "Gagal menyimpan data")

    # ================= UBAH =================
    def ubah(self):
        QMessageBox.information(self, "Info", "Fitur UBAH bisa ditambahkan")

    # ================= HAPUS =================
    def hapus(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Pilih Data", "Pilih data terlebih dahulu")
            return

        kode = self.table.item(row, 0).text()

        try:
            cursor = self.db.koneksi.cursor()
            cursor.execute(
                "DELETE FROM pembayaran WHERE kode_transfer=%s", (kode,)
            )
            self.db.koneksi.commit()
            QMessageBox.information(self, "Sukses", "Data berhasil dihapus")
            self.load_data()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    # ================= FILTER =================
    def filter_data(self):
        data = self.db.filterPembayaran(self.cariEdit.text())
        self.load_data(data)

    # ================= CETAK PDF =================
    def cetak_pdf(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Simpan PDF", "", "PDF Files (*.pdf)"
        )
        if path:
            c = canvas.Canvas(path, pagesize=letter)
            c.drawString(100, 750, "LAPORAN DATA PEMBAYARAN")

            y = 720
            for row in self.db.cariDataPembayaran():
                c.drawString(100, y, " | ".join(map(str, row)))
                y -= 20

            c.save()
            QMessageBox.information(self, "Sukses", "PDF berhasil dibuat")

    # ================= CLEAR =================
    def clear_form(self):
        self.kodeEdit.clear()
        self.rekeningEdit.clear()
        self.namaEdit.clear()
        self.nominalEdit.clear()
        self.idIklanEdit.clear()
