import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from member import FormMember
from iklan import FormIklan
from pembayaran import FormPembayaran
from pesan_inbox import FormPesanInbox


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        # ===============================
        # LOAD UI (form.ui HARUS QWidget)
        # ===============================
        loader = QUiLoader()
        ui_file = QFile("form.ui")

        if not ui_file.open(QFile.ReadOnly):
            print("❌ Gagal membuka form.ui")
            sys.exit(1)

        self.ui = loader.load(ui_file)
        ui_file.close()

        if self.ui is None:
            print("❌ UI gagal diload")
            sys.exit(1)

        # ===============================
        # SET SEBAGAI CENTRAL WIDGET
        # ===============================
        self.setCentralWidget(self.ui)
        self.resize(self.ui.size())
        self.setWindowTitle("Aplikasi Periklanan")

        # ===============================
        # HUBUNGKAN ACTION MENU (FIX)
        # ===============================
        self.hubungkan_menu()

    # =====================================================
    # HUBUNGKAN SEMUA ACTION DALAM MENU BAR
    # =====================================================
    def hubungkan_menu(self):
        menu_bar = self.ui.menuBar()

        for menu in menu_bar.findChildren(QMenu):
            for action in menu.actions():
                teks = action.text().lower()

                if "member" in teks:
                    action.triggered.connect(self.bukaMember)

                elif "iklan" in teks:
                    action.triggered.connect(self.bukaIklan)

                elif "pembayaran" in teks:
                    action.triggered.connect(self.bukaPembayaran)

                elif "pesan" in teks or "inbox" in teks:
                    action.triggered.connect(self.bukaPesanInbox)

    # ===============================
    # OPEN FORM
    # ===============================
    def bukaMember(self):
        self.formMember = FormMember()
        self.formMember.show()

    def bukaIklan(self):
        self.formIklan = FormIklan()
        self.formIklan.show()

    def bukaPembayaran(self):
        self.formPembayaran = FormPembayaran()
        self.formPembayaran.show()

    def bukaPesanInbox(self):
        self.formPesanInbox = FormPesanInbox()
        self.formPesanInbox.show()


# ===============================
# MAIN PROGRAM
# ===============================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
