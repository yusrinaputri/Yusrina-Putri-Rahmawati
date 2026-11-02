def make_album(artist, title, songs=None):
    """Membuat dictionary berisi informasi album."""
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album


while True:
    print("\n(ketik 'q' kapan saja untuk berhenti)")

    artist = input("Nama artis: ")
    if artist == 'q':
        break

    title = input("Judul album: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)