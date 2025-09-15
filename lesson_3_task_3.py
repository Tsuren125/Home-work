from address import Address
from mailing import Mailing

to_addr = Address("123456", "Москва", "Ленина", "10", "5")
from_addr = Address("654321", "Санкт-Петербург", "Невский", "20", "15")

mail = Mailing(to_addr, from_addr, 350.50, "RU123456789")

print(
    f"Отправление {mail.track} "
    f"из {mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, "
    f"{mail.from_address.house} - {mail.from_address.apartment} "
    f"в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, "
    f"{mail.to_address.house} - {mail.to_address.apartment}. "
    f"Стоимость {mail.cost} рублей."
)
