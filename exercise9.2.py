class Restoran:
    """Model sederhana sebuah restoran."""
 
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan
 
    def deskripsikan_restoran(self):
        print(f"Restoran {self.nama_restoran} menyajikan masakan "
              f"{self.jenis_masakan}.")
 
    def buka_restoran(self):
        print(f"{self.nama_restoran} sedang buka!")
        
print("\n=== 9-2 Tiga Restoran ===")
restoran_1 = Restoran("Sate Pak Slamet", "sate")
restoran_2 = Restoran("Pizza Nonna", "italia")
restoran_3 = Restoran("Sushi Sakura", "jepang")
 
restoran_1.deskripsikan_restoran()
restoran_2.deskripsikan_restoran()
restoran_3.deskripsikan_restoran()