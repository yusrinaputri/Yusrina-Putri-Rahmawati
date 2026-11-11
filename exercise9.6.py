class Restoran:
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan
        self.jumlah_dilayani = 0
 
    def deskripsikan_restoran(self):
        print(f"Restoran {self.nama_restoran} menyajikan masakan "
              f"{self.jenis_masakan}.")
 
    def buka_restoran(self):
        print(f"{self.nama_restoran} sedang buka!")
 
 
class KedaiEsKrim(Restoran):
    """Kedai es krim adalah jenis khusus dari restoran."""
 
    def __init__(self, nama_restoran, jenis_masakan="es krim"):
        super().__init__(nama_restoran, jenis_masakan)
        self.rasa = ["vanila", "cokelat", "stroberi", "matcha"]
 
    def tampilkan_rasa(self):
        print(f"Rasa es krim di {self.nama_restoran}:")
        for rasa in self.rasa:
            print(f"- {rasa.title()}")
 
 
kedai = KedaiEsKrim("Es Krim Ceria")
kedai.deskripsikan_restoran()
kedai.tampilkan_rasa()