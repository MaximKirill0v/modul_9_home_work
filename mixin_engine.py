class Engine:
    def __init__(self):
        self.__status_engine = False

    @property
    def state(self):
        return self.__status_engine

    @state.setter
    def state(self, value: bool):
        self.__status_engine = value

    def info_status_engine(self):
        return "Двигатель заведен." if self.__status_engine else "Двигатель не заведен."


class EngineConditionMixin:
    @staticmethod
    def get_status_engine(engine: Engine):
        print(engine.info_status_engine())
