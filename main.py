from typing import Dict


# Задание 1.
# Создайте класс Device, который содержит информацию об устройстве.
# С помощью механизма наследования, реализуйте класс CoffeeMachine
# (содержит информацию о кофемашине), класс Blender (содержит информацию
# о блендере).
class Device:
    def __init__(self, device_name: str, type_of_power: str, size: Dict[str, float], price: float):
        self.__device_name = device_name
        self.__type_of_power = type_of_power
        self.__size = size.copy()
        self.__price = price


def execute_application():
    pass


if __name__ == '__main__':
    execute_application()
