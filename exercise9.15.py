from random import sample

kumpulan = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e")
tiket_saya = [3, 7, "b", "e"]

percobaan = 0
while True:
    percobaan += 1
    hasil = sample(kumpulan, 4)
    if set(hasil) == set(tiket_saya):  # urutan tidak penting
        break

print(f"Tiket {tiket_saya} menang setelah {percobaan} kali undian.")