from car import Car


class GasEngine(Car):
    def __init__(self, car_model: str, car_body: str, color: str, fuel_type: str):
        super().__init__(car_model, car_body, color)
        self.__fuel_type = fuel_type

    def info(self):
        super().info()
        print(f"Тип топлива: Бензин")


class DieselEngine(Car):
    def __init__(self, car_model: str, car_body: str, color: str, fuel_type: str):
        super().__init__(car_model, car_body, color)
        self.__fuel_type = fuel_type

    def info(self):
        super().info()
        print(f"Тип топлива: Дизель")


class ElectroEngine(Car):
    def __init__(self, car_model: str, car_body: str, color: str, fuel_type: str):
        super().__init__(car_model, car_body, color)
        self.__fuel_type = fuel_type

    def info(self):
        super().info()
        print(f"Тип топлива: Электро")
