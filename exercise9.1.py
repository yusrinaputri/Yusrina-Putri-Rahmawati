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
        
print("=== 9-1 Restoran ===")
restoran = Restoran("Warung Sedap", "nusantara")
print(restoran.nama_restoran)
print(restoran.jenis_masakan)
restoran.deskripsikan_restoran()
restoran.buka_restoran()