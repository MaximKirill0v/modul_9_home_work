# Задание 1.
# Реализуйте класс «Человек». Необходимо хранить в полях класса: ФИО,
# дату рождения, контактный телефон, город, страну, домашний адрес.
# Реализуйте конструктор по умолчанию и метод для вывода данных.
class Human:
    full_name: dict[str, str]
    date_of_birth: dict[str, str]
    phone: str
    city: str
    country: str
    address: dict[str, str]

    def __init__(self, full_name: dict[str, str], date_of_birth: dict[str, str], phone: str, city: str, country: str,
                 address: dict[str, str]):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address

    def __str__(self):
        full_name = ", ".join(["-".join([key, value]) for key, value in self.full_name.items()])
        date_of_birth = ".".join([value for value in self.date_of_birth.values()])
        address = ", ".join(["-".join([key, value]) for key, value in self.address.items()])
        return f"ФИО: {full_name}\n" \
               f"Дата рождения: {date_of_birth}\n" \
               f"Контактный телефон: {self.phone}\n" \
               f"Страна: {self.country}\n" \
               f"Город: {self.city}\n" \
               f"Адрес: {address}"


def execute_application():
    full_name = {"Фамилия": "Иванов", "Имя": "Иван", "Отчество": "Иванович"}
    date_of_birth = {"Число": "01", "Месяц": "01", "Год": "2001"}
    address = {"Страна": "Россия", "Область": "Ярославская", "Город": "Ярославль", "Улица": "Пионерская", "Дом": "1",
               "Квартира": "1"}
    human_1 = Human(full_name, date_of_birth, "8(999)999-99-99", "Ярославль", "Россия", address)
    print(human_1)


if __name__ == '__main__':
    execute_application()
