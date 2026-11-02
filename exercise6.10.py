favorite_numbers = {
    'Ael': [7, 14],
    'Keira': [12, 3, 8],
    'Zahra': [3],
    'Putri': [21, 5],
    'Desy': [9, 1, 100],
}

for name, numbers in favorite_numbers.items():
    print(f"\nAngka favorit {name.title()}:")
    for number in numbers:
        print(f"- {number}")