# Задание 2.
# Реализуйте класс «Стадион». Необходимо хранить в полях класса:
# название стадиона, дату открытия, страну, город, вместимость. Реализуйте
# конструктор по умолчанию и метод для вывода данных.

class Stadium:
    stadium_name: str
    opening_date: dict[str, int]
    country: str
    city: str
    capacity: int

    def __init__(self, stadium_name: str, opening_date: dict[str, int], country: str, city: str, capacity: int):
        self.stadium_name = stadium_name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity


def execute_application():
    pass


if __name__ == '__main__':
    execute_application()
