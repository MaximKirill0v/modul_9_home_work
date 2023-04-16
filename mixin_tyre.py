# Класс Давление в колесе
class TyrePressure:
    MIN = 1.9
    MAX = 2.5

    def __init__(self):
        self.__value = 0

    @classmethod
    def get_status_tyre(cls, value: float = 0):
        if not isinstance(value, float | int):
            raise Exception(f"Не корректное значение давления.")
        if TyrePressure.MIN <= value <= TyrePressure.MAX:
            return "Давление в колесе в норме."
        elif value < TyrePressure.MIN:
            return "Низкое давление в колесе."
        else:
            return "Высокое давление в колесе."


class TyrePressureRatingMixin:  # Оценка давления в колесе
    @staticmethod
    def get_status_tyre(tyre: TyrePressure, value: float = 0):
        return tyre.get_status_tyre(value)
