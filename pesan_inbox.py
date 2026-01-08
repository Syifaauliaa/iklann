from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidgetItem,
    QMessageBox, QFileDialog
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDate
from db import DB

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class FormPesanInbox(QWidget):
    def __init__(self):
        super().__init__()

        # ===== LOAD UI =====
        loader = QUiLoader()
        ui_file = QFile("form_pesan_inbox.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        layout = QVBoxLayout(self)
        layout.addWidget(self.ui)

        self.db = DB()
        self.old_data = {}

        # ===== AMBIL WIDGET =====
        self.table = self.ui.findChild(type(self.ui.tableWidget), "tableWidget")

        self.btn_simpan = self.ui.findChild(type(self.ui.simpanBtn), "simpanBtn")
        self.btn_ubah = self.ui.findChild(type(self.ui.ubahBtn), "ubahBtn")
        self.btn_hapus = self.ui.findChild(type(self.ui.hapusBtn), "hapusBtn")
        self.btn_cetak = self.ui.findChild(type(self.ui.cetakBtn), "cetakBtn")

        self.cari_edit = self.ui.findChild(type(self.ui.cariEdit), "cariEdit")

        self.tgl = self.ui.findChild(type(self.ui.tanggalKirimDateEdit), "tanggalKirimDateEdit")
        self.nama = self.ui.findChild(type(self.ui.linePengirim), "linePengirim")
        self.email = self.ui.findChild(type(self.ui.emailPengirimLineEdit), "emailPengirimLineEdit")
        self.isi = self.ui.findChild(type(self.ui.lineIsi), "lineIsi")
        self.id_member = self.ui.findChild(type(self.ui.iDMemberLineEdit), "iDMemberLineEdit")

        # ===== KONEKSI =====
        self.btn_simpan.clicked.connect(self.simpan)
        self.btn_ubah.clicked.connect(self.ubah)
        self.btn_hapus.clicked.connect(self.hapus)
        self.btn_cetak.clicked.connect(self.cetak_pdf)
        self.cari_edit.textChanged.connect(self.filter_data)
        self.table.cellClicked.connect(self.isi_form_dari_tabel)

        self.load_data()

    # ================= LOAD DATA =================
    def load_data(self, data=None):
        if data is None:
            data = self.db.cariDataPesanInbox()

        self.table.setRowCount(len(data))
        for r, row in enumerate(data):
            for c, val in enumerate(row):
                self.table.setItem(r, c, QTableWidgetItem(str(val)))

    # ================= SIMPAN =================
    def simpan(self):
        tgl = self.tgl.date().toString("yyyy-MM-dd")
        nama = self.nama.text()
        email = self.email.text()
        isi = self.isi.text()
        id_member = self.id_member.text()

        if nama == "" or isi == "":
            QMessageBox.warning(self, "Validasi", "Nama dan isi pesan wajib diisi")
            return

        sukses = self.db.simpanPesanInbox(
            tgl, nama, email, isi, id_member
        )

        if sukses:
            QMessageBox.information(self, "Sukses", "Data berhasil disimpan")
            self.load_data()
            self.clear_form()
        else:
            QMessageBox.critical(self, "Gagal", "Gagal menyimpan data")

    # ================= ISI FORM DARI TABEL =================
    def isi_form_dari_tabel(self, row, col):
        self.old_data = {
            "tanggal": self.table.item(row, 0).text(),
            "nama": self.table.item(row, 1).text(),
            "email": self.table.item(row, 2).text(),
            "isi": self.table.item(row, 3).text(),
            "id_member": self.table.item(row, 4).text()
        }

        self.tgl.setDate(QDate.fromString(self.old_data["tanggal"], "yyyy-MM-dd"))
        self.nama.setText(self.old_data["nama"])
        self.email.setText(self.old_data["email"])
        self.isi.setText(self.old_data["isi"])
        self.id_member.setText(self.old_data["id_member"])

    # ================= UBAH =================
    def ubah(self):
        if not self.old_data:
            QMessageBox.warning(self, "Pilih Data", "Pilih data dari tabel dulu")
            return

        try:
            cursor = self.db.koneksi.cursor()
            cursor.execute(
                """
                UPDATE pesan_inbox SET
                    tanggal_kirim=%s,
                    nama_pengirim=%s,
                    email_pengirim=%s,
                    isi_pesan=%s,
                    id_member=%s
                WHERE
                    tanggal_kirim=%s AND
                    nama_pengirim=%s AND
                    email_pengirim=%s
                """,
                (
                    self.tgl.date().toString("yyyy-MM-dd"),
                    self.nama.text(),
                    self.email.text(),
                    self.isi.text(),
                    self.id_member.text(),
                    self.old_data["tanggal"],
                    self.old_data["nama"],
                    self.old_data["email"]
                )
            )
            self.db.koneksi.commit()
            QMessageBox.information(self, "Sukses", "Data berhasil diubah")
            self.load_data()
            self.clear_form()
            self.old_data = {}
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    # ================= HAPUS =================
    def hapus(self):
        if not self.old_data:
            QMessageBox.warning(self, "Pilih Data", "Pilih data dulu")
            return

        jawab = QMessageBox.question(
            self, "Konfirmasi",
            "Yakin ingin menghapus data ini?",
            QMessageBox.Yes | QMessageBox.No
        )

        if jawab == QMessageBox.Yes:
            try:
                cursor = self.db.koneksi.cursor()
                cursor.execute(
                    """
                    DELETE FROM pesan_inbox
                    WHERE tanggal_kirim=%s
                    AND nama_pengirim=%s
                    AND email_pengirim=%s
                    """,
                    (
                        self.old_data["tanggal"],
                        self.old_data["nama"],
                        self.old_data["email"]
                    )
                )
                self.db.koneksi.commit()
                QMessageBox.information(self, "Sukses", "Data berhasil dihapus")
                self.load_data()
                self.clear_form()
                self.old_data = {}
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    # ================= FILTER =================
    def filter_data(self):
        data = self.db.filterPesanInbox(self.cari_edit.text())
        self.load_data(data)

    # ================= CETAK PDF =================
    def cetak_pdf(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Simpan PDF", "", "PDF Files (*.pdf)"
        )
        if not path:
            return

        c = canvas.Canvas(path, pagesize=letter)
        c.drawString(100, 750, "LAPORAN PESAN INBOX")

        y = 720
        for row in self.db.cariDataPesanInbox():
            c.drawString(
                50, y,
                f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}"
            )
            y -= 20
            if y < 50:
                c.showPage()
                y = 750

        c.save()
        QMessageBox.information(self, "Sukses", "PDF berhasil dibuat")

    # ================= CLEAR FORM =================
    def clear_form(self):
        self.nama.clear()
        self.email.clear()
        self.isi.clear()
        self.id_member.clear()
