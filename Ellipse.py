from General_class_shape import Shape


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
