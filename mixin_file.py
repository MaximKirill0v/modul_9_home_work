import random
from abc import ABC, abstractmethod


class EngineCondition(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class EngineStartStopMixin(EngineCondition):

    def start_engine(self):
        print(f"{self.__class__.__name__}: Двигатель заведён.")

    def stop_engine(self):
        print(f"{self.__class__.__name__}: Двигатель остановлен.")

    # class Tire:
    #     def __init__(self, pressure: float):
    #         self.__pressure = pressure
    #
    #     @property
    #     def pressure(self):
    #         return self.__pressure
    #
    #     @pressure.setter
    #     def pressure(self, pressure):
    #         self.__pressure = pressure
    #
    #     @staticmethod
    #     def get_status_tires():
    #         stat_tire = random.randint(1, 3)
    #         if stat_tire == 1:
    #             return "Низкое давление, подкачайте колесо."
    #         elif stat_tire == 2:
    #             return "Высокое давление, спустите воздух из колеса до соответствующего значения."
    #         else:
    #             return "Давление в норме."
    #
    #


class StatusTireMixin:
    @staticmethod
    def status_tire():
        stat_tires = {"Лев. переднее": None, "Лев. заднее": None, "Прав. переднее": None, "Прав. заднее": None}
        for key in stat_tires.keys():
            stat_tires[key] = random.choice(['Давление в норме', 'Низкое давление', 'Высокое давление'])
        return stat_tires


# class StatusTire:
#
#     @staticmethod
#     def get_status_tires():
#         stat_tire = random.randint(1, 3)
#         if stat_tire == 1:
#             return "Низкое давление"
#         elif stat_tire == 2:
#             return "Высокое давление"
#         else:
#             return "Давление в норме"


class AutoRepair(ABC):
    @abstractmethod
    def get_mileage_before_maintenance(self, mileage: float):
        pass


class MileageBeforeMaintenanceMixin(AutoRepair):
    def get_mileage_before_maintenance(self, mileage: float):
        print(mileage)
        return f"Следующее ТО через: {15000 - (mileage % 15000)} км."
