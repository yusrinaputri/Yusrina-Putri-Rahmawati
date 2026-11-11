from pathlib import Path
 
path = Path("belajar_python.txt")
 
# ===== 10-1: Belajar Python =====
print("=== 10-1 (dibaca utuh) ===")
isi = path.read_text(encoding="utf-8")
print(isi)
 
print("=== 10-1 (disimpan ke list, lalu di-loop) ===")
baris_baris = isi.splitlines()
for baris in baris_baris:
    print(baris)