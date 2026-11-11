class Restoran:
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan
        self.jumlah_dilayani = 0  # nilai default
 
    def deskripsikan_restoran(self):
        print(f"Restoran {self.nama_restoran} menyajikan masakan "
              f"{self.jenis_masakan}.")
 
    def buka_restoran(self):
        print(f"{self.nama_restoran} sedang buka!")
 
    def atur_jumlah_dilayani(self, jumlah):
        """Atur jumlah pelanggan yang sudah dilayani."""
        self.jumlah_dilayani = jumlah
 
    def tambah_jumlah_dilayani(self, jumlah):
        """Tambah jumlah pelanggan yang sudah dilayani."""
        self.jumlah_dilayani += jumlah
 
 
restoran = Restoran("Warung Sedap", "nusantara")
 
print(f"Pelanggan dilayani: {restoran.jumlah_dilayani}")
 
# ubah nilai langsung lewat atribut
restoran.jumlah_dilayani = 20
print(f"Pelanggan dilayani: {restoran.jumlah_dilayani}")
 
# ubah lewat method atur_jumlah_dilayani()
restoran.atur_jumlah_dilayani(35)
print(f"Pelanggan dilayani: {restoran.jumlah_dilayani}")
 
# tambah lewat method tambah_jumlah_dilayani()
restoran.tambah_jumlah_dilayani(120)
print(f"Pelanggan dilayani: {restoran.jumlah_dilayani}")