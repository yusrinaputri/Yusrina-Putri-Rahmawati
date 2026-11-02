responses = {}
polling_active = True

while polling_active:
    name = input("\nSiapa nama Anda? ")
    place = input("Jika bisa mengunjungi satu tempat di dunia, ke mana Anda akan pergi? ")

    responses[name] = place

    repeat = input("Apakah ada orang lain yang mau mengisi? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Hasil Poll ---")
for name, place in responses.items():
    print(f"{name.title()} ingin pergi ke {place.title()}.")