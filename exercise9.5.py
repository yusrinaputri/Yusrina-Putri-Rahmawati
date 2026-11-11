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
 
    def sapa_pengguna(self):
        print(f"Halo, {self.nama_depan.title()} {self.nama_belakang.title()}!")
 
    def tambah_percobaan_login(self):
        """Tambah percobaan_login sebanyak 1."""
        self.percobaan_login += 1
 
    def reset_percobaan_login(self):
        """Reset percobaan_login ke 0."""
        self.percobaan_login = 0
 
 
pengguna = Pengguna("yusrina", "rahmawati", "ysrna", "yusrina@mail.com", "sukoharjo")
 
pengguna.tambah_percobaan_login()
pengguna.tambah_percobaan_login()
pengguna.tambah_percobaan_login()
print(f"percobaan_login: {pengguna.percobaan_login}")   # 3
 
pengguna.reset_percobaan_login()
print(f"percobaan_login: {pengguna.percobaan_login}")   # 0