from Rectangle import *
from Square import *
from Circle import *
from Ellipse import *
from figure_management import *


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
    path_to_file = "figures_file/square.json"
    data_square = square.get_date_figure()
    FigureManagement.save_data_to_a_file(path_to_file, data_square, square.__class__.__name__)
    reading_data_square = FigureManagement.read_data_to_a_file(path_to_file)
    print(f"Считанные данные из файла '{path_to_file}': {reading_data_square}\n")

    rectangle = Rectangle(0, 1, 6.0, 4.0)
    path_to_file = "figures_file/rectangle.json"
    data_rectangle = rectangle.get_date_figure()
    FigureManagement.save_data_to_a_file(path_to_file, data_rectangle, square.__class__.__name__)
    reading_data_rectangle = FigureManagement.read_data_to_a_file(path_to_file)
    print(f"Считанные данные из файла '{path_to_file}': {reading_data_rectangle}\n")

    circle = Circle(0, 0, 5.0)
    path_to_file = "figures_file/circle.json"
    data_circle = circle.get_date_figure()
    FigureManagement.save_data_to_a_file(path_to_file, data_circle, circle.__class__.__name__)
    reading_data_circle = FigureManagement.read_data_to_a_file(path_to_file)
    print(f"Считанные данные из файла '{path_to_file}': {reading_data_circle}\n")

    ellipse = Ellipse(0, 0, 8.0, 4.0)
    path_to_file = "figures_file/ellipse.json"
    data_ellipse = ellipse.get_date_figure()
    print(data_ellipse)
    FigureManagement.save_data_to_a_file(path_to_file, data_ellipse, ellipse.__class__.__name__)
    reading_data_ellipse = FigureManagement.read_data_to_a_file(path_to_file)
    print(f"Считанные данные из файла '{path_to_file}': {reading_data_ellipse}\n")

    figures_list = [square, rectangle, circle, ellipse]
    figures = None
    try:
        for figures in figures_list:
            figures.info()
    except AttributeError as e:
        print(f"У класса '{figures.__class__.__name__}' нет такого метода.")


if __name__ == '__main__':
    execute_application()
