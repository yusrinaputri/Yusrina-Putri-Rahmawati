def build_profile(first, last, **user_info):
    """Membuat dictionary berisi profil pengguna."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


my_profile = build_profile(
    'Yusrina', 'Putri',
    location='Surakarta',
    field='Algoritma Prokom',
    hobby='coding',
)
print(my_profile)