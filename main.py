# Задание 1.
# Создайте класс «Самолет». Наполните его необходимыми характеристиками и методами. Реализуйте упаковку и
# распаковку объектов класса «Самолет» с использованием
# модуля pickle.
class PassengerAirplane:
    def __init__(self, model: str, passenger_capacity: int, fuel_tank_volume: float, range_of_flight: float,
                 max_speed: float, number_engines: int):
        self.__model = model
        self.__passenger_capacity = passenger_capacity
        self.__fuel_tank_volume = fuel_tank_volume
        self.__range_of_flight = range_of_flight
        self.__max_speed = max_speed
        self.__number_engines = number_engines

    def __str__(self):
        return f"Модель самолёта: {self.__model}\nПассажировместимость: {self.__passenger_capacity} чел.\n"\
               f"Объём топливного бака: {self.__fuel_tank_volume} л.\nДальность полёта: {self.__range_of_flight} км.\n"\
               f"Максимальная скорость: {self.__max_speed} км/ч\nКоличество двигателей: {self.__number_engines}"


def execute_application():
    boeing = PassengerAirplane("Boeing 777", 400, 117000, 6020, 965, 2)
    print(boeing)


if __name__ == '__main__':
    execute_application()
