# Задание 1.
# Реализуйте класс «Человек». Необходимо хранить в полях класса: ФИО,
# дату рождения, контактный телефон, город, страну, домашний адрес.
# Реализуйте конструктор по умолчанию и метод для вывода данных.
# Реализуйте доступ к отдельным полям класса через методы класса (геттеры
# и сеттеры).
class Human:
    def __init__(self, full_name: dict[str, str], date_of_birth: dict[str, str], phone: str, city: str, country: str,
                 address: dict[str, str]):
        self.__full_name = full_name
        self.__date_of_birth = date_of_birth
        self.__phone = phone
        self.__city = city
        self.__country = country
        self.__address = address


def execute_application():
    pass


if __name__ == '__main__':
    execute_application()
