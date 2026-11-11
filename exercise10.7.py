print("Kalkulator Penjumlahan (ketik 'q' untuk keluar)")
 
while True:
    angka_1 = input("\nAngka pertama: ")
    if angka_1 == "q":
        break
    angka_2 = input("Angka kedua: ")
    if angka_2 == "q":
        break
 
    try:
        hasil = int(angka_1) + int(angka_2)
    except ValueError:
        print("Maaf, kamu harus memasukkan angka, bukan teks.")
    else:
        print(f"Hasil penjumlahan: {hasil}")