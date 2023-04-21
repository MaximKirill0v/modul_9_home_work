# Задание 2.
# Создайте класс Point (точка). Для данного класса реализуйте ряд
# перегруженных операторов:
# Проверка на равенство пар координат по осям X и Y (операция ==, !=);
# Проверка сравнения пар координат (операции >, <, <=, >=);

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __is_point(self, other):
        if not isinstance(other, Point):
            raise TypeError(f"Невозможно выполнить сравнение "
                            f"между типом {self.__class__.__name__} "
                            f"и {other.__class__.__name__}")

    def __eq__(self, other):
        self.__is_point(other)
        return self.__x == other.__x and self.__y == other.__y

    def __ne__(self, other):
        self.__is_point(other)
        return self.__x != other.__x or self.__y != other.__y

    def __lt__(self, other):
        self.__is_point(other)
        return self.__y < other.__y

    def __gt__(self, other):
        self.__is_point(other)
        return self.__y > other.__y

    def __le__(self, other):
        self.__is_point(other)
        return self.__x == other.__x and self.__y < other.__y

    def __ge__(self, other):
        self.__is_point(other)
        return self.__x == other.__x and self.__y > other.__y

    def __hash__(self):
        return hash((self.__x, self.__y))


def execute_application():
    point_1 = Point(1, 9)
    point_2 = Point(1, 3)
    try:
        print("Проверка на оператор 'равно':", point_1 == point_2)
        print("Проверка на оператор 'не равно:'", point_1 != point_2)
        # считаю, что если точка расположена выше по оси у, то она больше,
        # если ниже по оси у, то она меньше.
        print("Проверка на оператор  'меньше':", point_1 < point_2)
        print("Проверка на оператор 'больше':", point_1 > point_2)
        # считаю, что точка меньше или равна другой точке, если координаты по оси х равны,
        # а по оси у координата меньше координаты другой точки. Для оператора больше или равно наоборот.
        print("Проверка на оператор 'меньше или равно':", point_1 <= point_2)
        print("Проверка на оператор 'больше или равно':", point_1 >= point_2)
    except TypeError as e:
        print(e)


if __name__ == '__main__':
    execute_application()
