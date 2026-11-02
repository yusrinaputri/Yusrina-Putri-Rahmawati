def make_car(manufacturer, model, **car_info):
    """Membuat dictionary berisi informasi mobil."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


car = make_car('mazda', 'hatchback', color='silver', tow_package=True)
print(car)