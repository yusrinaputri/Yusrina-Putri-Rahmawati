# Menyimpan nama beberapa jenis pizza favorit
pizzas = ['pepperoni', 'margherita', 'sosis', 'keju', 'jamur', 'daging asap', 'hawaiian']

# Mencetak nama setiap pizza
for pizza in pizzas:
    print(pizza)
    
# Setiap pizza dicetak dalam satu kalimat
for pizza in pizzas:
    print(f"Saya suka pizza {pizza}.")

# Baris ini berada di luar loop (tanpa indentasi), jadi hanya dicetak sekali
print("\nAku suka pizza pakai topping daging dan keju.")
print("Rasanya gurih, enak, dan bisa mengenyangkan.")
print("Saya benar-benar cinta pizza!")