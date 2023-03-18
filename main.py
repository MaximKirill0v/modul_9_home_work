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

    def __str__(self):
        return f"Модель автомобиля - '{self.name_model}'.\n" \
               f"Год выпуска - {self.year_of_manufacture}г.\n" \
               f"Производитель - {self.manufacturer}.\n" \
               f"Объём двигателя - {self.engine_capacity}л.\n" \
               f"Цвет кузова - {self.color}.\n" \
               f"Цена - {self.price:,.2f}р."


def execute_application():
    my_car = Car("Mustang", 2017, "Ford", 5.0, "Red", 3500000)
    print(my_car)


if __name__ == '__main__':
    execute_application()
