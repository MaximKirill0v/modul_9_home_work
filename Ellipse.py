from General_class_shape import Shape


class Ellipse(Shape):
    def __init__(self, x: int, y: int, length: float, width: float):
        super().__init__(x, y)
        self.__length = length
        self.__width = width
        self.__coord_center = self.x + self.__length / 2, self.y - self.__width / 2
        self.__major_axis = self.__length / 2
        self.__semi_minor_axis = self.__width / 2

    def info(self):
        print(f"Класс фигуры: {self.__class__.__name__}\n"
              f"Координата центра эллипса, относительно координат описанного вокруг"
              f"него прямоугольника равна: {self.__coord_center}\n"
              f"Большая полуось эллипса равна: {self.__major_axis}\n"
              f"Малая полуось эллипса равна: {self.__semi_minor_axis}")

    def get_date_figure(self):
        return {"Класс": self.__class__.__name__, "Координаты": self.__coord_center, "Большая полуось": self.__major_axis,
                "Малая полуось": self.__semi_minor_axis}
