tamu = ['Domi', 'Fillaena', 'Nissa']

print(f"Halo {tamu[0]}, saya mengundang Anda untuk makan malam.")
print(f"Halo {tamu[1]}, saya mengundang Anda untuk makan malam.")
print(f"Halo {tamu[2]}, saya mengundang Anda untuk makan malam.")

# Tamu yang tidak bisa hadir
print(f"\nMaaf, {tamu[1]} tidak bisa hadir.")

# Mengganti tamu yang tidak bisa hadir dengan orang baru
tamu[1] = 'Zahra'

# Mencetak undangan kedua
print(f"\nHalo {tamu[0]}, saya mengundang Anda untuk makan malam.")
print(f"Halo {tamu[1]}, saya mengundang Anda untuk makan malam.")
print(f"Halo {tamu[2]}, saya mengundang Anda untuk makan malam.")