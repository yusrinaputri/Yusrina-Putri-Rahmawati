gunung = ['Merapi', 'Merbabu', 'Lawu']
print(f"List awal: {gunung}")

# Mengakses elemen dengan indeks
print(f"Gunung pertama: {gunung[0]}")
print(f"Gunung terakhir: {gunung[-1]}")

# Mengubah elemen
gunung[1] = 'Sindoro'
print(f"Setelah mengubah elemen: {gunung}")

# append() menambah di akhir
gunung.append('Semeru')
print(f"Setelah append(): {gunung}")

# insert() menyisipkan di posisi tertentu
gunung.insert(0, 'Rinjani')
print(f"Setelah insert(): {gunung}")

# len() menghitung jumlah elemen
print(f"Jumlah gunung: {len(gunung)}")

# sorted() mengurutkan sementara
print(f"Hasil sorted(): {sorted(gunung)}")

# sort() mengurutkan permanen
gunung.sort()
print(f"Setelah sort(): {gunung}")

# reverse() membalik urutan
gunung.reverse()
print(f"Setelah reverse(): {gunung}")

# pop() menghapus elemen terakhir dan mengembalikannya
dihapus = gunung.pop()
print(f"Dihapus dengan pop(): {dihapus}")
print(f"Setelah pop(): {gunung}")

# del menghapus elemen berdasarkan indeks
del gunung[0]
print(f"Setelah del: {gunung}")

# remove() menghapus elemen berdasarkan nilai
gunung.remove('Rinjani')
print(f"Setelah remove(): {gunung}")