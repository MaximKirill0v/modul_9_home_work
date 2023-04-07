from abc import ABC, abstractmethod


class Shape:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y


class Square(Shape):
    def __init__(self, x: int, y: int, side: float):
        super().__init__(x, y)
        self.__side = side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side):
        self.__side = side

    def info(self):
        print(f"Класс фигуры: {self.__class__.__name__}\n"
              f"Сторона квадрата равна: {self.__side}\n"
              f"Координата верхнего левого угла равна: ({self.x}, {self.y})\n")


class Rectangle(Shape):
    def __init__(self, x: int, y: int, length: float, width: float):
        super().__init__(x, y)
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, width):
        self.width = width

    def info(self):
        print(f"Класс фигуры: {self.__class__.__name__}\n"
              f"Длина прямоугольника равна: {self.__length}\n"
              f"Ширина прямоугольника равна: {self.__width}\n"
              f"Координата верхнего левого угла равна: ({self.x}, {self.y})\n")


class Circle(Shape):
    def __init__(self, x: int, y: int, radius: float):
        super().__init__(x, y)
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    def info(self):
        print(f"Класс фигуры: {self.__class__.__name__}\n"
              f"Радиус окружности равен: {self.__radius}\n"
              f"Координата центра окружности равна: ({self.x}, {self.y})\n")


class Ellipse(Shape):
    def __init__(self, x: int, y: int, length: float, width: float):
        super().__init__(x, y)
        self.__length = length
        self.__width = width

    def get_coord_center_ellipse_inscribed_in_rectangle(self):
        self.__x = self.x + self.__length / 2
        self.__y = self.y - self.__width / 2
        return self.__x, self.__y

    def info(self):
        coord_center = self.get_coord_center_ellipse_inscribed_in_rectangle()
        print(f"Класс фигуры: {self.__class__.__name__}\n"
              f"Координата центра эллипса, относительно координат описанного вокруг"
              f" него прямоугольника равна: {coord_center}\n"
              f"Большая полуось эллипса равна: {self.__length / 2}\n"
              f"Малая полуось эллипса равна: {self.__width / 2}")
