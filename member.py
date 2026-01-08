from PySide6.QtWidgets import (
    QWidget, QTableWidgetItem, QMessageBox, QFileDialog
)
from ui_form_member import Ui_Form
from db import DB
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class FormMember(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.db = DB()
        self.load_data()

        # ===== Koneksi Tombol =====
        self.ui.simpanBtn.clicked.connect(self.simpan)
        self.ui.ubahBtn.clicked.connect(self.ubah)
        self.ui.hapusBtn.clicked.connect(self.hapus)
        self.ui.cetakBtn.clicked.connect(self.cetak_pdf)
        self.ui.cariEdit.textChanged.connect(self.filter_data)

    # ================= LOAD DATA =================
    def load_data(self, data=None):
        if data is None:
            data = self.db.cariDataMember()

        self.ui.tableWidget.setRowCount(len(data))
        for r, row in enumerate(data):
            for c, val in enumerate(row):
                self.ui.tableWidget.setItem(
                    r, c, QTableWidgetItem(str(val))
                )

    # ================= SIMPAN =================
    def simpan(self):
        nama = self.ui.namaMemberLineEdit.text()
        email = self.ui.emailLineEdit.text()
        telp = self.ui.noTeleponLineEdit.text()
        pin = self.ui.pINBBLineEdit.text()
        foto = self.ui.pathFotoLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        tgl = self.ui.tanggalDaftarDateEdit.date().toString("yyyy-MM-dd")

        if nama == "":
            QMessageBox.warning(self, "Validasi", "Nama member wajib diisi")
            return

        sukses = self.db.simpanMember(
            nama, email, telp, pin, foto, password, tgl
        )

        if sukses:
            QMessageBox.information(self, "Sukses", "Data member berhasil disimpan")
            self.load_data()
            self.clear_form()
        else:
            QMessageBox.critical(self, "Gagal", "Gagal menyimpan data")

    # ================= UBAH =================
    def ubah(self):
        QMessageBox.information(
            self, "Info",
            "Fungsi UBAH bisa ditambahkan (update by klik tabel)"
        )

    # ================= HAPUS =================
    def hapus(self):
        row = self.ui.tableWidget.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Pilih Data", "Pilih data dulu")
            return

        kd_member = self.ui.tableWidget.item(row, 0).text()

        try:
            cursor = self.db.koneksi.cursor()
            cursor.execute(
                "DELETE FROM member WHERE kd_member=%s", (kd_member,)
            )
            self.db.koneksi.commit()
            QMessageBox.information(self, "Sukses", "Data berhasil dihapus")
            self.load_data()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    # ================= FILTER =================
    def filter_data(self):
        data = self.db.filterMember(self.ui.cariEdit.text())
        self.load_data(data)

    # ================= CETAK PDF =================
    def cetak_pdf(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Simpan PDF", "", "PDF Files (*.pdf)"
        )
        if path:
            c = canvas.Canvas(path, pagesize=letter)
            c.drawString(100, 750, "LAPORAN DATA MEMBER")

            y = 720
            for row in self.db.cariDataMember():
                c.drawString(
                    100, y,
                    f"{row[0]} | {row[1]} | {row[2]} | {row[3]}"
                )
                y -= 20

            c.save()
            QMessageBox.information(self, "Sukses", "PDF berhasil dibuat")

    # ================= CLEAR FORM =================
    def clear_form(self):
        self.ui.namaMemberLineEdit.clear()
        self.ui.emailLineEdit.clear()
        self.ui.noTeleponLineEdit.clear()
        self.ui.pINBBLineEdit.clear()
        self.ui.pathFotoLineEdit.clear()
        self.ui.passwordLineEdit.clear()
