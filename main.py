import pickle
import json


# Задание 1.
# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
# название модели, год выпуска, производителя, объем двигателя, цвет машины,
# цену. Реализуйте конструктор по умолчанию и метод для вывода данных.
# Реализуйте доступ к отдельным полям класса через методы класса (геттеры
# и сеттеры).
# Реализуйте в классе «Автомобиль» дополнительный метод класса и
# статический метод.


# К уже реализованному классу «Автомобиль» добавьте
# возможность упаковки и распаковки данных с использованием json и pickle.

class Car:
    def __init__(self, name_model: str = None, year_of_manufacture: int = None, manufacturer: str = None,
                 engine_capacity: float = None, color: str = None, price: float = None):
        self.__name_model = name_model
        self.__year_of_manufacture = year_of_manufacture
        self.__manufacturer = manufacturer
        self.__engine_capacity = engine_capacity
        self.__color = color
        self.__price = price

    def __str__(self):
        return f"Модель автомобиля - '{self.__name_model}'.\n" \
               f"Год выпуска - {self.__year_of_manufacture}г.\n" \
               f"Производитель - {self.__manufacturer}.\n" \
               f"Объём двигателя - {self.__engine_capacity}л.\n" \
               f"Цвет кузова - {self.__color}.\n" \
               f"Цена - {self.__price:,.2f}р.\n"

    @classmethod
    def init_car(cls, data_car: tuple):
        """Создаёт объект класса Car"""
        if Car.check_data_car(data_car):
            return cls(data_car[0], data_car[1], data_car[2], data_car[3], data_car[4], data_car[5])

    @staticmethod
    def check_data_car(data_car: tuple):
        """Проверяет данные автомобиля на корректность"""
        if len(data_car) == 6:
            if isinstance(data_car[1], int | float) and isinstance(data_car[3], int | float) and \
                    isinstance(data_car[5], int | float):
                if data_car[1] > 0 and data_car[3] > 0 and data_car[5] > 0:
                    return True
                else:
                    print(f"Не корректные данные. Переданные данные - {' '.join(map(str, data_car))}")
                    return False
            else:
                print(f"Не корректные данные, ожидалось число. Переданные данные - {' '.join(map(str, data_car))}")
                return False
        else:
            print(f"В метод переданы не все данные об автомобиле. Переданные данные - {' '.join(map(str, data_car))}")
            return False

    @property
    def name_model(self):
        return self.__name_model

    @name_model.setter
    def name_model(self, name_model):
        self.__name_model = name_model

    @property
    def year_of_manufacture(self):
        return self.__year_of_manufacture

    @year_of_manufacture.setter
    def year_of_manufacture(self, year_of_manufacture):
        self.__year_of_manufacture = year_of_manufacture

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    @property
    def engine_capacity(self):
        return self.__engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, engine_capacity):
        self.__engine_capacity = engine_capacity

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


class PickleCarAdapter:
    @staticmethod
    def to_pickle_car(car: Car):
        if isinstance(car, Car):
            return pickle.dumps({
                "_Car__name_model": car.name_model,
                "_Car__year_of_manufacture": car.year_of_manufacture,
                "_Car__manufacturer": car.manufacturer,
                "_Car__engine_capacity": car.engine_capacity,
                "_Car__color": car.color,
                "_Car__price": car.price,
            })
        raise TypeError(f"Переданный аргумент не является объектом класса {car.__class__.__name__}")

    @staticmethod
    def from_pickle_car(data):
        obj = pickle.loads(data)

        try:
            return Car(obj["_Car__name_model"], obj["_Car__year_of_manufacture"], obj["_Car__manufacturer"],
                       obj["_Car__engine_capacity"], obj["_Car__color"], obj["_Car__price"])
        except AttributeError as e:
            print(e)


class JsonCarAdapter:
    @staticmethod
    def to_json_car(car: Car):
        if isinstance(car, Car):
            return json.dumps({
                "_Car__name_model": car.name_model,
                "_Car__year_of_manufacture": car.year_of_manufacture,
                "_Car__manufacturer": car.manufacturer,
                "_Car__engine_capacity": car.engine_capacity,
                "_Car__color": car.color,
                "_Car__price": car.price,
            })
        raise TypeError(f"Переданный аргумент не является объектом класса {car.__class__.__name__}")

    @staticmethod
    def from_json_car(data):
        obj = json.loads(data)

        try:
            return Car(obj["_Car__name_model"], obj["_Car__year_of_manufacture"], obj["_Car__manufacturer"],
                       obj["_Car__engine_capacity"], obj["_Car__color"], obj["_Car__price"])
        except AttributeError as e:
            print(e)


def execute_application():
    my_car = "Mustang", 2017, "Ford", 5.0, "Red", 3500000
    my_car = Car.init_car(my_car)
    print(my_car)

    your_car = "Urus", 2017, "Lamborghini", 4.0, "Yellow", 16500000
    your_car = Car.init_car(your_car)
    print(your_car)

    to_pickle_car = PickleCarAdapter.to_pickle_car(my_car)
    print(f"Сериализация объекта класса Car с помощью модуля pickle:\n{to_pickle_car}")
    from_pickle_car = PickleCarAdapter.from_pickle_car(to_pickle_car)
    print(f"Десериализация объекта класса Car с помощью модуля pickle:\n{from_pickle_car}")

    to_json_car = JsonCarAdapter.to_json_car(your_car)
    print(f"\nСериализация объекта класса Car с помощью модуля json:\n{to_json_car}")
    from_json_car = JsonCarAdapter.from_json_car(to_json_car)
    print(f"Десериализация объекта класса Car с помощью модуля json:\n{from_json_car}")


if __name__ == '__main__':
    execute_application()
