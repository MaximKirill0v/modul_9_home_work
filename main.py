from typing import Dict


# Задание 1.
# Реализуйте класс «Человек». Необходимо хранить в полях класса: ФИО,
# дату рождения, контактный телефон, город, страну, домашний адрес.
# Реализуйте конструктор по умолчанию и метод для вывода данных.
# Реализуйте доступ к отдельным полям класса через методы класса (геттеры
# и сеттеры).
class Human:
    def __init__(self, full_name: Dict[str, str], date_of_birth: Dict[str, str], phone: str, city: str, country: str,
                 address: Dict[str, str]):
        self.__full_name = full_name.copy()
        self.__date_of_birth = date_of_birth.copy()
        self.__phone = phone
        self.__city = city
        self.__country = country
        self.__address = address.copy()

    def __str__(self):
        return f"ФИО: {' '.join(self.full_name.values())}\n" \
               f"Дата рождения: {'.'.join(self.date_of_birth.values())}\n" \
               f"Контактный телефон: {self.__phone}\n" \
               f"Страна: {self.__country}\n" \
               f"Город: {self.__city}\n" \
               f"Адрес: Страна: {self.address['Страна']}, Область: {self.address['Область']}," \
               f" Город: {self.address['Город']}, Улица: {self.address['Улица']}, Дом: {self.address['Дом']}, " \
               f"Квартира: {self.address['Квартира']}."

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name: dict[str, str]):
        self.__full_name = full_name

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: dict[str, str]):
        self.__date_of_birth = date_of_birth

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: dict[str, str]):
        self.__address = address


def execute_application():
    full_name = {"Фамилия": "Иванов", "Имя": "Иван", "Отчество": "Иванович"}
    date_of_birth = {"Число": "01", "Месяц": "01", "Год": "2001"}
    address = {"Страна": "Россия", "Область": "Ярославская", "Город": "Ярославль", "Улица": "Пионерская", "Дом": "1",
               "Квартира": "1"}
    human_1 = Human(full_name, date_of_birth, "8(999)999-99-99", "Ярославль", "Россия", address)
    print(human_1)
    print("\nОбращение к отдельным полям при помощи методов класса 'get': ")
    print(f"Телефон экземпляра класса Human - {human_1.phone}")
    print(f"Город экземпляра класса Human - {human_1.city}")
    print(f"Страна экземпляра класса Human - {human_1.country}")
    print(f"ФИО экземпляра класса Human - {human_1.full_name}")
    print(f"Дата рождения экземпляра класса Human - {human_1.date_of_birth}")
    print(f"Адрес экземпляра класса Human - {human_1.address}")


if __name__ == '__main__':
    execute_application()
