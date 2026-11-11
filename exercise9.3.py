class Pengguna:
    """Profil pengguna sederhana."""
 
    def __init__(self, nama_depan, nama_belakang, nama_pengguna, email, lokasi):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nama_pengguna = nama_pengguna
        self.email = email
        self.lokasi = lokasi
 
    def deskripsikan_pengguna(self):
        print(f"\nNama          : {self.nama_depan.title()} "
              f"{self.nama_belakang.title()}")
        print(f"Nama pengguna : {self.nama_pengguna}")
        print(f"Email         : {self.email}")
        print(f"Lokasi        : {self.lokasi.title()}")
 
    def sapa_pengguna(self):
        print(f"Halo, {self.nama_depan.title()} {self.nama_belakang.title()}! "
              f"Selamat datang kembali.")
 
 
pengguna_1 = Pengguna("yusrina", "rahmawati", "ysrna", "yusrina@mail.com", "sukoharjo")
pengguna_2 = Pengguna("gannisa", "sari", "nissa", "nissa@mail.com", "wonogiri")
pengguna_3 = Pengguna("dominique", "winoto", "domi", "domi@mail.com", "salatiga")
 
for pengguna in (pengguna_1, pengguna_2, pengguna_3):
    pengguna.deskripsikan_pengguna()
    pengguna.sapa_pengguna()