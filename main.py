from math import pi


# Задание 1.
# Создайте класс Circle (окружность). Для данного класса реализуйте ряд
# перегруженных операторов:
# Проверка на равенство радиусов двух окружностей (операция ==, !=);
# Проверка сравнения длин двух окружностей (операции >, <, <=,>=);

class InitializationValueError(Exception):
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


def execute_application():
    try:
        circle_1 = Circle(2)
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


if __name__ == '__main__':
    execute_application()
