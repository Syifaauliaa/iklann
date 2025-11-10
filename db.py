# db.py - Disesuaikan untuk database 'periklanan'

import mysql.connector

class DB:
    def _init_(self):
        # PASTIKAN nama database di sini sesuai
        self.koneksi = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='periklanan'  # <-- PERUBAHAN
        )

    # =================================================================
    # CRUD UNTUK MEMBER (kd_member, nm_member, email, no_telp, username, password)
    # =================================================================

    def simpanMember(self, kd, nama, email, telp, username, password):
        cursor = self.koneksi.cursor()
        sql = """INSERT INTO member
                 (kd_member, nm_member, email, no_telp, username, password)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (kd, nama, email, telp, username, password))
        self.koneksi.commit()
        cursor.close()

    def ubahMember(self, kd, nama, email, telp, username, password):
        cursor = self.koneksi.cursor()
        sql = """UPDATE member SET
                    nm_member=%s, email=%s, no_telp=%s, username=%s, password=%s
                 WHERE kd_member=%s"""
        cursor.execute(sql, (nama, email, telp, username, password, kd))
        self.koneksi.commit()
        cursor.close()

    def hapusMember(self, kd):
        cursor = self.koneksi.cursor()
        sql = "DELETE FROM member WHERE kd_member=%s"
        cursor.execute(sql, (kd,))
        self.koneksi.commit()
        cursor.close()

    def cariDataMember(self):
        cursor = self.koneksi.cursor()
        cursor.execute("SELECT kd_member, nm_member, email, no_telp, username, password FROM member")
        hasil = cursor.fetchall()
        cursor.close()
        return hasil

    # =================================================================
    # CRUD UNTUK IKLAN (kd_iklan, kd_member, tgl_pasang, judul_iklan, kondisi, status_aktif)
    # =================================================================

    def simpanIklan(self, kd_iklan, kd_member, tgl_pasang, judul, kondisi, status_aktif):
        cursor = self.koneksi.cursor()
        sql = """INSERT INTO iklan
                 (kd_iklan, kd_member, tgl_pasang, judul_iklan, kondisi, status_aktif)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (kd_iklan, kd_member, tgl_pasang, judul, kondisi, status_aktif))
        self.koneksi.commit()
        cursor.close()

    def ubahIklan(self, kd_iklan, kd_member, tgl_pasang, judul, kondisi, status_aktif):
        cursor = self.koneksi.cursor()
        sql = """UPDATE iklan SET
                    kd_member=%s, tgl_pasang=%s, judul_iklan=%s, kondisi=%s, status_aktif=%s
                 WHERE kd_iklan=%s"""
        cursor.execute(sql, (kd_member, tgl_pasang, judul, kondisi, status_aktif, kd_iklan))
        self.koneksi.commit()
        cursor.close()

    def hapusIklan(self, kd_iklan):
        cursor = self.koneksi.cursor()
        sql = "DELETE FROM iklan WHERE kd_iklan=%s"
        # Catatan: Perlu cek apakah ada foreign key constraint (misal di pembayaran)
        cursor.execute(sql, (kd_iklan,))
        self.koneksi.commit()
        cursor.close()

    def cariDataIklan(self):
        cursor = self.koneksi.cursor()
        cursor.execute("SELECT kd_iklan, kd_member, tgl_pasang, judul_iklan, kondisi, status_aktif FROM iklan")
        hasil = cursor.fetchall()
        cursor.close()
        return hasil

    # =================================================================
    # CRUD UNTUK PEMBAYARAN (id_bayar, kd_iklan, tgl_bayar, total_bayar, metode)
    # =================================================================

    def simpanPembayaran(self, id_bayar, kd_iklan, tgl_bayar, total, metode):
        cursor = self.koneksi.cursor()
        sql = """INSERT INTO pembayaran
                 (id_bayar, kd_iklan, tgl_bayar, total_bayar, metode)
                 VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(sql, (id_bayar, kd_iklan, tgl_bayar, total, metode))
        self.koneksi.commit()
        cursor.close()

    def cariDataPembayaran(self):
        cursor = self.koneksi.cursor()
        cursor.execute("SELECT id_bayar, kd_iklan, tgl_bayar, total_bayar, metode FROM pembayaran")
        hasil = cursor.fetchall()
        cursor.close()
        return hasil

    # =================================================================
    # CRUD UNTUK PESAN INBOX (kd_pesan_inx, tgl_kirim_inx, nm_pengirim, email_pengirim, isi_pesan_inx, kd_member)
    # =================================================================

    def simpanPesanInbox(self, kd_pesan, tgl_kirim, nama_pengirim, email, isi_pesan, kd_member):
        cursor = self.koneksi.cursor()
        sql = """INSERT INTO pesan_inbox
                 (kd_pesan_inx, tgl_kirim_inx, nm_pengirim, email_pengirim, isi_pesan_inx, kd_member)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (kd_pesan, tgl_kirim, nama_pengirim, email, isi_pesan, kd_member))
        self.koneksi.commit()
        cursor.close()

    def cariDataPesanInbox(self):
        cursor = self.koneksi.cursor()
        cursor.execute("SELECT kd_pesan_inx, tgl_kirim_inx, nm_pengirim, email_pengirim, isi_pesan_inx, kd_member FROM pesan_inbox")
        hasil = cursor.fetchall()
        cursor.close()
        return hasil
