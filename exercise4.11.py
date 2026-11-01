pizzas = ['pepperoni', 'margherita', 'sosis', 'keju']

# Membuat salinan list dengan slice [:]
friend_pizzas = pizzas[:]

# Menambah pizza baru ke list asli
pizzas.append('jamur')

# Menambah pizza yang berbeda ke list teman
friend_pizzas.append('hawaiian')

# Membuktikan bahwa ada dua list yang terpisah
print("Pizza favoritku adalah:")
for pizza in pizzas:
    print(pizza)

print("\nPizza favorit temanku adalah:")
for pizza in friend_pizzas:
    print(pizza)