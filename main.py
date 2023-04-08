from Rectangle import *
from Square import *
from Circle import *
from Ellipse import *


# Задание 1.
# Создайте базовый класс Shape для хранения плоских фигур.
# Определите производные классы:
# Square — квадрат, который характеризуется координатами левого
# верхнего угла и длиной стороны;
# Rectangle — прямоугольник с заданными координатами верхнего
# левого угла и размерами;
# Circle — окружность с заданными координатами цен-тра и радиусом;
# Ellipse — эллипс с заданными координатами верхнего угла описанного
# вокруг него прямоугольника со сторонами, параллельными осям координат,
# и размерами этого прямоугольника.
# Создайте список фигур. Определите класс, который сохраняет фигуры
# в файлы, загружает из файла и отобразите информацию о каждой из фигур.


def execute_application():
    square = Square(0, 0, 5.0)

    rectangle = Rectangle(0, 0, 6.0, 4.0)

    circle = Circle(0, 0, 5.0)

    ellipse = Ellipse(0, 0, 8.0, 4.0)

    figures_list = [square, rectangle, circle, ellipse]
    figures = None
    try:
        for figures in figures_list:
            figures.info()
    except AttributeError as e:
        print(f"У класса '{figures.__class__.__name__}' нет такого метода.")


if __name__ == '__main__':
    execute_application()
