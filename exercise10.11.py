# 10-11 (program 1): simpan angka favorit
from pathlib import Path
import json
 
angka = input("Berapa angka favoritmu? ")
 
path = Path("angka_favorit.json")
isi = json.dumps(angka)
path.write_text(isi)
print("Angka favoritmu sudah disimpan!")

# 10-11 (program 2): baca angka favorit
from pathlib import Path
import json
 
path = Path("angka_favorit.json")
isi = path.read_text()
angka = json.loads(isi)
 
print(f"Aku tahu angka favoritmu! Yaitu {angka}.")