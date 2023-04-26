from math import pi


# Задание 1.
# Создайте класс Circle (окружность). Для данного класса реализуйте ряд
# перегруженных операторов:
# Проверка на равенство радиусов двух окружностей (операция ==, !=);
# Проверка сравнения длин двух окружностей (операции >, <, <=,>=);
# Пропорциональное изменение размеров окружности, путем изменения
# ее радиуса (операции + - += -=)

class InitializationValueError(Exception):
    def __init__(self, text):
        self.__text = text


class InvalidValueError(Exception):
    def __init__(self, text):
        self.__text = text


class Circle:
    def __init__(self, radius: float):
        if radius <= 0:
            raise InitializationValueError("Радиус окружности должен быть больше нуля.")
        self.__radius = radius
        self.__circumference = 2 * pi * self.__radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    def __is_circle(self, other):
        if not isinstance(other, Circle):
            raise TypeError(f"Невозможно выполнить сравнение "
                            f"между типом {self.__class__.__name__} "
                            f"и {other.__class__.__name__}")

    def __eq__(self, other):
        self.__is_circle(other)
        return self.__radius == other.__radius

    def __ne__(self, other):
        self.__is_circle(other)
        return self.__radius != other.__radius

    def __lt__(self, other):
        self.__is_circle(other)
        return self.__circumference < other.__circumference

    def __gt__(self, other):
        self.__is_circle(other)
        return self.__circumference > other.__circumference

    def __le__(self, other):
        self.__is_circle(other)
        return self.__circumference <= other.__circumference

    def __ge__(self, other):
        self.__is_circle(other)
        return self.__circumference >= other.__circumference

    def __hash__(self):
        return hash((self.__radius, self.__circumference))

    def __add__(self, other):
        if isinstance(other, int | float):
            if other < 0 and abs(other) >= self.__radius:
                raise InvalidValueError(
                    f"Невозможно выполнить операцию сложения с отрицательным числом, большим по модулю "
                    f"чем радиус окружности. Радиус окружности"
                    f" не может быть отрицательным или быть равным нулю.")
            t = self.__radius + other
            return Circle(t)
        raise TypeError(
            f"Невозможно выполнить сложение между типом {self.__class__.__name__} и {other.__class__.__name__}")

    def __sub__(self, other):
        if isinstance(other, int | float):
            if abs(other) >= self.__radius:
                raise InvalidValueError(
                    f"Модуль вычитаемого числа больше либо равен, чем величина радиуса. Радиус окружности"
                    f" не может быть отрицательным или быть равным нулю.")
            t = self.__radius - other
            return Circle(t)
        raise TypeError(
            f"Невозможно выполнить сложение между типом {self.__class__.__name__} и {other.__class__.__name__}")


def execute_application():
    circle_1 = Circle(10)
    circle_2 = Circle(20)

    try:
        print("Проверка на оператор 'равно':", circle_1 == circle_2)
        print("Проверка на оператор 'не равно':", circle_1 != circle_2)
        print("Проверка на оператор  'меньше':", circle_1 < circle_2)
        print("Проверка на оператор 'больше':", circle_1 > circle_2)
        print("Проверка на оператор 'меньше или равно':", circle_1 <= circle_2)
        print("Проверка на оператор 'больше или равно':", circle_1 >= circle_2)
    except TypeError as e:
        print(e)

    try:
        circle_3 = circle_1 + 10
        print(circle_3.radius)
        circle_3 = circle_1 - 3
        print(circle_3.radius)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    execute_application()
