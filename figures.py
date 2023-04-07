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


