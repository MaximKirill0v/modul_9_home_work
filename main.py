# Задание 1.
# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:название модели,
# год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте конструктор по умолчанию
# и метод для вывода данных.

class Car:
    name_model: str
    year_of_manufacture: int
    manufacturer: str
    engine_capacity: float
    color: str
    price: float

    def __init__(self, name_model: str, year_of_manufacture: int, manufacturer: str, engine_capacity: float, color: str,
                 price: float):
        self.name_model = name_model
        self.year_of_manufacture = year_of_manufacture
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price


def execute_application():
    pass


if __name__ == '__main__':
    execute_application()
