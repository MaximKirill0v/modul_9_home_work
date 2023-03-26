from typing import Dict


# Задание 1.
# Реализуйте класс «Человек». Необходимо хранить в полях класса: ФИО,
# дату рождения, контактный телефон, город, страну, домашний адрес.
# Реализуйте конструктор по умолчанию и метод для вывода данных.
# Реализуйте доступ к отдельным полям класса через методы класса (геттеры
# и сеттеры).
# Реализуйте в классе «Человек» дополнительный метод класса и
# статический метод.
class Human:
    @classmethod
    def init_from_data_human(cls, data_human: list, index: int):
        """Создаёт объект класса Human"""
        if index > len(data_human) - 1:
            raise IndexError(f"Индекс больше длины списка базы данных!")
        human = data_human[index].split()
        full_name = {"Фамилия": human[0], "Имя": human[1], "Отчество": human[2]}
        date_of_birth = {"Число": human[3], "Месяц": human[4], "Год": human[5]}
        phone = human[6]
        city = human[7]
        country = human[8]
        address = {"Страна": human[9], "Область": human[10], "Город": human[11], "Улица": human[12],
                   "Дом": human[13], "Квартира": human[14]}
        return cls(full_name, date_of_birth, phone, city, country, address)

    @staticmethod
    def read_data_human_in_file(path: str):
        """Считывает базу данных из файла"""
        try:
            with open(path, "r", encoding="utf-8") as file:
                data_human = file.read().strip().split('\n')
                print(f"Файл '{path}' успешно считан.")
                return data_human
        except FileNotFoundError:
            print(f"Не удалось открыть файл по указанному пути '{path}'")

    def __init__(self, full_name: Dict[str, str], date_of_birth: Dict[str, str], phone: str, city: str, country: str,
                 address: Dict[str, str]):
        self.__full_name = full_name.copy()
        self.__date_of_birth = date_of_birth.copy()
        self.__phone = phone
        self.__city = city
        self.__country = country
        self.__address = address.copy()

    def __str__(self):
        return f"ФИО: {' '.join(self.full_name.values())}\n" \
               f"Дата рождения: {'.'.join(self.date_of_birth.values())}\n" \
               f"Контактный телефон: {self.__phone}\n" \
               f"Страна: {self.__country}\n" \
               f"Город: {self.__city}\n" \
               f"Адрес: Страна: {self.address['Страна']}, Область: {self.address['Область']}," \
               f" Город: {self.address['Город']}, Улица: {self.address['Улица']}, Дом: {self.address['Дом']}, " \
               f"Квартира: {self.address['Квартира']}."

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name: dict[str, str]):
        self.__full_name = full_name

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: dict[str, str]):
        self.__date_of_birth = date_of_birth

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: dict[str, str]):
        self.__address = address


def execute_application():
    path_to_file = "human_data.txt"
    try:
        data_human = Human.read_data_human_in_file(path_to_file)
        human_1 = Human.init_from_data_human(data_human, 0)
        print(human_1)
        human_2 = Human.init_from_data_human(data_human, 1)
        print(human_2)
        human_3 = Human.init_from_data_human(data_human, 2)
        print(human_3)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    execute_application()
