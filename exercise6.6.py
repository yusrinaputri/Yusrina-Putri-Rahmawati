favorite_languages = {
    'Yusrina': 'python',
    'Nissa': 'c',
    'Domi': 'rust',
    'Ael': 'python',
}
people_to_poll = ['Yusrina', 'Keira', 'Domi', 'Zahra', 'Ael']

for name in people_to_poll:
    if name in favorite_languages:
        print(f"Terima kasih {name.title()}, sudah mengisi poll!")
    else:
        print(f"{name.title()}, silakan ikut poll bahasa favorit kami!")