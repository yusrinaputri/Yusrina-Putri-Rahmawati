def make_album(artist, title, songs=None):
    """Membuat dictionary berisi informasi album."""
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album


print(make_album('Rex Orange County', 'Pony'))
print(make_album('Frank Ocean', 'Blonde'))
print(make_album('Daniel Caesar', 'Freudian', songs=10))