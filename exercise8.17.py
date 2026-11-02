# Program 1 (8-6. City Names)
def city_country(city, country):
    """Mengembalikan string dengan format 'Kota, Negara'."""
    return f"{city.title()}, {country.title()}"


print(city_country('santiago', 'chile'))
print(city_country('tokyo', 'japan'))
print(city_country('paris', 'france'))

# Program 2 (8-7. Album)
def make_album(artist, title, songs=None):
    """Membuat dictionary berisi informasi album."""
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album


print(make_album('Rex Orange County', 'Pony'))
print(make_album('Frank Ocean', 'Blonde'))
print(make_album('Daniel Caesar', 'Freudian', songs=10))

# Program 3 (8-14. Cars)
def make_car(manufacturer, model, **car_info):
    """Membuat dictionary berisi informasi mobil."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


car = make_car('mazda', 'hatchback', color='silver', tow_package=True)
print(car)
