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


class InternationalPassport(Passport):
    def __init__(self, full_name: Dict[str, str], date_of_birth: Dict[str, str], gender: str, series: str,
                 passport_no: str, state_code: str, date_of_issue: Dict[str, str], expiration_date: Dict[str, str]):
        super().__init__(full_name, date_of_birth, gender)
        self.__series = series
        self.__passport_no = passport_no
        self.__state_code = state_code
        self.__date_of_issue = date_of_issue
        self.__expiration_date = expiration_date

    def info(self):
        super().info()
        print(f"Серия паспорта: {self.__series}\n"
              f"Номер паспорта: {self.__passport_no}\n"
              f"Код государства: {self.__state_code}\n"
              f"Дата выдачи: {self.__date_of_issue['Число']}.{self.__date_of_issue['Месяц']}.{self.__date_of_issue['Год']}г.\n"
              f"Дата окончания срока действия: {self.__expiration_date['Число']}.{self.__expiration_date['Месяц']}."
              f"{self.__expiration_date['Год']}г.")


def execute_application():
    full_name = {"Фамилия": "Иванов", "Имя": "Иван", "Отчество": "Иванович"}
    date_of_birth = {"Число": "01", "Месяц": "01", "Год": "2000"}
    gender = "м"
    passport = Passport(full_name, date_of_birth, gender)
    passport.info()
    print()

    full_name = {"Фамилия": "Степанов", "Имя": "Степан", "Отчество": "Степанович"}
    date_of_birth = {"Число": "10", "Месяц": "10", "Год": "2010"}
    gender = "м"
    series = "73"
    passport_no = "0838439"
    state_code = "RUS"
    date_of_issue = {"Число": "20", "Месяц": "12", "Год": "2012"}
    expiration_date = {"Число": "20", "Месяц": "12", "Год": "2022"}

    international_passport = InternationalPassport(full_name, date_of_birth, gender, series, passport_no, state_code,
                                                   date_of_issue, expiration_date)
    international_passport.info()


if __name__ == '__main__':
    execute_application()
