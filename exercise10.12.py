# 10-12: Angka Favorit yang Diingat (gabungan dua program 10-11)
from pathlib import Path
import json
 
path = Path("angka_favorit.json")
 
if path.exists():
    angka = json.loads(path.read_text())
    print(f"Aku tahu angka favoritmu! Yaitu {angka}.")
else:
    angka = input("Berapa angka favoritmu? ")
    path.write_text(json.dumps(angka))
    print("Angka favoritmu sudah disimpan! Jalankan lagi programnya.")