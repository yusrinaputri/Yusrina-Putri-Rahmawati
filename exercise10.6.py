print("Masukkan dua angka, nanti saya jumlahkan.")
 
angka_1 = input("Angka pertama: ")
angka_2 = input("Angka kedua: ")
 
try:
    hasil = int(angka_1) + int(angka_2)
except ValueError:
    print("Maaf, kamu harus memasukkan angka, bukan teks.")
else:
    print(f"Hasil penjumlahan: {hasil}")