from typing import Dict


# Задание 1.
# Реализуйте класс «Человек». Необходимо хранить в полях класса: ФИО,
# дату рождения, контактный телефон, город, страну, домашний адрес.
# Реализуйте конструктор по умолчанию и метод для вывода данных.
class Human:
    full_name: Dict[str, str]
    date_of_birth: Dict[str, str]
    phone: str
    city: str
    country: str
    address: Dict[str, str]

    def __init__(self, full_name: Dict[str, str], date_of_birth: Dict[str, str], phone: str, city: str, country: str,
                 address: Dict[str, str]):
        self.full_name = full_name.copy()
        self.date_of_birth = date_of_birth.copy()
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address.copy()

    def __str__(self):
        return f"ФИО: {' '.join(self.full_name.values())}\n" \
               f"Дата рождения: {'.'.join(self.date_of_birth.values())}\n" \
               f"Контактный телефон: {self.phone}\n" \
               f"Страна: {self.country}\n" \
               f"Город: {self.city}\n" \
               f"Адрес: Страна: {self.address['Страна']}, Область: {self.address['Область']}," \
               f" Город: {self.address['Город']}, Улица: {self.address['Улица']}, Дом: {self.address['Дом']}, " \
               f"Квартира: {self.address['Квартира']}."


def execute_application():
    full_name = {"Фамилия": "Иванов", "Имя": "Иван", "Отчество": "Иванович"}
    date_of_birth = {"Число": "01", "Месяц": "01", "Год": "2001"}
    address = {"Страна": "Россия", "Область": "Ярославская", "Город": "Ярославль", "Улица": "Пионерская", "Дом": "1",
               "Квартира": "1"}
    human_1 = Human(full_name, date_of_birth, "8(999)999-99-99", "Ярославль", "Россия", address)
    print(human_1)


if __name__ == '__main__':
    execute_application()
