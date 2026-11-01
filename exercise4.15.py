# Sebelum pakai aturan PEP8 (indentasi 2 spasi, banyak baris kosong)
pizzas = ['pepperoni', 'margherita', 'sosis', 'keju']



for pizza in pizzas:
  print(f"Saya suka pizza {pizza}.")




print("\nSaya benar-benar cinta pizza!")

# Sesudah pakai aturan PEP8
pizzas = ['pepperoni', 'margherita', 'sosis', 'keju']

for pizza in pizzas:
    print(f"Saya suka pizza {pizza}.")

print("\nSaya benar-benar cinta pizza!")

# Sebelum pakai aturan PEP8 (indentasi tidak konsisten, baris terlalu panjang)
pangkat_tiga = []
for nilai in range(1, 11):
      pangkat_tiga.append(nilai ** 3)
print("Daftar pangkat tiga dari satu sampai sepuluh yang dihitung menggunakan loop for dan operator pangkat adalah:", pangkat_tiga)

# Sesudah pakai aturan PEP8
pangkat_tiga = []
for nilai in range(1, 11):
    pangkat_tiga.append(nilai ** 3)

print("Daftar pangkat tiga dari 1 sampai 10:")
print(pangkat_tiga)

# Sebelum pakai aturan PEP8 (baris terlalu panjang, tanpa jarak antar bagian)
pizzas = ['pepperoni', 'margherita', 'sosis', 'keju']
friend_pizzas = pizzas[:]
pizzas.append('jamur')
friend_pizzas.append('hawaiian')
print("Pizza favoritku adalah:")
for pizza in pizzas:
  print(pizza)
print("Pizza favorit temanku adalah:")
for pizza in friend_pizzas:
  print(pizza)
  
# Sesudah pakai aturan PEP8
pizzas = ['pepperoni', 'margherita', 'sosis', 'keju']
friend_pizzas = pizzas[:]

pizzas.append('jamur')
friend_pizzas.append('hawaiian')

print("Pizza favoritku adalah:")
for pizza in pizzas:
    print(pizza)

print("\nPizza favorit temanku adalah:")
for pizza in friend_pizzas:
    print(pizza)