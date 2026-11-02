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

for city, info in cities.items():
    print(f"\nKota: {city.title()}")
    print(f"Negara: {info['country'].title()}")
    print(f"Populasi: {info['population']}")
    print(f"Fakta: {info['fact']}") 