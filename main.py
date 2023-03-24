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
    def init_from_file(cls, path: str):
        with open(path, "r", encoding="utf-8") as file:
            file = (file.readline().strip()).split()
            full_name = {"Фамилия": file[0], "Имя": file[1], "Отчество": file[2]}
            date_of_birth = {"Число": file[3], "Месяц": file[4], "Год": file[5]}
            phone = file[6]
            city = file[7]
            country = file[8]
            address = {"Страна": file[9], "Область": file[10], "Город": file[11], "Улица": file[12],
                       "Дом": file[13], "Квартира": file[14]}
            return cls(full_name, date_of_birth, phone, city, country, address)

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
    human_1 = Human.init_from_file(path_to_file)
    print(human_1)


if __name__ == '__main__':
    execute_application()
