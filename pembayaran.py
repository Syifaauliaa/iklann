# pembayaran.py - Mengelola Data Pembayaran
import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader # Menggunakan QUiLoader seperti form Anda yang lain

from db import DB

# Asumsi: Menggunakan QUiLoader seperti file main.py, dokter.py, dll.
class FormPembayaran(QMainWindow):
    """
    Kelas untuk mengelola form dan data Pembayaran.
    Menggunakan QUiLoader untuk memuat form_pembayaran.ui.
    """
    def __init__(self, parent=None):
        super().__init___(parent)

        # 1. Load UI dari form_pembayaran.ui
        ui_file = QFile("form_pembayaran.ui")
        if not ui_file.open(QFile.ReadOnly):
            print("Gagal membuka form_pembayaran.ui. Pastikan file ini ada.")
            sys.exit(-1)

        loader = QUiLoader()
        # Muat UI
        self.ui = loader.load(ui_file)
        ui_file.close()

        if not self.ui:
            print("Gagal memuat UI Pembayaran")
            sys.exit(-1)

        # Pindahkan central widget ke objek FormPembayaran (self)
        self.setCentralWidget(self.ui.centralwidget)
        self.resize(self.ui.size())
        self.setWindowTitle("Form Data Pembayaran")

        # Inisialisasi koneksi database
        self.db = DB()

        # Promosikan widget UI ke namespace 'self' untuk akses mudah (konsisten dengan pasien.py)
        self.kodeTransferLineEdit = self.ui.kodeTransferLineEdit
        self.noRekeningLineEdit = self.ui.noRekeningLineEdit
        self.namaPemilikRekLineEdit = self.ui.namaPemilikRekLineEdit
        self.nominalLineEdit = self.ui.nominalLineEdit
        self.iDIklanLineEdit = self.ui.iDIklanLineEdit
        self.tableWidget = self.ui.tableWidget

        # Hubungkan tombol
        self.ui.pushButton.clicked.connect(self.simpan_data)      # SIMPAN
        self.ui.pushButton_2.clicked.connect(self.ubah_data)     # UBAH
        self.ui.pushButton_3.clicked.connect(self.hapus_data)    # HAPUS
        self.ui.pushButton_4.clicked.connect(self.clear_form)    # CLEAR
        self.tableWidget.cellClicked.connect(self.tabel_diklik)

        # Atur agar field ID tidak bisa diubah user, hanya diisi dari tabel
        self.kodeTransferLineEdit.setEnabled(False)

        self.load_data()

    def load_data(self):
        """Mengambil data dari DB dan menampilkannya di QTableWidget (5 kolom)."""
        data = self.db.cariDataPembayaran()

        # Kolom di tabel UI: ID, REKENING, KODE, NAMA, ID IKLAN
        # Kolom di DB: id_bayar, no_rekening, kode_transfer, nama_pemilik_rek, nominal, id_iklan
        # Ada 6 kolom data di DB, tapi tabel Anda hanya 5. Nominal akan diabaikan di tabel

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(5)

        header_labels = [
            "ID (PK)", "REKENING", "KODE TRANSFER", "NAMA PEMILIK", "ID IKLAN"
        ]
        self.tableWidget.setHorizontalHeaderLabels(header_labels)

        for row, item in enumerate(data):
            # Mapping Data DB (6 kolom) ke Tabel UI (5 kolom):
            # DB Index: 0       1           2               3                   4       5
            # DB Field: id_bayar, no_rek, kode_transfer, nama_pemilik_rek, nominal, id_iklan

            # Table Column: 0       1       2       3           4
            # Table Field: ID (PK), NO REK, KODE TR, NAMA PEM, ID IKLAN

            # Kolom 0 (ID) <- id_bayar (DB index 0)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(item[0])))
            # Kolom 1 (REKENING) <- no_rekening (DB index 1)
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(item[1])))
            # Kolom 2 (KODE) <- kode_transfer (DB index 2)
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(item[2])))
            # Kolom 3 (NAMA) <- nama_pemilik_rek (DB index 3)
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(item[3])))
            # Kolom 4 (ID IKLAN) <- id_iklan (DB index 5)
            self.tableWidget.setItem(row, 4, QTableWidgetItem(str(item[5])))

            # Nominal (DB index 4) tidak ditampilkan di QTableWidget Anda, tapi akan di-load saat tabel diklik.

        self.tableWidget.resizeColumnsToContents()

    def simpan_data(self):
        """Mengambil data dari form dan menyimpannya ke database."""
        # id_bayar diabaikan karena AUTO_INCREMENT
        kode_transfer = self.kodeTransferLineEdit.text() # Di UI dinamakan kodeTransfer, tapi isinya PK, jadi kita pakai isiannya utk kode transfer
        no_rekening = self.noRekeningLineEdit.text()
        nama_pemilik_rek = self.namaPemilikRekLineEdit.text()
        nominal = self.nominalLineEdit.text()
        id_iklan = self.iDIklanLineEdit.text()

        if not all([no_rekening, nama_pemilik_rek, nominal, id_iklan]):
             QMessageBox.warning(self, "Peringatan", "Semua field wajib diisi!")
             return

        try:
            # Pastikan nominal adalah angka
            nominal_val = float(nominal)
        except ValueError:
            QMessageBox.warning(self, "Peringatan", "Nominal harus berupa angka!")
            return

        try:
            # Asumsi db.simpanPembayaran menerima 5 parameter non-PK:
            # (kode_transfer, no_rekening, nama_pemilik_rek, nominal, id_iklan)
            self.db.simpanPembayaran(
                kode_transfer, no_rekening, nama_pemilik_rek, nominal_val, id_iklan
            )
            QMessageBox.information(self, "Sukses", "Data Pembayaran berhasil disimpan!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan data: {e}")

    def ubah_data(self):
        """Mengubah data Pembayaran yang sudah ada di database."""
        id_bayar = self.kodeTransferLineEdit.text() # Diambil dari LineEdit yang sebelumnya berisi PK

        if not id_bayar:
            QMessageBox.warning(self, "Peringatan", "Pilih data Pembayaran yang akan diubah!")
            return

        # Ambil data dari widget
        kode_transfer = self.kodeTransferLineEdit.text()
        no_rekening = self.noRekeningLineEdit.text()
        nama_pemilik_rek = self.namaPemilikRekLineEdit.text()
        nominal = self.nominalLineEdit.text()
        id_iklan = self.iDIklanLineEdit.text()

        if not all([no_rekening, nama_pemilik_rek, nominal, id_iklan]):
             QMessageBox.warning(self, "Peringatan", "Field wajib tidak boleh kosong!")
             return

        try:
            nominal_val = float(nominal)
        except ValueError:
            QMessageBox.warning(self, "Peringatan", "Nominal harus berupa angka!")
            return

        try:
            # Asumsi db.ubahPembayaran menerima 6 parameter (5 data + 1 PK):
            # (id_bayar, kode_transfer, no_rekening, nama_pemilik_rek, nominal, id_iklan)
            self.db.ubahPembayaran(
                id_bayar, kode_transfer, no_rekening, nama_pemilik_rek, nominal_val, id_iklan
            )
            QMessageBox.information(self, "Sukses", "Data Pembayaran berhasil diubah!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal mengubah data: {e}")

    def hapus_data(self):
        """Menghapus data Pembayaran dari database."""
        id_bayar = self.kodeTransferLineEdit.text()

        if not id_bayar:
            QMessageBox.warning(self, "Peringatan", "Pilih data Pembayaran yang akan dihapus!")
            return

        confirm = QMessageBox.question(self, 'Konfirmasi Hapus',
                                          f"Anda yakin ingin menghapus Pembayaran dengan ID: {id_bayar}?",
                                          QMessageBox.Yes | QMessageBox.No)

        if confirm == QMessageBox.Yes:
            try:
                self.db.hapusPembayaran(id_bayar)
                QMessageBox.information(self, "Sukses", "Data Pembayaran berhasil dihapus!")
                self.load_data()
                self.clear_form()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal menghapus data: {str(e)}")


    def tabel_diklik(self, row, column):
        """Mengisi form saat baris di tabel diklik."""
        try:
            # Ambil ID Bayar (PK) dari kolom 0
            id_bayar = self.tableWidget.item(row, 0).text()

            # Ambil data lengkap dari database menggunakan ID
            data_lengkap = self.db.cariDataPembayaranById(id_bayar)

            if data_lengkap:
                data = data_lengkap[0]
                # DB Field: id_bayar, no_rekening, kode_transfer, nama_pemilik_rek, nominal, id_iklan

                # Mengisi LineEdit
                self.kodeTransferLineEdit.setText(str(data[0])) # id_bayar (PK)
                self.noRekeningLineEdit.setText(str(data[1]))
                # Mengisi kodeTransferLineEdit dengan data kode_transfer (DB index 2)
                # Catatan: Karena UI hanya punya 1 LineEdit untuk Kode Transfer (kodeTransferLineEdit),
                # kita akan menggunakan LineEdit ini untuk menampung id_bayar (PK) dan
                # menampilkannya di tabel. Di sini kita memuat id_bayar, bukan kode_transfer.
                # Jika Anda ingin kode transfer ditampilkan di form, Anda harus menambahkan
                # LineEdit baru di form UI Anda.

                # Sesuai form UI: Kode Transfer Label menunjuk ke kodeTransferLineEdit
                # dan digunakan sebagai PK saat ubah/hapus. Kita tetap isi dengan id_bayar (PK)
                # untuk memastikan fungsi Ubah dan Hapus berjalan.

                self.namaPemilikRekLineEdit.setText(str(data[3]))
                self.nominalLineEdit.setText(str(data[4]))
                self.iDIklanLineEdit.setText(str(data[5]))

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal mengisi form dari tabel: {e}")

    def clear_form(self):
        """Membersihkan semua field input."""
        self.kodeTransferLineEdit.clear()
        self.noRekeningLineEdit.clear()
        self.namaPemilikRekLineEdit.clear()
        self.nominalLineEdit.clear()
        self.iDIklanLineEdit.clear()


if __name__ == '__main__':
    # Ini adalah contoh menjalankan form secara mandiri
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = FormPembayaran()
    window.show()
    sys.exit(app.exec())
