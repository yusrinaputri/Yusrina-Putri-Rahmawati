from pathlib import Path
import json
 
 
def ambil_data_tersimpan(path):
    """Kembalikan dictionary pengguna jika ada, jika tidak None."""
    if path.exists():
        isi = path.read_text(encoding="utf-8")
        return json.loads(isi)
    return None
 
 
def ambil_data_baru(path):
    """Tanyakan data pengguna, simpan sebagai dictionary ke file JSON."""
    data = {
        "nama": input("Siapa namamu? "),
        "kota": input("Dari kota mana kamu berasal? "),
        "hobi": input("Apa hobimu? "),
    }
    path.write_text(json.dumps(data), encoding="utf-8")
    return data
 
 
def sapa_pengguna():
    path = Path("data_pengguna.json")
    data = ambil_data_tersimpan(path)
 
    if data:
        print(f"Selamat datang kembali, {data['nama']}!")
        print("Ini yang aku ingat tentangmu:")
        print(f"- Nama : {data['nama']}")
        print(f"- Kota : {data['kota']}")
        print(f"- Hobi : {data['hobi']}")
    else:
        data = ambil_data_baru(path)
        print(f"Aku akan mengingatmu, {data['nama']}!")
 
 
sapa_pengguna()