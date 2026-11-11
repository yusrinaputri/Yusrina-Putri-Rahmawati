from pathlib import Path
 
path = Path("belajar_python.txt")

# ===== 10-3: Kode lebih sederhana (tanpa variabel sementara) =====
print("\n=== 10-3 Kode lebih sederhana ===")
for baris in path.read_text(encoding="utf-8").splitlines():
    print(baris.replace("Python", "C"))