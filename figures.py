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
              f"Координата верхнего левого угла равна: ({self.x}, {self.y})")
