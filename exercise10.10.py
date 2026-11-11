from pathlib import Path
 
nama_file = ["contoh_teks_1.txt", "contoh_teks_2.txt"]
 
for nama in nama_file:
    path = Path(nama)
    try:
        isi = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Maaf, file {nama} tidak ditemukan.")
        continue
 
    isi = isi.lower()
    jumlah_the = isi.count("the")
    jumlah_the_spasi = isi.count("the ")  # lebih akurat (tanpa 'then', 'there')
 
    print(f"\n{nama}")
    print(f"  'the'  muncul {jumlah_the} kali")
    print(f"  'the ' muncul {jumlah_the_spasi} kali")