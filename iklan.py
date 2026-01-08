from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidgetItem,
    QPushButton, QLineEdit, QMessageBox,
    QTableWidget, QFileDialog, QComboBox, QDateEdit
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from db import DB


class FormIklan(QWidget):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        ui_file = QFile("form_iklan.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        layout = QVBoxLayout(self)
        layout.addWidget(self.ui)

        self.db = DB()

        # === Widget ===
        self.table = self.ui.findChild(QTableWidget, "tableWidget")
        self.cariEdit = self.ui.findChild(QLineEdit, "cariEdit")

        self.simpanBtn = self.ui.findChild(QPushButton, "simpanBtn")
        self.ubahBtn = self.ui.findChild(QPushButton, "ubahBtn")
        self.hapusBtn = self.ui.findChild(QPushButton, "hapusBtn")
        self.cetakBtn = self.ui.findChild(QPushButton, "cetakBtn")

        # === Koneksi ===
        self.simpanBtn.clicked.connect(self.simpan)
        self.ubahBtn.clicked.connect(self.ubah)
        self.hapusBtn.clicked.connect(self.hapus)
        self.cetakBtn.clicked.connect(self.cetak_pdf)
        self.cariEdit.textChanged.connect(self.filter_data)

        self.load_data()

    # ================= LOAD DATA =================
    def load_data(self, data=None):
        if data is None:
            data = self.db.cariDataIklan()

        self.table.setRowCount(len(data))
        for r, row in enumerate(data):
            for c, val in enumerate(row):
                self.table.setItem(r, c, QTableWidgetItem(str(val)))

    # ================= SIMPAN =================
    def simpan(self):
        try:
            kd_member = self.ui.findChild(QLineEdit, "iDMemberLineEdit").text()

            tgl = self.ui.findChild(
                QDateEdit, "tanggalPasangDateEdit"
            ).date().toString("yyyy-MM-dd")

            judul = self.ui.findChild(QLineEdit, "judulIklanLineEdit").text()

            kondisi = self.ui.findChild(
                QComboBox, "kondisiComboBox"
            ).currentText()

            status = self.ui.findChild(
                QComboBox, "statusAktifComboBox"
            ).currentText()

            jalan = self.ui.findChild(QLineEdit, "namaJalanLineEdit").text()
            g1 = self.ui.findChild(QLineEdit, "gambar1LineEdit").text()
            g2 = self.ui.findChild(QLineEdit, "gambar2LineEdit").text()
            g3 = self.ui.findChild(QLineEdit, "gambar3LineEdit").text()
            harga = self.ui.findChild(QLineEdit, "hargaLineEdit").text()
            desk = self.ui.findChild(QLineEdit, "deskripsiLineEdit").text()

            self.db.simpanIklan(
                kd_member, tgl, judul, kondisi, status,
                jalan, g1, g2, g3, harga, desk
            )

            QMessageBox.information(self, "Sukses", "Data iklan berhasil disimpan")
            self.load_data()

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    # ================= UBAH =================
    def ubah(self):
        QMessageBox.information(self, "Info", "Fungsi UBAH siap ditambahkan")

    # ================= HAPUS =================
    def hapus(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Pilih Data", "Pilih data dulu")
            return

        kd_iklan = self.table.item(row, 0).text()
        self.db.hapusIklan(kd_iklan)
        self.load_data()

    # ================= FILTER =================
    def filter_data(self):
        data = self.db.filterIklan(self.cariEdit.text())
        self.load_data(data)

    # ================= CETAK =================
    def cetak_pdf(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Simpan PDF", "", "PDF Files (*.pdf)"
        )
        if not path:
            return

        c = canvas.Canvas(path, pagesize=letter)
        c.drawString(200, 750, "LAPORAN DATA IKLAN")

        y = 720
        for row in self.db.cariDataIklan():
            c.drawString(50, y, f"{row[0]} | {row[3]} | {row[9]}")
            y -= 20
            if y < 50:
                c.showPage()
                y = 750

        c.save()
        QMessageBox.information(self, "Sukses", "PDF berhasil dibuat")
