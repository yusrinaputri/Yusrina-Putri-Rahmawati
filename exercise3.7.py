# Lanjutan dari program 3-6
tamu = ['Domi', 'Zahra', 'Nissa','Keira', 'Naila', 'Berlina']

# Memberi tahu bahwa hanya bisa mengundang dua orang
print("Maaf, meja yang baru tidak sampai tepat waktu. Aku cuma bisa mengundang dua orang.")

# Menghapus tamu satu per satu dengan pop() sampai tersisa dua nama
while len(tamu) > 2:
    dihapus = tamu.pop()
    print(f"Maaf {dihapus}, saya tidak bisa mengundang Anda makan malam.")

# Mengirim pesan kepada dua orang yang masih ada
print(f"\nHalo {tamu[0]}, Anda masih diundang makan malam.")
print(f"Halo {tamu[1]}, Anda masih diundang makan malam.")

# Menghapus dua nama terakhir dengan del sehingga list kosong
del tamu[0]
del tamu[0]

# Mencetak list untuk memastikan sudah kosong
print(f"\nIsi list sekarang: {tamu}")