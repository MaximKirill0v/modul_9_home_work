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

    def __str__(self):
        opening_date = ".".join([value for value in self.opening_date.values()])
        return f"Название стадиона: '{self.stadium_name}'.\n" \
               f"Дата открытия: {opening_date}г.\n" \
               f"Страна: {self.country}.\n" \
               f"Город: {self.city}.\n" \
               f"Вместительность: {self.capacity:,}."


def execute_application():
    opening_date = {"Число": "31", "Месяц": "07", "Год": "1956"}
    stadium_1 = Stadium("Лужники", opening_date, "Россия", "Москва", 76880)
    print(stadium_1)


if __name__ == '__main__':
    execute_application()
