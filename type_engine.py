from car import Car
from mixin_file import *


class GasEngine(Car, EngineConditionMixin, StatusTireMixin):
    def __init__(self, car_model: str, car_body: str, color: str, fuel_type: str, brand_gasoline: int = None):
        super().__init__(car_model, car_body, color)
        self.__fuel_type = fuel_type
        self.__brand_gasoline = brand_gasoline

    def info(self):
        super().info()
        if self.__brand_gasoline is None:
            print(f"Тип топлива: {self.__fuel_type}, Марка бензина: Не определено")
        else:
            print(f"Тип топлива: {self.__fuel_type}, Марка бензина: {self.__brand_gasoline}")


class DieselEngine(Car, EngineConditionMixin, StatusTireMixin):
    def __init__(self, car_model: str, car_body: str, color: str, fuel_type: str, min_hpfp_pressure: float = None,
                 max_hpfp_pressure: float = None):
        super().__init__(car_model, car_body, color)
        self.__fuel_type = fuel_type
        self.__min_hpfp_pressure = min_hpfp_pressure
        self.__max_hpfp_pressure = max_hpfp_pressure

    def info(self):
        super().info()
        print(f"Тип топлива: {self.__fuel_type}, Мин. давление тнвд: {self.__min_hpfp_pressure} бар, "
              f"Макс. давление тнвд: {self.__max_hpfp_pressure} бар")


class ElectroEngine(Car, EngineConditionMixin, StatusTireMixin):
    def __init__(self, car_model: str, car_body: str, color: str, fuel_type: str, power_reserve: float = "Не задано"):
        super().__init__(car_model, car_body, color)
        self.__fuel_type = fuel_type
        self.__power_reserve = power_reserve

    def info(self):
        super().info()
        print(f"Тип топлива: {self.__fuel_type}, Запас хода: {self.__power_reserve} км")
