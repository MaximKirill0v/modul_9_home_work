import pickle


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

    @property
    def model(self):
        return self.__model

    @property
    def passenger_capacity(self):
        return self.__passenger_capacity

    @property
    def fuel_tank_volume(self):
        return self.__fuel_tank_volume

    @property
    def range_of_flight(self):
        return self.__range_of_flight

    @property
    def max_speed(self):
        return self.__max_speed

    @property
    def number_engines(self):
        return self.__number_engines

    def __str__(self):
        return f"Модель самолёта: {self.__model}\nПассажировместимость: {self.__passenger_capacity} чел.\n" \
               f"Объём топливного бака: {self.__fuel_tank_volume} л.\nМаксимальная дальность полёта: {self.__range_of_flight} км.\n" \
               f"Максимальная скорость: {self.__max_speed} км/ч\nКоличество двигателей: {self.__number_engines}"


class PickleAirplaneAdapter:
    @staticmethod
    def to_pickle_passenger_airplane(airplane: PassengerAirplane):
        if isinstance(airplane, PassengerAirplane):
            return pickle.dumps({
                "Модель": airplane.model,
                "Пассажировместимость": airplane.passenger_capacity,
                "Объём топливного бака": airplane.fuel_tank_volume,
                "Максимальная дальность полёта": airplane.range_of_flight,
                "Максимальная скорость": airplane.max_speed,
                "Количество двигателей": airplane.number_engines,
            })
        raise TypeError(f"Не поддерживаемый тип объекта для сериализации.")

    @staticmethod
    def from_pickle_passenger_airplane(data):
        obj = pickle.loads(data)
        try:
            return PassengerAirplane(obj["Модель"], obj["Пассажировместимость"], obj["Объём топливного бака"],
                                     obj["Максимальная дальность полёта"], obj["Максимальная скорость"],
                                     obj["Количество двигателей"])
        except AttributeError as e:
            print(e)


def execute_application():
    boeing = PassengerAirplane("Boeing 777", 400, 117000, 6020, 965, 2)
    try:
        boeing_to_pickle = PickleAirplaneAdapter.to_pickle_passenger_airplane(boeing)
        print(f"*Упаковка объекта класса 'PassengerAirplane' с помощью модуля Pickle:\n{boeing_to_pickle}")
        boeing_from_pickle = PickleAirplaneAdapter.from_pickle_passenger_airplane(boeing_to_pickle)
        print(f"\n*Распаковка объекта класса 'PassengerAirplane' с помощью модуля Pickle:\n{boeing_from_pickle}")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    execute_application()
