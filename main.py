from abc import ABC, abstractmethod


# Задание 1.
# Создайте класс «Число», которое хранит его значение и информацию о
# системе счисления. Создайте несколько экземпляров данного класса.
# Создайте класс «Калькулятор СС». В классе должна быть реализована
# следующая функциональность:
# Перевод числа в восьмеричную систему счисления.
# Перевод числа в шестнадцатеричную систему счисления.
# Перевод числа в двоичную систему счисления.
# Перевод числа в десятичную систему счисления.
class NotationValueError(Exception):
    def __init__(self, text: str):
        self.__text = text


class Number:
    def __init__(self, notation: int, num: str):
        self.__notation = notation
        self.__num = num

    @property
    def notation(self):
        return self.__notation

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        self.__num = value

    @staticmethod
    def __is_notation(notation: int):
        if isinstance(notation, int):
            return notation in (2, 8, 10, 16)
        return False

    def __is_num(self, number: str):
        if self.__notation == 2:
            for num in number:
                if num not in ('0', '1'):
                    return False
            return True
        elif self.__notation == 8:
            for num in number:
                if num not in '01234567':
                    return False
            return True
        elif self.__notation == 10:
            for num in number:
                if num not in '0123456789':
                    return False
            return True
        elif self.__notation == 16:
            for num in number:
                if num not in '0123456789ABCDEF':
                    return False
            return True

    def __setattr__(self, key, value):
        if key == '_Number__notation' and not self.__is_notation(value):
            raise ValueError(f"Не корректная запись системы счисления: {self.__notation}")
        if key == '_Number__num' and not self.__is_num(value):
            raise ValueError(f"Не корректная запись числа: {value} в {self.__notation}-ой системе счисления.")
        super().__setattr__(key, value)

    def __str__(self):
        return f"Число: {self.__num}, система счисления: {self.__notation}"


class NumberSystemsCalculator(ABC):
    @staticmethod
    @abstractmethod
    def conversion_number(num: Number):
        raise NotImplementedError


class BinaryNumberSystem(NumberSystemsCalculator, NotationValueError):
    @staticmethod
    def conversion_number(num: Number):
        if num.notation != 2:
            return f"Число в {num.notation}-ой СС {num.num} в двоичной СС равно: {bin(int(str(int(num.num, num.notation))))[2:]}"
        raise NotationValueError(f"Ошибка конвертации. Перевод в ту же СС.")


class OctalNumberSystem(NumberSystemsCalculator, NotationValueError):
    @staticmethod
    def conversion_number(num: Number):
        if num.notation != 8:
            return f"Число в {num.notation}-ой СС {num.num} в восьмеричной СС равно: {oct(int(str(int(num.num, 16))))[2:]}"
        raise NotationValueError(f"Ошибка конвертации. Перевод в ту же СС.")


class DecimalNumberSystem(NumberSystemsCalculator, NotationValueError):
    @staticmethod
    def conversion_number(num: Number):
        if num.notation != 10:
            return f"Число в {num.notation}-ой СС {num.num} в десятеричной СС равно: {int(num.num, num.notation)}"
        raise NotationValueError(f"Ошибка конвертации. Перевод в ту же СС.")


class HexadecimalNumberSystem(NumberSystemsCalculator, NotationValueError):
    @staticmethod
    def conversion_number(num: Number):
        if num.notation != 16:
            return f"Число в {num.notation}-ой СС {num.num} в шестнадцатеричной СС равно: {hex(int(num.num))[2:]}"
        raise NotationValueError(f"Ошибка конвертации. Перевод в ту же СС.")


def execute_application():
    try:
        number_2 = Number(2, '101')
        number_8 = Number(8, '257')
        number_10 = Number(10, '29')
        number_16 = Number(16, '4F5')
        try:
            print(BinaryNumberSystem.conversion_number(number_8))
            print(OctalNumberSystem.conversion_number(number_2))
            print(DecimalNumberSystem.conversion_number(number_16))
            print(HexadecimalNumberSystem.conversion_number(number_10))

        except NotationValueError as e:
            print(e)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    execute_application()
