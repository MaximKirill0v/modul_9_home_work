import random


class EngineConditionMixin:
    @staticmethod
    def start_engine():
        print("Двигатель заведён.")

    @staticmethod
    def stop_engine():
        print("Двигатель остановлен.")


class StatusTireMixin:
    @staticmethod
    def status_tire():
        stat_tires = {"Лев. переднее": 0, "Лев. заднее": 0, "Прав. переднее": 0, "Прав. заднее": 0}
        for key in stat_tires.keys():
            stat_tires[key] = random.choice(['Давление в норме', 'Низкое давление', 'Высокое давление'])
        return stat_tires

