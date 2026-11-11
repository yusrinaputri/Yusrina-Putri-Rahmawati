from random import sample

print("=== 9-14 Undian ===")
kumpulan = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e")
pemenang = sample(kumpulan, 4)  # 4 item berbeda secara acak
print(f"Tiket yang menang: {pemenang}")
print("Selamat! Tiket yang cocok dengan 4 angka/huruf ini memenangkan hadiah!")