from typing import Dict


# Задание 2.
# Реализуйте класс «Стадион». Необходимо хранить в полях класса:
# название стадиона, дату открытия, страну, город, вместимость. Реализуйте
# конструктор по умолчанию и метод для вывода данных. Реализуйте доступ к
# отдельным полям класса через методы класса (геттеры и сеттеры).
class Stadium:
    def __init__(self, stadium_name: str, opening_date: Dict[str, str], country: str, city: str, capacity: int):
        self.__stadium_name = stadium_name
        self.__opening_date = opening_date.copy()
        self.__country = country
        self.__city = city
        self.__capacity = capacity


def execute_application():
    pass


if __name__ == '__main__':
    execute_application()
