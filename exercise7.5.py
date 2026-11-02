prompt = "\nBerapa umur Anda? (ketik 'quit' untuk selesai) "

while True:
    age = input(prompt)

    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print("Tiket gratis.")
    elif age <= 12:
        print("Harga tiket 200000.")
    else:
        print("Harga tiket 250000.")