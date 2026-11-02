guests = input("Berapa orang dalam rombongan makan malam Anda? ")
guests = int(guests)

if guests > 8:
    print("Maaf, Anda harus menunggu meja tersedia.")
else:
    print("Meja Anda sudah siap.")