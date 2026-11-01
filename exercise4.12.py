my_foods = ['pizza', 'burger', 'spaghetti']
friend_foods = my_foods[:]

my_foods.append('ice cream')
friend_foods.append('kebab')

print("Makanan favoritku adalah:")
for makanan in my_foods:
    print(makanan)

print("\nMakanan favorit temanku adalah:")
for makanan in friend_foods:
    print(makanan)