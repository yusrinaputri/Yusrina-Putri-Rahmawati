def make_sandwich(*items):
    """Menampilkan ringkasan isi sandwich yang dipesan."""
    print("\nSandwich Anda berisi:")
    for item in items:
        print(f"- {item}")


make_sandwich('keju')
make_sandwich('telur', 'tomat')
make_sandwich('ayam', 'selada', 'mayones', 'keju')