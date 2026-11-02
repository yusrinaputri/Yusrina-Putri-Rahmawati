def make_shirt(size, text):
    """Menampilkan ringkasan ukuran dan tulisan pada kaos."""
    print(f"Ukuran kaos {size} dengan tulisan '{text}'.")

# Positional arguments
make_shirt('large', 'I love Python')

# Keyword arguments
make_shirt(text='Hello Python', size='medium')