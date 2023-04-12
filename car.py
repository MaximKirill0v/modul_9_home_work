class Car:
    def __init__(self, car_model: str, car_body: str, color: str):
        self.__car_model = car_model
        self.__car_body = car_body
        self.__color = color

    def info(self):
        return f"Модель: {self.__car_model}, Кузов: {self.__car_body}, Цвет: {self.__color}"

