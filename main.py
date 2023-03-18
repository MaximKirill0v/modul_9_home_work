# Задание 2.
# Реализуйте класс «Стадион». Необходимо хранить в полях класса:
# название стадиона, дату открытия, страну, город, вместимость. Реализуйте
# конструктор по умолчанию и метод для вывода данных.

class Stadium:
    stadium_name: str
    opening_date: dict[str, str]
    country: str
    city: str
    capacity: int

    def __init__(self, stadium_name: str, opening_date: dict[str, str], country: str, city: str, capacity: int):
        self.stadium_name = stadium_name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity


def execute_application():
    opening_date = {"Число": "31", "Месяц": "07", "Год": "1956"}
    luzhniki_stadium = Stadium("Luzhniki", opening_date, "Россия", "Москва", 76880)


if __name__ == '__main__':
    execute_application()
