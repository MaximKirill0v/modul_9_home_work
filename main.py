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
        self.__radius = radius

    def __get_circumference(self):
        return 2 * pi * self.__radius

    @staticmethod
    def __is_valid_radius(radius: float):
        return radius > 0 if isinstance(radius, int | float) else False

    def __setattr__(self, key, value):
        if key == '_Circle__radius' and not self.__is_valid_radius(value):
            raise InitializationValueError(f"Не корректное значение радиуса окружности: {value}.")
        else:
            object.__setattr__(self, key, value)

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
        return self.__get_circumference() < other.__get_circumference()

    def __gt__(self, other):
        self.__is_circle(other)
        return self.__get_circumference() > other.__get_circumference()

    def __le__(self, other):
        self.__is_circle(other)
        return self.__get_circumference() <= other.__get_circumference()

    def __ge__(self, other):
        self.__is_circle(other)
        return self.__get_circumference() >= other.__get_circumference()

    def __hash__(self):
        return hash(self.__radius)

    def __add__(self, other):
        if isinstance(other, int | float):
            if other < 0 and abs(other) >= self.__radius:
                raise InvalidValueError(
                    f"Невозможно выполнить операцию сложения с отрицательным числом, большим по модулю "
                    f"чем радиус окружности. Радиус окружности"
                    f" не может быть отрицательным или быть равным нулю.")
            t = self.__radius + other
            return Circle(t)

    def __sub__(self, other):
        if isinstance(other, int | float):
            if abs(other) >= self.__radius:
                raise InvalidValueError(
                    f"Модуль вычитаемого числа больше либо равен, чем величина радиуса. Радиус окружности"
                    f" не может быть отрицательным или быть равным нулю.")
            t = self.__radius - other
            return Circle(t)

    def __iadd__(self, other):
        if isinstance(other, int | float):
            if abs(other) >= self.__radius and other < 0:
                raise InvalidValueError(
                    f"Невозможно выполнить операцию сложения с отрицательным числом, большим по модулю "
                    f"чем радиус окружности. Радиус окружности"
                    f" не может быть отрицательным или быть равным нулю.")
            self.__radius = self.__radius + other
            return self

    def __isub__(self, other):
        if isinstance(other, int | float):
            if abs(other) >= self.__radius:
                raise InvalidValueError(
                    f"Невозможно выполнить операцию сложения с отрицательным числом, большим по модулю "
                    f"чем радиус окружности. Радиус окружности"
                    f" не может быть отрицательным или быть равным нулю.")
            self.__radius = self.__radius - other
            return self


def execute_application():
    try:
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

    except InitializationValueError as e:
        print(e)

    circle_1 = Circle(10)
    num = 3
    try:
        circle_3 = circle_1 + num
        print(f"\nОперация сложения: {circle_3.radius}.")
        circle_3 = circle_1 - num
        print(f"Операция вычитания: {circle_3.radius}.")
        circle_1 += num
        print(f"Операция сложения с присваиванием: {circle_1.radius}.")
        circle_1 -= num
        print(f"Операция вычитания с присваиванием: {circle_1.radius}.")

    except Exception as e:
        print(e)


if __name__ == '__main__':
    execute_application()
