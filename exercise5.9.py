usernames = ['Admin', 'Yusrina', 'Nissa', 'Domi', 'Ael']

if usernames:
    for username in usernames:
        if username == 'Admin':
            print("Halo Admin, apakah Anda ingin melihat laporan status?")
        else:
            print(f"Halo {username}, terima kasih sudah login lagi.")
else:
    print("Kita perlu mencari beberapa pengguna!")