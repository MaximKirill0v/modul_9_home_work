# Задание 1.
# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
# название модели, год выпуска, производителя, объем двигателя, цвет машины,
# цену. Реализуйте конструктор по умолчанию и метод для вывода данных.
# Реализуйте доступ к отдельным полям класса через методы класса (геттеры
# и сеттеры).

class Car:
    def __init__(self, name_model: str, year_of_manufacture: int, manufacturer: str, engine_capacity: float, color: str,
                 price: float):
        self.__name_model = name_model
        self.__year_of_manufacture = year_of_manufacture
        self.__manufacturer = manufacturer
        self.__engine_capacity = engine_capacity
        self.__color = color
        self.__price = price


def execute_application():
    pass


if __name__ == '__main__':
    execute_application()
