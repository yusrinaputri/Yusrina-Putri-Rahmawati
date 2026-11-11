class Pengguna:
    def __init__(self, nama_depan, nama_belakang, nama_pengguna, email, lokasi):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nama_pengguna = nama_pengguna
        self.email = email
        self.lokasi = lokasi
        self.percobaan_login = 0
 
    def deskripsikan_pengguna(self):
        print(f"\nNama          : {self.nama_depan.title()} "
              f"{self.nama_belakang.title()}")
        print(f"Nama pengguna : {self.nama_pengguna}")
        print(f"Email         : {self.email}")
        print(f"Lokasi        : {self.lokasi.title()}")
 
 
class Admin(Pengguna):
    def __init__(self, nama_depan, nama_belakang, nama_pengguna, email, lokasi):
        super().__init__(nama_depan, nama_belakang, nama_pengguna, email, lokasi)
        self.hak_akses = ["dapat menambah postingan",
                          "dapat menghapus postingan",
                          "dapat memblokir pengguna"]
 
    def tampilkan_hak_akses(self):
        print("Hak akses administrator:")
        for hak in self.hak_akses:
            print(f"- {hak}")
 
print("=== 9-7 Admin ===")
admin = Admin("yusrina", "rahmawati", "ysrna", "yusrina@mail.com", "sukoharjo")
admin.deskripsikan_pengguna()
admin.tampilkan_hak_akses()