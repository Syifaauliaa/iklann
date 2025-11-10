# main.py - Disesuaikan untuk Periklanan

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

# Import form yang baru
from iklan import FormIklan
from member import FormMember
from pembayaran import FormPembayaran
from Pesaninbox import FormPesanInbox
# Asumsi: Anda tetap menggunakan ui_form.py/form.ui yang lama
# Jika Anda mengkompilasi form.ui, ubah QUiLoader menjadi import Ui_main

class Main(QMainWindow):
    def __init__(self, parent=None):
        super()._init_(parent)

        # Karena Anda menggunakan QUiLoader di form yang lama (form.ui),
        # kita pertahankan cara ini untuk Main Window, atau ganti jika Anda sudah mengkompilasi form.ui.
        ui_file = QFile("form.ui")
        if not ui_file.open(QFile.ReadOnly): sys.exit(-1)
        loader = QUiLoader()
        self.formUtama = loader.load(ui_file, self)
        ui_file.close()

        self.setCentralWidget(self.formUtama.centralwidget)
        self.setMenuBar(self.formUtama.menuBar())
        self.resize(self.formUtama.size())

        # Sesuaikan koneksi menu action dari form.ui (asumsi Anda sudah mengubah nama action di Qt Designer)
        # Jika Anda tetap menggunakan nama action lama, ubah koneksi di bawah.
        # ASUMSI: actionForm_Dokter -> actionForm_Member, actionForm_Pasien -> actionForm_Iklan, dll.

        try:
            self.formUtama.actionForm_Dokter.triggered.connect(self.bukaMember)
            self.formUtama.actionForm_Pasien.triggered.connect(self.bukaIklan)
            self.formUtama.actionForm_Petugas.triggered.connect(self.bukaPembayaran) # Ganti Petugas
            self.formUtama.actionForm_Obat.triggered.connect(self.bukaPesanInbox)  # Ganti Obat
        except AttributeError:
             print("Pastikan action menu di form.ui sudah diubah namanya (misalnya, actionForm_Member)")

    def bukaMember(self):
        self.memberForm = FormMember()
        self.memberForm.show()

    def bukaIklan(self):
        self.iklanForm = FormIklan()
        self.iklanForm.show()

    def bukaPembayaran(self):
        self.pembayaranForm = FormPembayaran()
        self.pembayaranForm.show()

    def bukaPesanInbox(self):
        self.pesanInboxForm = FormPesanInbox()
        self.pesanInboxForm.show()

if __name__ == '_main_':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
