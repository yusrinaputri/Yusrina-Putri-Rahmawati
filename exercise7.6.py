# Memakai while
prompt = "\nMasukkan topping pizza (ketik 'quit' untuk selesai): "
topping = ""

while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(f"Baik, {topping} akan ditambahkan ke pizza Anda.")
        
# memakai variabel aktif
prompt = "\nMasukkan topping pizza (ketik 'quit' untuk selesai): "
active = True

while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f"Baik, {topping} akan ditambahkan ke pizza Anda.")
        
# memakai break
prompt = "\nMasukkan topping pizza (ketik 'quit' untuk selesai): "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Baik, {topping} akan ditambahkan ke pizza Anda.")