prompt = "\nMasukkan topping pizza (ketik 'quit' untuk selesai): "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Baik, {topping} akan ditambahkan ke pizza Anda.")