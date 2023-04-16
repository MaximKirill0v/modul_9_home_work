class Conditioner:
    def __init__(self):
        self.__status = False

    @property
    def status_conditioner(self):
        return self.__status

    @status_conditioner.setter
    def status_conditioner(self, value: bool):
        self.__status = value

    def info_status_conditioner(self):
        return "Кондиционер включён." if self.__status else "Кондиционер выключен."


class StatusConditionerMixin:
    @staticmethod
    def get_status_conditioner(conditioner: Conditioner):
        print(conditioner.info_status_conditioner())
