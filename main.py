from typing import Tuple


# Задание 1.
# Создайте класс Device, который содержит информацию об устройстве.
# С помощью механизма наследования, реализуйте класс CoffeeMachine
# (содержит информацию о кофе машине), класс Blender (содержит информацию
# о блендере).
class Device:
    def __init__(self, device_name: str, type_of_power: str, price: float = None):
        self.__device_name = device_name
        self.__type_of_power = type_of_power
        self.__price = price

    def info(self):
        if self.__price is None:
            self.__price = "Не задано."
        else:
            self.__price = str(self.__price) + "р."
        print(f"Название класса: {self.__class__.__name__}\n"
              f"Название устройства: {self.__device_name}\n"
              f"Тип питания: {self.__type_of_power}\n"
              f"Цена: {self.__price}")


class CoffeeMachine(Device):
    def __init__(self, device_name: str, type_of_power: str, power: int,
                 type_of_coffee: tuple, price: float = None, max_pressure: int = None):
        super().__init__(device_name, type_of_power, price)
        self.__max_pressure = max_pressure
        self.__power = power
        self.__type_of_coffee = type_of_coffee

    def info(self):
        super().info()
        if self.__max_pressure is None:
            self.__max_pressure = "Не задано."
        else:
            self.__max_pressure = str(self.__max_pressure) + " бар."
        print(f"Максимальное давление: {self.__max_pressure}\n"
              f"Мощность: {self.__power} Вт.\n"
              f"Тип используемого кофе: {', '.join(self.__type_of_coffee)}")


class Blender(Device):
    def __init__(self, device_name: str, type_of_power: str, type_blender: str, price: float = None,
                 number_of_speeds: int = None):
        super().__init__(device_name, type_of_power, price)
        self.__type_blender = type_blender
        self.__number_of_speeds = number_of_speeds

    def info(self):
        if self.__number_of_speeds is None:
            self.__number_of_speeds = "Не задано."
        else:
            self.__number_of_speeds = str(self.__number_of_speeds)
        super().info()
        print(f"Тип блендера: {self.__type_blender}\n"
              f"Количество скоростей: {self.__number_of_speeds}")


def execute_application():
    device = Device("Компьютерная мышка", "Батарейка")
    device.info()
    print()

    coffee_machine = CoffeeMachine("Кофе машина", "От сети", 15, ("зерновой", "молотый"), 40000, 15)
    coffee_machine.info()
    print()

    blender = Blender("Блендер", "От сети", "Погружной", 5000, 2)
    blender.info()
    print()


if __name__ == '__main__':
    execute_application()
