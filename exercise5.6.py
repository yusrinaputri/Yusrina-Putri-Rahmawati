umur = int(input("Masukkan umur: "))

if umur < 2:
    print("Orang ini adalah seorang bayi.")
elif umur < 4:
    print("Orang ini adalah seorang balita.")
elif umur < 13:
    print("Orang ini adalah seorang anak-anak.")
elif umur < 20:
    print("Orang ini adalah seorang remaja.")
elif umur < 65:
    print("Orang ini adalah seorang dewasa.")
else:
    print("Orang ini adalah seorang lansia.")