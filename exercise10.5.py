from pathlib import Path
 
print("Buku Tamu (ketik 'q' untuk selesai)")
daftar_nama = []
 
while True:
    nama = input("Siapa namamu? ")
    if nama == "q":
        break
    daftar_nama.append(nama)
    print(f"Terima kasih, {nama}!")
 
# setiap nama di baris baru
isi = "\n".join(daftar_nama)
Path("buku_tamu.txt").write_text(isi, encoding="utf-8")
print(f"{len(daftar_nama)} nama disimpan di buku_tamu.txt")