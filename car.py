class Car:
    def __init__(self, car_model: str, car_body: str, color: str, car_mileage: float):
        self.__car_model = car_model
        self.__car_body = car_body
        self.__color = color
        self.__car_mileage = car_mileage

    @property
    def car_mileage(self):
        return self.__car_mileage

    def info(self):
        print(f"Модель: {self.__car_model}, Кузов: {self.__car_body}, Цвет: {self.__color},"
              f" Пробег: {self.__car_mileage} км.,", end=" ")
