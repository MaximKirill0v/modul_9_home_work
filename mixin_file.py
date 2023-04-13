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


class StatusTireMixin:
    @staticmethod
    def status_tire():
        stat_tires = {"Лев. переднее": 0, "Лев. заднее": 0, "Прав. переднее": 0, "Прав. заднее": 0}
        for key in stat_tires.keys():
            stat_tires[key] = random.choice(['Давление в норме', 'Низкое давление', 'Высокое давление'])
        return stat_tires


class AutoRepair(ABC):
    @abstractmethod
    def get_mileage_before_maintenance(self, mileage: float):
        pass


class MileageBeforeMaintenanceMixin(AutoRepair):
    def get_mileage_before_maintenance(self, mileage: float):
        print(mileage)
        return f"Следующее ТО через: {15000 - (mileage % 15000)} км."

