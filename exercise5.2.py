# 1. Kesamaan dan ketidaksamaan string
nama = 'Yusrina'
print(nama == 'Yusrina')     # True
print(nama == 'Nissa')     # False
print(nama != 'Fillaena')     # True
print(nama != 'Yusrina')     # False

# 2. Metode lower()
kota = 'Solo'
print(kota.lower() == 'solo')      # True
print(kota.lower() == 'Solo')      # False

# 3. Tes numerik
umur = 18
print(umur == 18)    # True
print(umur == 25)    # False
print(umur != 25)    # True
print(umur != 18)    # False
print(umur > 15)     # True
print(umur > 30)     # False
print(umur < 30)     # True
print(umur < 10)     # False
print(umur >= 18)    # True
print(umur >= 19)    # False
print(umur <= 18)    # True
print(umur <= 17)    # False

# 4. Kata kunci and dan or
print(umur > 10 and umur < 30)    # True
print(umur > 10 and umur < 15)    # False
print(umur < 10 or umur > 15)     # True
print(umur < 10 or umur > 50)     # False

# 5. Item ada di dalam list
buah = ['apel', 'jeruk', 'mangga']
print('apel' in buah)     # True
print('pisang' in buah)   # False

# 6. Item tidak ada di dalam list
print('pisang' not in buah)   # True
print('apel' not in buah)     # False