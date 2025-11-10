# iklan.py - Mengelola Data Iklan
import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QDate
from db import DB
# Asumsi: Anda telah mengkompilasi form_iklan.ui menjadi ui_form_iklan.py
from ui_form_iklan import Ui_Form


class FormIklan(QMainWindow, Ui_Form):
    """
    Kelas untuk mengelola form dan data Iklan.
    Menggunakan kelas UI yang sudah dikompilasi (Ui_MainWindow).
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.db = DB()

        # Inisialisasi widget
        self.setWindowTitle("Form Data Iklan")
        self.tanggalPasangDateEdit.setDisplayFormat("yyyy-MM-dd")

        # Isi ComboBox (Asumsi nilai default)
        self.kondisiComboBox.addItems(["Baru", "Bekas"])
        self.statusAktifComboBox.addItems(["Aktif", "Tidak Aktif"])

        # Hubungkan tombol
        self.pushButton.clicked.connect(self.simpan_data)      # SIMPAN
        self.pushButton_2.clicked.connect(self.ubah_data)     # UBAH
        self.pushButton_3.clicked.connect(self.hapus_data)    # HAPUS
        self.pushButton_4.clicked.connect(self.clear_form)    # CLEAR
        self.tableWidget.cellClicked.connect(self.tabel_diklik)

        self.load_data()

    def load_data(self):
        """Mengambil data dari DB dan menampilkannya di QTableWidget."""
        # Asumsi db.cariDataIklan() mengembalikan 12 kolom
        data = self.db.cariDataIklan()

        # Set jumlah baris dan kolom (12 kolom)
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(12)

        header_labels = [
            "kd_iklan", "kd_member", "tgl_pasang", "judul_iklan",
            "kondisi", "status_aktif", "nama_jalan", "gambar1",
            "gambar2", "gambar3", "harga", "deskripsi"
        ]
        self.tableWidget.setHorizontalHeaderLabels(header_labels)

        for row, item in enumerate(data):
            for col, value in enumerate(item):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(value)))

    def simpan_data(self):
        """Mengambil data dari form dan menyimpannya ke database."""
        # Ambil data dari widget (Asumsi kd_iklanLineEdit ada di UI)
        try:
            kd_iklan = self.kd_iklanLineEdit.text()
        except AttributeError:
             QMessageBox.critical(self, "Error UI", "Tambahkan kd_iklanLineEdit ke form!")
             return

        kd_member = self.iDMemberLineEdit.text()
        tgl_pasang = self.tanggalPasangDateEdit.date().toString("yyyy-MM-dd")
        judul = self.judulIklanLineEdit.text()
        kondisi = self.kondisiComboBox.currentText()
        status_aktif = self.statusAktifComboBox.currentText()
        nama_jalan = self.namaJalanLineEdit.text()
        gbr1 = self.gambar1LineEdit.text()
        gbr2 = self.gambar2LineEdit.text()
        gbr3 = self.gambar3LineEdit.text()
        harga = self.hargaLineEdit.text()
        deskripsi = self.deskripsiLineEdit.text()

        if not all([kd_iklan, kd_member, judul, harga]):
             QMessageBox.warning(self, "Peringatan", "Kode Iklan, ID Member, Judul, dan Harga wajib diisi!")
             return

        try:
            # Asumsi db.py sudah diupdate untuk menerima 12 parameter
            self.db.simpanIklan(
                kd_iklan, kd_member, tgl_pasang, judul, kondisi, status_aktif,
                nama_jalan, gbr1, gbr2, gbr3, harga, deskripsi
            )
            QMessageBox.information(self, "Sukses", "Data Iklan berhasil disimpan!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan data: {e}")

    def ubah_data(self):
        """Mengubah data Iklan yang sudah ada di database."""
        try:
            kd_iklan = self.kd_iklanLineEdit.text()
        except AttributeError: return

        if not kd_iklan:
            QMessageBox.warning(self, "Peringatan", "Pilih data Iklan yang akan diubah!")
            return

        # Ambil data dari widget
        kd_member = self.iDMemberLineEdit.text()
        tgl_pasang = self.tanggalPasangDateEdit.date().toString("yyyy-MM-dd")
        judul = self.judulIklanLineEdit.text()
        kondisi = self.kondisiComboBox.currentText()
        status_aktif = self.statusAktifComboBox.currentText()
        nama_jalan = self.namaJalanLineEdit.text()
        gbr1 = self.gambar1LineEdit.text()
        gbr2 = self.gambar2LineEdit.text()
        gbr3 = self.gambar3LineEdit.text()
        harga = self.hargaLineEdit.text()
        deskripsi = self.deskripsiLineEdit.text()

        if not all([kd_member, judul, harga]):
             QMessageBox.warning(self, "Peringatan", "Field wajib tidak boleh kosong!")
             return

        try:
            # Asumsi db.py sudah diupdate untuk menerima 12 parameter
            self.db.ubahIklan(
                kd_iklan, kd_member, tgl_pasang, judul, kondisi, status_aktif,
                nama_jalan, gbr1, gbr2, gbr3, harga, deskripsi
            )
            QMessageBox.information(self, "Sukses", "Data Iklan berhasil diubah!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal mengubah data: {e}")

    def hapus_data(self):
        """Menghapus data Iklan dari database."""
        try:
            kd_iklan = self.kd_iklanLineEdit.text()
        except AttributeError: return

        if not kd_iklan:
            QMessageBox.warning(self, "Peringatan", "Pilih data Iklan yang akan dihapus!")
            return

        confirm = QMessageBox.question(self, 'Konfirmasi Hapus',
                                          f"Anda yakin ingin menghapus Iklan dengan Kode: {kd_iklan}?",
                                          QMessageBox.Yes | QMessageBox.No)

        if confirm == QMessageBox.Yes:
            try:
                self.db.hapusIklan(kd_iklan)
                QMessageBox.information(self, "Sukses", "Data Iklan berhasil dihapus!")
                self.load_data()
                self.clear_form()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal menghapus data: {str(e)}")


    def tabel_diklik(self, row, column):
        """Mengisi form saat baris di tabel diklik."""
        try:
            # Ambil semua data dari baris yang diklik (12 kolom)
            kd_iklan_str = self.tableWidget.item(row, 0).text()
            kd_member_str = self.tableWidget.item(row, 1).text()
            tgl_pasang_str = self.tableWidget.item(row, 2).text()
            judul_str = self.tableWidget.item(row, 3).text()
            kondisi_str = self.tableWidget.item(row, 4).text()
            status_aktif_str = self.tableWidget.item(row, 5).text()
            nama_jalan_str = self.tableWidget.item(row, 6).text()
            gbr1_str = self.tableWidget.item(row, 7).text()
            gbr2_str = self.tableWidget.item(row, 8).text()
            gbr3_str = self.tableWidget.item(row, 9).text()
            harga_str = self.tableWidget.item(row, 10).text()
            deskripsi_str = self.tableWidget.item(row, 11).text()

            # Mengisi LineEdit/Text
            self.kd_iklanLineEdit.setText(kd_iklan_str) # Asumsi LineEdit ini ada
            self.iDMemberLineEdit.setText(kd_member_str)
            self.judulIklanLineEdit.setText(judul_str)
            self.namaJalanLineEdit.setText(nama_jalan_str)
            self.gambar1LineEdit.setText(gbr1_str)
            self.gambar2LineEdit.setText(gbr2_str)
            self.gambar3LineEdit.setText(gbr3_str)
            self.hargaLineEdit.setText(harga_str)
            self.deskripsiLineEdit.setText(deskripsi_str)

            # Mengisi QDateEdit
            tgl_pasang = QDate.fromString(tgl_pasang_str, "yyyy-MM-dd")
            self.tanggalPasangDateEdit.setDate(tgl_pasang)

            # Mengisi QComboBox
            index_kondisi = self.kondisiComboBox.findText(kondisi_str)
            if index_kondisi >= 0:
                self.kondisiComboBox.setCurrentIndex(index_kondisi)

            index_status = self.statusAktifComboBox.findText(status_aktif_str)
            if index_status >= 0:
                self.statusAktifComboBox.setCurrentIndex(index_status)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal mengisi form dari tabel: {e}")

    def clear_form(self):
        """Membersihkan semua field input."""
        try:
            self.kd_iklanLineEdit.clear() # Asumsi LineEdit ini ada
        except AttributeError:
            pass # Lanjutkan jika widget tidak ditemukan

        self.iDMemberLineEdit.clear()
        self.judulIklanLineEdit.clear()
        self.namaJalanLineEdit.clear()
        self.gambar1LineEdit.clear()
        self.gambar2LineEdit.clear()
        self.gambar3LineEdit.clear()
        self.hargaLineEdit.clear()
        self.deskripsiLineEdit.clear()
        self.tanggalPasangDateEdit.setDate(QDate.currentDate())
        self.kondisiComboBox.setCurrentIndex(0)
        self.statusAktifComboBox.setCurrentIndex(0)
