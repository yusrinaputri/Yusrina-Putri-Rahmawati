class Mobil:
    def __init__(self, merek, model, tahun):
        self.merek = merek
        self.model = model
        self.tahun = tahun
        self.pembacaan_odometer = 0
 
    def ambil_nama_lengkap(self):
        return f"{self.tahun} {self.merek} {self.model}".title()
 
    def baca_odometer(self):
        print(f"Mobil ini sudah menempuh {self.pembacaan_odometer} km.")
 
 
class Baterai:
    def __init__(self, ukuran_baterai=40):
        self.ukuran_baterai = ukuran_baterai
 
    def deskripsikan_baterai(self):
        print(f"Mobil ini punya baterai {self.ukuran_baterai}-kWh.")
 
    def ambil_jarak_tempuh(self):
        if self.ukuran_baterai == 40:
            jarak = 240
        elif self.ukuran_baterai == 65:
            jarak = 360
        else:
            jarak = 0
        print(f"Mobil ini bisa menempuh sekitar {jarak} km dengan "
              f"sekali pengisian penuh.")
 
    def upgrade_baterai(self):
        """Atur kapasitas ke 65 jika belum."""
        if self.ukuran_baterai != 65:
            self.ukuran_baterai = 65
            print("Baterai di-upgrade menjadi 65-kWh.")
        else:
            print("Baterai sudah berukuran 65-kWh.")
 
 
class MobilListrik(Mobil):
    def __init__(self, merek, model, tahun):
        super().__init__(merek, model, tahun)
        self.baterai = Baterai()
 
 
mobil_saya = MobilListrik("nissan", "leaf", 2024)
print(mobil_saya.ambil_nama_lengkap())
mobil_saya.baterai.ambil_jarak_tempuh()   # sebelum upgrade
mobil_saya.baterai.upgrade_baterai()
mobil_saya.baterai.ambil_jarak_tempuh()   # sesudah upgrade: jarak bertambah