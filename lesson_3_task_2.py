from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79990000001"),
    Smartphone("Samsung", "Galaxy S24", "+79990000002"),
    Smartphone("Xiaomi", "Mi 14", "+79990000003"),
    Smartphone("Google", "Pixel 9", "+79990000004"),
    Smartphone("Huawei", "P60 Pro", "+79990000005"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
