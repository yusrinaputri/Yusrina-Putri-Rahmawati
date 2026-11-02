person_1 = {'first_name': 'Dominique', 'last_name': 'Winoto', 'age': 19, 'city': 'Salatiga'}
person_2 = {'first_name': 'Fillaena', 'last_name': 'Bipta', 'age': 19, 'city': 'Purwokerto'}
person_3 = {'first_name': 'Gannisa', 'last_name': 'Sari', 'age': 19, 'city': 'Wonogiri'}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name}, {person['age']} tahun, tinggal di {person['city']}.")