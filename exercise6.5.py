rivers = {
    'nile': 'Mesir',
    'amazon': 'brazil',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print(f"Sungai {river.title()} mengalir melalui {country.title()}.")

print("\nSungai:")
for river in rivers.keys():
    print(river.title())

print("\nNegara:")
for country in rivers.values():
    print(country.title())