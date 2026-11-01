# Menyimpan lokasi yang ingin dikunjungi (tidak berurutan secara alfabet)
lokasi = ['Nusa Penida', 'Labuan Bajo', 'Raja Ampat', 'Karimun Jawa', 'Wae Rebo']

# Mencetak list dalam urutan asli
print("Urutan asli:")
print(lokasi)

# sorted() urutan alfabet tanpa mengubah list asli
print("\nsorted() alfabet:")
print(sorted(lokasi))

# Menunjukkan list masih dalam urutan asli
print("\nList masih urutan asli:")
print(lokasi)

# sorted() urutan alfabet terbalik tanpa mengubah list asli
print("\nsorted() alfabet terbalik:")
print(sorted(lokasi, reverse=True))

# Menunjukkan list masih dalam urutan asli
print("\nList masih urutan asli:")
print(lokasi)

# reverse() mengubah urutan list
lokasi.reverse()
print("\nSetelah reverse() pertama:")
print(lokasi)

# reverse() lagi untuk mengembalikan ke urutan asli
lokasi.reverse()
print("\nSetelah reverse() kedua (kembali ke asli):")
print(lokasi)

# sort() mengurutkan list secara alfabet (mengubah list)
lokasi.sort()
print("\nSetelah sort() alfabet:")
print(lokasi)

# sort() urutan alfabet terbalik (mengubah list)
lokasi.sort(reverse=True)
print("\nSetelah sort() alfabet terbalik:")
print(lokasi)