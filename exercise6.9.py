favorite_places = {
    'Aira': ['Pantai Parangtritis', 'Candi Borobudur'],
    'Naila': ['Bali', 'Bromo', 'Raja Ampat'],
    'Berlina': ['Danau Toba'],
}

for name, places in favorite_places.items():
    print(f"\nTempat favorit {name.title()}:")
    for place in places:
        print(f"- {place}")