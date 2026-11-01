current_users = ['yusrina', 'domi', 'ael', 'nissa', 'admin']
new_users = ['zahra', 'Domi', 'keira', 'YUSRINA', 'naila']

# Salinan huruf kecil agar perbandingan tidak peduli huruf besar/kecil
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' sudah dipakai. Masukkan username lain.")
    else:
        print(f"Username '{new_user}' tersedia.")