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


class Tyre:
    def __init__(self, pressure: list[float]):
        self.pressure = pressure
        self.tyres_lst = ["Лев. переднее", "Лев. заднее", "Прав. переднее", "Прав. заднее"]
        self.info_tyres = list()

    def get_pressure_info(self):
        for value in self.pressure:
            if 1.9 <= value <= 2.4:
                self.info_tyres.append("Давление в норме")
            elif 0 <= value < 1.9:
                self.info_tyres.append("Низкое давление")
            elif value > 2.4:
                self.info_tyres.append("Высокое давление")
            else:
                raise Exception(f"Не корректное значение давления.")
        return dict(zip(self.tyres_lst, self.info_tyres))


class TyreMixin:
    @staticmethod
    def get_info_tyres(tyre: Tyre):
        print(tyre.get_pressure_info())



class AutoRepair(ABC):
    @abstractmethod
    def get_mileage_before_maintenance(self, mileage: float):
        pass


class MileageBeforeMaintenanceMixin(AutoRepair):
    def get_mileage_before_maintenance(self, mileage: float):
        print(mileage)
        return f"Следующее ТО через: {15000 - (mileage % 15000)} км."
