import mysql.connector
from mysql.connector import Error


class DB:
    def __init__(self):
        try:
            self.koneksi = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="periklanan"
            )
            self.cursor = self.koneksi.cursor()
            print("✔ Terhubung ke database periklanan")
        except Error as e:
            print("❌ Error Database:", e)
            self.koneksi = None

    # =====================================================
    # MODUL MEMBER
    # =====================================================
    def cariDataMember(self):
        try:
            self.cursor.execute("""
                SELECT kd_member, nm_member, alamat_email,
                       tlp_mbr, pin_bb, foto, tgl_daftar
                FROM member
            """)
            return self.cursor.fetchall()
        except Error as e:
            print("Error Member:", e)
            return []

    def filterMember(self, keyword):
        try:
            self.cursor.execute("""
                SELECT * FROM member
                WHERE nm_member LIKE %s OR kd_member LIKE %s
            """, (f"%{keyword}%", f"%{keyword}%"))
            return self.cursor.fetchall()
        except Error:
            return []

    def simpanMember(self, nama, email, telp, pin, foto, password, tgl):
        try:
            self.cursor.execute("""
                INSERT INTO member
                (nm_member, alamat_email, tlp_mbr, pin_bb, foto, password, tgl_daftar)
                VALUES (%s,%s,%s,%s,%s,%s,%s)
            """, (nama, email, telp, pin, foto, password, tgl))
            self.koneksi.commit()
            return True
        except Error as e:
            print("Error Simpan Member:", e)
            return False

    # =====================================================
    # MODUL IKLAN  ✅ (SUDAH FIX TOTAL)
    # =====================================================
    def cariDataIklan(self):
        try:
            self.cursor.execute("""
                SELECT kd_iklan, kd_member, tgl_pasang,
                       judul_iklan, kondisi, status_aktif,
                       nama_jalan, gambar1, gambar2,
                       gambar3, harga, deskripsi
                FROM iklan
            """)
            return self.cursor.fetchall()
        except Error as e:
            print("Error Iklan:", e)
            return []

    def filterIklan(self, keyword):
        try:
            self.cursor.execute("""
                SELECT * FROM iklan
                WHERE judul_iklan LIKE %s OR kd_iklan LIKE %s
            """, (f"%{keyword}%", f"%{keyword}%"))
            return self.cursor.fetchall()
        except Error:
            return []

    def simpanIklan(
        self, kd_member, tgl, judul, kondisi, status,
        jalan, g1, g2, g3, harga, desk
    ):
        try:
            self.cursor.execute("""
                INSERT INTO iklan
                (kd_member, tgl_pasang, judul_iklan, kondisi,
                 status_aktif, nama_jalan,
                 gambar1, gambar2, gambar3,
                 harga, deskripsi)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, (
                kd_member, tgl, judul, kondisi, status,
                jalan, g1, g2, g3, harga, desk
            ))
            self.koneksi.commit()
            return True
        except Error as e:
            print("Error Simpan Iklan:", e)
            return False

    def hapusIklan(self, kd_iklan):
        try:
            self.cursor.execute(
                "DELETE FROM iklan WHERE kd_iklan=%s", (kd_iklan,)
            )
            self.koneksi.commit()
        except Error as e:
            print("Error Hapus Iklan:", e)

    # =====================================================
    # MODUL PEMBAYARAN
    # =====================================================
    def cariDataPembayaran(self):
        try:
            self.cursor.execute("""
                SELECT id_bayar, kode_transfer, no_rek,
                       nam_rek, nominal, kd_iklan
                FROM pembayaran
            """)
            return self.cursor.fetchall()
        except Error:
            return []

    def simpanPembayaran(self, kode, norek, nama, nominal, kd_iklan):
        try:
            self.cursor.execute("""
                INSERT INTO pembayaran
                (kode_transfer, no_rek, nam_rek, nominal, kd_iklan)
                VALUES (%s,%s,%s,%s,%s)
            """, (kode, norek, nama, nominal, kd_iklan))
            self.koneksi.commit()
            return True
        except Error as e:
            print("Error Pembayaran:", e)
            return False

    # =====================================================
    # MODUL PESAN INBOX
    # =====================================================
    def cariDataPesanInbox(self):
        try:
            self.cursor.execute("""
                SELECT kd_pesan_inx, tgl_kirim_inx,
                       nm_pengirim, email_pengirim,
                       isi_pesan_inx, kd_member
                FROM pesan_inbox
            """)
            return self.cursor.fetchall()
        except Error:
            return []

    def simpanPesanInbox(self, tgl, nama, email, isi, kd_member):
        try:
            self.cursor.execute("""
                INSERT INTO pesan_inbox
                (tgl_kirim_inx, nm_pengirim, email_pengirim,
                 isi_pesan_inx, kd_member)
                VALUES (%s,%s,%s,%s,%s)
            """, (tgl, nama, email, isi, kd_member))
            self.koneksi.commit()
            return True
        except Error as e:
            print("Error Inbox:", e)
            return False

    def close(self):
        if self.koneksi:
            self.koneksi.close()
            print("Koneksi ditutup")
