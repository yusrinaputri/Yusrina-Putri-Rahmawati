cities = {
    'jakarta': {
        'country': 'indonesia',
        'population': 10500000,
        'fact': 'Ibu kota Indonesia saat ini.',
    },
    'tokyo': {
        'country': 'japan',
        'population': 14000000,
        'fact': 'Salah satu kota terbesar di dunia.',
    },
    'paris': {
        'country': 'france',
        'population': 2100000,
        'fact': 'Rumah bagi Menara Eiffel.',
    },
}

# Pengembangan 6-12: tambah key baru 'landmark' ke tiap kota
cities['jakarta']['landmark'] = 'Monas'
cities['tokyo']['landmark'] = 'Tokyo Tower'
cities['paris']['landmark'] = 'Menara Eiffel'

for city, info in cities.items():
    print(f"\n{city.title()} ({info['country'].title()})")
    print("-" * 30)
    print(f"Populasi : {info['population']}")
    print(f"Fakta    : {info['fact']}")
    print(f"Landmark : {info['landmark']}")