glossary = {
    'string': 'Rangkaian karakter yang diapit tanda kutip.',
    'list': 'Kumpulan item berurutan yang dapat diubah.',
    'loop': 'Struktur untuk mengulang blok kode.',
    'dictionary': 'Kumpulan pasangan key-value.',
    'variable': 'Nama yang menyimpan sebuah nilai.',
    # lima istilah baru
    'tuple': 'List yang tidak dapat diubah (immutable).',
    'function': 'Blok kode bernama yang bisa dipanggil berulang kali.',
    'boolean': 'Tipe data yang bernilai True atau False.',
    'integer': 'Bilangan bulat tanpa desimal.',
    'comment': 'Catatan dalam kode yang diabaikan Python.',
}

for word, meaning in glossary.items():
    print(f"{word}:\n\t{meaning}\n")