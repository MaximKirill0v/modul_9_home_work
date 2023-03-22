from typing import Dict


# Задание 2.
# Реализуйте класс «Стадион». Необходимо хранить в полях класса:
# название стадиона, дату открытия, страну, город, вместимость. Реализуйте
# конструктор по умолчанию и метод для вывода данных. Реализуйте доступ к
# отдельным полям класса через методы класса (геттеры и сеттеры).
class Stadium:
    def __init__(self, stadium_name: str, opening_date: Dict[str, str], country: str, city: str, capacity: int = 0):
        self.__stadium_name = stadium_name
        self.__opening_date = opening_date.copy()
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def __str__(self):
        return f"Название стадиона: '{self.__stadium_name}'.\n" \
               f"Дата открытия: {'.'.join(self.__opening_date.values())}г.\n" \
               f"Страна: {self.__country}.\n" \
               f"Город: {self.__city}.\n" \
               f"Вместительность: {self.__capacity:,}."

    @property
    def stadium_name(self):
        return self.__stadium_name

    @stadium_name.setter
    def stadium_name(self, stadium_name):
        self.__stadium_name = stadium_name

    @property
    def opening_date(self):
        return self.__opening_date

    @opening_date.setter
    def opening_date(self, opening_date):
        self.__opening_date = opening_date

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country):
        self.__country = country

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity


def execute_application():
    opening_date = {"Число": "31", "Месяц": "07", "Год": "1956"}
    stadium_1 = Stadium("Лужники", opening_date, "Россия", "Москва", 76880)
    print(stadium_1)


if __name__ == '__main__':
    execute_application()
