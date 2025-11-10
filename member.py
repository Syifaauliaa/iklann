# member.py - Mengelola Data Member
import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QLineEdit, QApplication
from PySide6.QtCore import QDate

from ui_form_member import Ui_Form   # pastikan file ini sudah ada
from db import DB


class FormMember(QMainWindow, Ui_Form):
    """Kelas untuk mengelola form dan data Member."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.db = DB()

        self.setWindowTitle("Form Data Member")
        self.tanggalDaftarDateEdit.setDisplayFormat("yyyy-MM-dd")
        self.tanggalDaftarDateEdit.setDate(QDate.currentDate())

        # Hubungkan tombol
        self.pushButton.clicked.connect(self.simpan_data)   # SIMPAN
        self.pushButton_2.clicked.connect(self.ubah_data)   # UBAH
        self.pushButton_3.clicked.connect(self.hapus_data)  # HAPUS
        self.pushButton_4.clicked.connect(self.clear_form)  # CLEAR
        self.tableWidget.cellClicked.connect(self.tabel_diklik)

        self.load_data()

    def load_data(self):
        """Mengambil data dari DB dan menampilkannya di QTableWidget (7 kolom)."""
        data = self.db.cariDataMember()  # pastikan fungsi ini ada di db.py

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(7)
        header_labels = [
            "ID", "NAMA", "EMAIL", "NO TLP",
            "PIN BB", "PATH FOTO", "TANGGAL DAFTAR"
        ]
        self.tableWidget.setHorizontalHeaderLabels(header_labels)

        for row, item in enumerate(data):
            for col, value in enumerate(item):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(value)))

        self.tableWidget.resizeColumnsToContents()

    def simpan_data(self):
        """Mengambil data dari form dan menyimpannya ke database."""
        nama = self.namaMemberLineEdit.text()
        email = self.emailLineEdit.text()
        no_telp = self.noTeleponLineEdit.text()
        pin_bb = self.pINBBLineEdit.text()
        path_foto = self.pathFotoLineEdit.text()
        password = self.passwordLineEdit.text()
        tgl_daftar = self.tanggalDaftarDateEdit.date().toString("yyyy-MM-dd")

        if not all([nama, email, no_telp, password]):
            QMessageBox.warning(self, "Peringatan", "Nama, Email, No Telepon, dan Password wajib diisi!")
            return

        try:
            self.db.simpanMember(nama, email, no_telp, pin_bb, path_foto, password, tgl_daftar)
            QMessageBox.information(self, "Sukses", "Data Member berhasil disimpan!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan data: {e}")

    def ubah_data(self):
        """Mengubah data Member dari tabel."""
        baris = self.tableWidget.currentRow()
        if baris < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang akan diubah!")
            return

        kd_member = self.tableWidget.item(baris, 0).text()
        nama = self.namaMemberLineEdit.text()
        email = self.emailLineEdit.text()
        no_telp = self.noTeleponLineEdit.text()
        pin_bb = self.pINBBLineEdit.text()
        path_foto = self.pathFotoLineEdit.text()
        password = self.passwordLineEdit.text()
        tgl_daftar = self.tanggalDaftarDateEdit.date().toString("yyyy-MM-dd")

        try:
            self.db.ubahMember(kd_member, nama, email, no_telp, pin_bb, path_foto, password, tgl_daftar)
            QMessageBox.information(self, "Sukses", "Data Member berhasil diubah!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal mengubah data: {e}")

    def hapus_data(self):
        """Menghapus data Member dari database."""
        baris = self.tableWidget.currentRow()
        if baris < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang akan dihapus!")
            return

        kd_member = self.tableWidget.item(baris, 0).text()
        confirm = QMessageBox.question(
            self, 'Konfirmasi Hapus',
            f"Yakin ingin menghapus Member ID {kd_member}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            try:
                self.db.hapusMember(kd_member)
                QMessageBox.information(self, "Sukses", "Data Member berhasil dihapus!")
                self.load_data()
                self.clear_form()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal menghapus data: {e}")

    def tabel_diklik(self, row, column):
        """Mengisi form saat baris di tabel diklik."""
        try:
            self.namaMemberLineEdit.setText(self.tableWidget.item(row, 1).text())
            self.emailLineEdit.setText(self.tableWidget.item(row, 2).text())
            self.noTeleponLineEdit.setText(self.tableWidget.item(row, 3).text())
            self.pINBBLineEdit.setText(self.tableWidget.item(row, 4).text())
            self.pathFotoLineEdit.setText(self.tableWidget.item(row, 5).text())
            self.passwordLineEdit.setText("")  # kosongkan password
            tgl_daftar_str = self.tableWidget.item(row, 6).text()
            tgl_daftar = QDate.fromString(tgl_daftar_str, "yyyy-MM-dd")
            self.tanggalDaftarDateEdit.setDate(tgl_daftar)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal mengisi form dari tabel: {e}")

    def clear_form(self):
        """Membersihkan semua input form."""
        self.namaMemberLineEdit.clear()
        self.emailLineEdit.clear()
        self.noTeleponLineEdit.clear()
        self.pINBBLineEdit.clear()
        self.pathFotoLineEdit.clear()
        self.passwordLineEdit.clear()
        self.tanggalDaftarDateEdit.setDate(QDate.currentDate())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FormMember()
    window.show()
    sys.exit(app.exec())
