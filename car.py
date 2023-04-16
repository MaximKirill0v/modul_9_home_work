from mixin_engine import *
from mixin_tyre import *
from mixin_conditioner import *


class Car:
    def __init__(self, car_model: str, car_body: str, color: str, year: int):
        self.__car_model = car_model
        self.__car_body = car_body
        self.__color = color
        self.__year = year

    def info(self):
        print(f"Модель: {self.__car_model}, Кузов: {self.__car_body}, Цвет: {self.__color}, Год выпуска: {self.__year},"
              , end=" ")


# Машина с бензиновым двигателем (Дочерний класс от класса Car)
class CarGasEngine(Car, EngineConditionMixin, TyrePressureRatingMixin, StatusConditionerMixin):
    def __init__(self, car_model: str, car_body: str, color: str, year: int, brand_gasoline: int = None):
        super().__init__(car_model, car_body, color, year)
        self.__brand_gasoline = brand_gasoline

    def info(self):
        super().info()
        print(f"Марка бензина: {self.__brand_gasoline}")


# Машина с дизельным двигателем (Дочерний класс от класса Car)
class CarDieselEngine(Car, EngineConditionMixin, TyrePressureRatingMixin, StatusConditionerMixin):
    def __init__(self, car_model: str, car_body: str, color: str, year: int, type_diesel_fuel: str):
        super().__init__(car_model, car_body, color, year)
        self.__type_diesel_fuel = type_diesel_fuel

    def info(self):
        super().info()
        print(f"Тип дизельного топлива: {self.__type_diesel_fuel}")
