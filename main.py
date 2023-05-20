from typing import Dict
import re
import json
import pickle


# Задание 2.
# Реализуйте класс «Стадион». Необходимо хранить в полях класса:
# название стадиона, дату открытия, страну, город, вместимость. Реализуйте
# конструктор по умолчанию и метод для вывода данных. Реализуйте доступ к
# отдельным полям класса через методы класса (геттеры и сеттеры).
# Реализуйте в классе «Стадион» дополнительный метод класса и
# статический метод.

# К уже реализованному классу «Стадион» добавьте
# возможность упаковки и распаковки данных с использованием json и pickle.
class Stadium:

    def __init__(self, stadium_name: str = None, opening_date: Dict[str, str] = None, country: str = None,
                 city: str = None, capacity: int = 0):
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
    def init_data_stadium_from_file(cls, path: str, index: int):
        """Создаёт объект класса Stadium"""
        with open(path, "r", encoding="utf-8") as file:
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


class PickleStadiumAdapter:
    @staticmethod
    def to_pickle_stadium(stadium: Stadium):
        if isinstance(stadium, Stadium):
            return pickle.dumps({
                "_Stadium__stadium_name": stadium.stadium_name,
                "_Stadium__opening_date": stadium.opening_date,
                "_Stadium__country": stadium.country,
                "_Stadium__city": stadium.city,
                "_Stadium__capacity": stadium.capacity,
            })
        raise TypeError(f"Переданный аргумент не является объектом класса {car.__class__.__name__}")

    @staticmethod
    def from_pickle_stadium(data):
        obj = pickle.loads(data)

        try:
            return Stadium(obj["_Stadium__stadium_name"], obj["_Stadium__opening_date"], obj["_Stadium__country"],
                           obj["_Stadium__city"], obj["_Stadium__capacity"])
        except AttributeError as e:
            print(e)


class StadiumJSONConverter:
    @staticmethod
    def to_dict(stadium: Stadium):
        if isinstance(stadium, Stadium):
            result = stadium.__dict__
            result["className"] = stadium.__class__.__name__
            return result
        raise TypeError(f"Переданный аргумент не является объектом класса {stadium.__class__.__name__}")


class JsonStadiumAdapter:
    @staticmethod
    def to_json_stadium(d: dict):
        return json.dumps(d)

    @staticmethod
    def from_json_stadium(data):
        obj = json.loads(data)

        try:
            return Stadium(obj["_Stadium__stadium_name"], obj["_Stadium__opening_date"], obj["_Stadium__country"],
                           obj["_Stadium__city"], obj["_Stadium__capacity"])
        except AttributeError as e:
            print(e)


class TestEncoder(json.JSONEncoder):
    def default(self, other):
        return {"_Stadium__stadium_name": other.stadium_name, "_Stadium__opening_date": other.opening_date,
                "_Stadium__country": other.country, "_Stadium__city": other.city, "_Stadium__capacity": other.capacity,
                "className": other.__class__.__name__}


def execute_application():
    path_to_file = "data_stadiums.txt"
    try:
        opening_date = Stadium.create_dict_opening_date("31.07.1956")
        stadium_1 = Stadium("Лужники", opening_date, "Россия", "Москва", 76880)
        print(stadium_1)

        stadium_2 = Stadium.init_data_stadium_from_file(path_to_file, 1)
        print(stadium_2)

        to_pickle_stadium = PickleStadiumAdapter.to_pickle_stadium(stadium_1)
        print(f"Сериализация объекта класса Stadium с помощью модуля pickle:\n{to_pickle_stadium}")
        from_pickle_stadium = PickleStadiumAdapter.from_pickle_stadium(to_pickle_stadium)
        print(f"Десериализация объекта класса Stadium с помощью модуля pickle:\n{from_pickle_stadium}")

        to_json_stadium = JsonStadiumAdapter.to_json_stadium(StadiumJSONConverter.to_dict(stadium_2))
        print(f"\nСериализация объекта класса Stadium с помощью модуля json:\n{to_json_stadium}")
        from_json_stadium = JsonStadiumAdapter.from_json_stadium(to_json_stadium)
        print(f"Десериализация объекта класса Stadium с помощью модуля Json:\n{from_json_stadium}")

    except Exception as e:
        print(e)


if __name__ == '__main__':
    execute_application()
