from pathlib import Path
import json
 
 
def ambil_nama_tersimpan(path):
    """Ambil nama pengguna yang tersimpan, jika ada."""
    if path.exists():
        isi = path.read_text(encoding="utf-8")
        return json.loads(isi)
    return None
 
 
def ambil_nama_baru(path):
    """Minta nama pengguna baru dan simpan."""
    nama = input("Siapa namamu? ")
    path.write_text(json.dumps(nama), encoding="utf-8")
    return nama
 
 
def sapa_pengguna():
    """Sapa pengguna dengan nama, setelah diverifikasi."""
    path = Path("nama_pengguna.json")
    nama = ambil_nama_tersimpan(path)
 
    if nama:
        benar = input(f"Apakah kamu {nama}? (y/n) ")
        if benar.lower() == "y":
            print(f"Selamat datang kembali, {nama}!")
        else:
            nama = ambil_nama_baru(path)
            print(f"Kami akan mengingatmu saat kamu kembali, {nama}!")
    else:
        nama = ambil_nama_baru(path)
        print(f"Kami akan mengingatmu saat kamu kembali, {nama}!")
 
 
sapa_pengguna()