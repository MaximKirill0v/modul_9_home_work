from General_class_shape import Shape


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
