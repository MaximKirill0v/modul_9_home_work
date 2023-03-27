from typing import Dict
import re


# Задание 2.
# Реализуйте класс «Стадион». Необходимо хранить в полях класса:
# название стадиона, дату открытия, страну, город, вместимость. Реализуйте
# конструктор по умолчанию и метод для вывода данных. Реализуйте доступ к
# отдельным полям класса через методы класса (геттеры и сеттеры).
# Реализуйте в классе «Стадион» дополнительный метод класса и
# статический метод.
class Stadium:
    PATH_TO_FILE = "data_stadiums.txt"

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
               f"Вместительность: {self.__capacity:,}.\n"

    @staticmethod
    def create_dict_opening_date(date: str):
        if re.search(r'^[0-3]?[0-9].[0-3]?[0-9].(?:[0-9]{2})?[0-9]{2}$', date):
            date = date.split(".")
            return {"Число": date[0], "Месяц": date[1], "Год": date[2]}
        else:
            raise Exception(f"Дата не соответствует формату - 'DD.MM.YYYY'.")

    @classmethod
    def init_data_stadium_from_file(cls, index: int):
        """Создаёт объект класса Stadium"""
        with open(cls.PATH_TO_FILE, "r", encoding="utf-8") as file:
            data_stadiums = file.readlines()
            data_stadium = data_stadiums[index].strip().split(", ")
            opening_date = cls.create_dict_opening_date(data_stadium[1])
            return cls(data_stadium[0], opening_date, data_stadium[2], data_stadium[3], int(data_stadium[4]))

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
    try:
        opening_date = Stadium.create_dict_opening_date("31.07.1956")
        stadium_1 = Stadium("Лужники", opening_date, "Россия", "Москва", 76880)
        print(stadium_1)

        stadium_2 = Stadium.init_data_stadium_from_file(1)
        print(stadium_2)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    execute_application()
