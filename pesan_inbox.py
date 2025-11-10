# pesan_inbox.py - Mengelola Data Pesan Inbox
import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem


from db import DB

class FormPesanInbox(QMainWindow):
    """
    Kelas untuk mengelola form dan data Pesan Inbox.
    Menggunakan QUiLoader untuk memuat form_pesan_inbox.ui.
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        # 1. Load UI dari form_pesan_inbox.ui
        ui_file = QFile("form_pesan_inbox.ui")
        if not ui_file.open(QFile.ReadOnly):
            QMessageBox.critical(self, "Error", "Gagal membuka form_pesan_inbox.ui. Pastikan file ini ada.")
            sys.exit(-1)

        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        ui_file.close()

        if not self.ui:
            QMessageBox.critical(self, "Error", "Gagal memuat UI Pesan Inbox")
            sys.exit(-1)

        self.setCentralWidget(self.ui.centralwidget)
        self.resize(self.ui.size())
        self.setWindowTitle("Form Data Pesan Inbox")

        # Inisialisasi koneksi database
        self.db = DB()

        # Variabel untuk menyimpan Primary Key dari data yang dipilih di tabel
        self.current_id_pesan = None

        # Promosikan widget UI ke namespace 'self' untuk akses mudah
        self.tanggalKirimDateEdit = self.ui.tanggalKirimDateEdit
        self.namaPengirimLineEdit = self.ui.namaPengirimLineEdit
        self.emailPengirimLineEdit = self.ui.emailPengirimLineEdit
        self.isiPesanLineEdit = self.ui.isiPesanLineEdit
        self.iDMemberLineEdit = self.ui.iDMemberLineEdit
        self.tableWidget = self.ui.tableWidget

        # Hubungkan tombol
        self.ui.pushButton.clicked.connect(self.simpan_data)      # SIMPAN
        self.ui.pushButton_2.clicked.connect(self.ubah_data)     # UBAH
        self.ui.pushButton_3.clicked.connect(self.hapus_data)    # HAPUS
        self.ui.pushButton_4.clicked.connect(self.clear_form)    # CLEAR
        self.tableWidget.cellClicked.connect(self.tabel_diklik)

        # Atur format tanggal
        self.tanggalKirimDateEdit.setDisplayFormat("yyyy-MM-dd")
        self.tanggalKirimDateEdit.setDate(QDate.currentDate())

        self.load_data()

    def load_data(self):
        """Mengambil data dari DB dan menampilkannya di QTableWidget (5 kolom)."""
        # DB Fields: kd_pesan_inx, tgl_kirim_inx, nm_pengirim, email_pengirim, isi_pesan_inx, kd_member
        data = self.db.cariDataPesanInbox()

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(5)

        header_labels = ["ID (PK)", "NAMA", "EMAIL", "ISI PESAN", "ID MEMBER"]
        self.tableWidget.setHorizontalHeaderLabels(header_labels)

        for row, item in enumerate(data):
            # Item index: 0           1           2           3               4               5
            # DB Field:   kd_pesan_inx, tgl_kirim_inx, nm_pengirim, email_pengirim, isi_pesan_inx, kd_member

            # Kolom 0 (ID) <- kd_pesan_inx (PK)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(item[0])))
            # Kolom 1 (NAMA) <- nm_pengirim
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(item[2])))
            # Kolom 2 (EMAIL) <- email_pengirim
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(item[3])))
            # Kolom 3 (ISI PESAN) <- isi_pesan_inx
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(item[4])))
            # Kolom 4 (ID MEMBER) <- kd_member
            self.tableWidget.setItem(row, 4, QTableWidgetItem(str(item[5])))

            # tgl_kirim_inx (DB index 1) tidak ditampilkan di QTableWidget

        self.tableWidget.resizeColumnsToContents()

    def simpan_data(self):
        """Mengambil data dari form dan menyimpannya ke database."""

        tgl_kirim = self.tanggalKirimDateEdit.date().toString("yyyy-MM-dd")
        nm_pengirim = self.namaPengirimLineEdit.text()
        email_pengirim = self.emailPengirimLineEdit.text()
        isi_pesan = self.isiPesanLineEdit.text()
        kd_member = self.iDMemberLineEdit.text()

        if not all([tgl_kirim, nm_pengirim, email_pengirim, isi_pesan, kd_member]):
             QMessageBox.warning(self, "Peringatan", "Semua field wajib diisi!")
             return

        try:
            # Asumsi db.simpanPesanInbox menerima 5 parameter non-PK:
            # (tgl_kirim, nm_pengirim, email_pengirim, isi_pesan, kd_member)
            self.db.simpanPesanInbox(
                tgl_kirim, nm_pengirim, email_pengirim, isi_pesan, kd_member
            )
            QMessageBox.information(self, "Sukses", "Pesan Inbox berhasil disimpan!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan data: {e}")

    def ubah_data(self):
        """Mengubah data Pesan Inbox yang sudah ada di database."""
        # Gunakan self.current_id_pesan yang diisi saat tabel diklik
        id_pesan = self.current_id_pesan

        if not id_pesan:
            QMessageBox.warning(self, "Peringatan", "Pilih data Pesan Inbox yang akan diubah!")
            return

        # Ambil data dari form
        tgl_kirim = self.tanggalKirimDateEdit.date().toString("yyyy-MM-dd")
        nm_pengirim = self.namaPengirimLineEdit.text()
        email_pengirim = self.emailPengirimLineEdit.text()
        isi_pesan = self.isiPesanLineEdit.text()
        kd_member = self.iDMemberLineEdit.text()

        if not all([tgl_kirim, nm_pengirim, email_pengirim, isi_pesan, kd_member]):
             QMessageBox.warning(self, "Peringatan", "Field wajib tidak boleh kosong!")
             return

        try:
            # Asumsi db.ubahPesanInbox menerima 6 parameter (5 data + 1 PK):
            # (id_pesan, tgl_kirim, nm_pengirim, email_pengirim, isi_pesan, kd_member)
            self.db.ubahPesanInbox(
                id_pesan, tgl_kirim, nm_pengirim, email_pengirim, isi_pesan, kd_member
            )
            QMessageBox.information(self, "Sukses", "Pesan Inbox berhasil diubah!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal mengubah data: {e}")

    def hapus_data(self):
        """Menghapus data Pesan Inbox dari database."""
        id_pesan = self.current_id_pesan

        if not id_pesan:
            QMessageBox.warning(self, "Peringatan", "Pilih data Pesan Inbox yang akan dihapus!")
            return

        confirm = QMessageBox.question(self, 'Konfirmasi Hapus',
                                          f"Anda yakin ingin menghapus Pesan Inbox dengan ID: {id_pesan}?",
                                          QMessageBox.Yes | QMessageBox.No)

        if confirm == QMessageBox.Yes:
            try:
                self.db.hapusPesanInbox(id_pesan)
                QMessageBox.information(self, "Sukses", "Pesan Inbox berhasil dihapus!")
                self.load_data()
                self.clear_form()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal menghapus data: {str(e)}")


    def tabel_diklik(self, row, column):
        """Mengisi form saat baris di tabel diklik."""
        try:
            # Ambil ID Pesan (PK) dari kolom 0
            id_pesan = self.tableWidget.item(row, 0).text()
            self.current_id_pesan = id_pesan # Simpan PK di instance variable

            # Ambil data lengkap dari database menggunakan ID
            data_lengkap = self.db.cariDataPesanInboxById(id_pesan)

            if data_lengkap:
                data = data_lengkap[0]
                # DB Field: kd_pesan_inx, tgl_kirim_inx, nm_pengirim, email_pengirim, isi_pesan_inx, kd_member

                tgl_kirim_str = str(data[1])

                # Mengisi LineEdit
                self.namaPengirimLineEdit.setText(str(data[2]))
                self.emailPengirimLineEdit.setText(str(data[3]))
                self.isiPesanLineEdit.setText(str(data[4]))
                self.iDMemberLineEdit.setText(str(data[5]))

                # Mengisi QDateEdit
                tgl_kirim = QDate.fromString(tgl_kirim_str, "yyyy-MM-dd")
                self.tanggalKirimDateEdit.setDate(tgl_kirim)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal mengisi form dari tabel: {e}")

    def clear_form(self):
        """Membersihkan semua field input dan mereset ID terpilih."""
        self.tanggalKirimDateEdit.setDate(QDate.currentDate())
        self.namaPengirimLineEdit.clear()
        self.emailPengirimLineEdit.clear()
        self.isiPesanLineEdit.clear()
        self.iDMemberLineEdit.clear()
        self.current_id_pesan = None


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = FormPesanInbox()
    window.show()
    sys.exit(app.exec())
