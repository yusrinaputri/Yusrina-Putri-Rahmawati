from pathlib import Path
 
path = Path("belajar_python.txt")

# ===== 10-2: Belajar C (replace) =====
print("\n=== 10-2 Belajar C ===")

isi = path.read_text(encoding="utf-8")
baris_baris = isi.splitlines()

for baris in baris_baris:
    print(baris.replace("Python", "C"))