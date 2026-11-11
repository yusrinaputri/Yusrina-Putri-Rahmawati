from pathlib import Path
 
nama = input("Siapa namamu? ")
 
path = Path("tamu.txt")
path.write_text(nama, encoding="utf-8")
print(f"Halo, {nama}! Namamu sudah disimpan di {path}.")