from General_class_shape import Shape


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
