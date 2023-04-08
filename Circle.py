from General_class_shape import Shape


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