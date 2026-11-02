def describe_city(city, country='indonesia'):
    """Menampilkan kalimat tentang sebuah kota."""
    print(f"{city.title()} is in {country.title()}.")


describe_city('surakarta')
describe_city('bandung')
describe_city('reykjavik', 'iceland')