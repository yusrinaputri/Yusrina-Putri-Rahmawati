def city_country(city, country):
    """Mengembalikan string 'Kota, Negara'."""
    return f"{city.title()}, {country.title()}"


print(city_country('santiago', 'chile'))
print(city_country('tokyo', 'japan'))
print(city_country('paris', 'france'))