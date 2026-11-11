from pathlib import Path
 
nama_file = ["kucing.txt", "anjing.txt"]
 
for nama in nama_file:
    path = Path(nama)
    try:
        isi = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        print(f"\nIsi {nama}:")
        print(isi)