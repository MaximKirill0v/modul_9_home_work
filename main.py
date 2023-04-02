from typing import Dict


# Задание 1.
# Создайте класс Passport (паспорт), который будет содержать
# паспортную информацию о гражданине страны. С помощью механизма
# наследования, реализуйте класс ForeignPassport (загран.паспорт)
# производный от Passport.

class Passport:

    def __init__(self, full_name: Dict[str, str], date_of_birth: Dict[str, str], gender: str):
        self.__full_name = full_name.copy()
        self.__date_of_birth = date_of_birth.copy()
        self.__gender = gender

    def info(self):
        print(f"Название класса: {self.__class__.__name__}\n"
              f"Полное имя: {self.__full_name['Фамилия']} {self.__full_name['Имя']} {self.__full_name['Отчество']}\n"
              f"Дата рождения: {self.__date_of_birth['Число']}.{self.__date_of_birth['Месяц']}.{self.__date_of_birth['Год']}г.\n"
              f"Пол: {self.__gender}")


def execute_application():
    full_name = {"Фамилия": "Иванов", "Имя": "Иван", "Отчество": "Иванович"}
    date_of_birth = {"Число": "01", "Месяц": "01", "Год": "2000"}
    gender = "м"
    passport = Passport(full_name, date_of_birth, gender)
    passport.info()


if __name__ == '__main__':
    execute_application()
