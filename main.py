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


class Digit:
    def __init__(self, notation: int, num: str):
        self.__notation = notation
        self.__num = num

    @property
    def notation(self):
        return self.__notation

    @notation.setter
    def notation(self, value):
        self.__notation = value

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        self.__num = value

    @staticmethod
    def __is_notation(notation: str):
        return isinstance(notation, int) and notation > 0

    def __is_num(self, number: str):

        notation_dict = {1: '1', 2: '01', 3: '012', 4: '0123', 5: '01234', 6: '012345', 7: '0123456', 8: '01234567',
                         9: '012345678', 10: '0123456789', 11: '0123456789A', 12: '0123456789AB', 13: '0123456789ABC',
                         14: '0123456789ABCD', 15: '0123456789ABCDE', 16: '0123456789ABCDEF'}

        for num in number:
            if num.upper() not in notation_dict[self.__notation]:
                return False
        return True

    def __setattr__(self, key, value):
        if key == '_Digit__notation' and value not in range(1, 17):
            raise ValueError(f"Не поддерживаемая СС: {value}.")
        if key == '_Digit__notation' and not self.__is_notation(value):
            raise ValueError(f"Не корректная запись системы счисления: {value}")
        if key == '_Digit__num' and not self.__is_num(value):
            raise ValueError(f"Не корректная запись числа: {value} в системе счисления {self.__notation}")
        super().__setattr__(key, value)

    def __str__(self):
        return f"Число: {self.__num}, система счисления: {self.__notation}"


class Decorator:
    @staticmethod
    def uppercase_translation(func):
        def wrapper(*args, **kwargs):
            digit = func(*args, **kwargs)
            digit.num = digit.num.upper()
            return digit

        return wrapper


class NumberSystemsCalculator:

    @staticmethod
    def digit_to_bin(digit: Digit):
        if digit.notation != 2:
            if digit.notation == 1:
                digit.notation = 10
                digit.num = str(len(digit.num))
            return Digit(2, bin(int(str(int(digit.num, digit.notation))))[2:])
        raise NotationValueError(f"Попытка перевода в ту же СС.")

    @staticmethod
    def digit_to_oct(digit: Digit):
        if digit.notation != 8:
            if digit.notation == 1:
                digit.notation = 10
                digit.num = str(len(digit.num))
            return Digit(8, oct(int(str(int(digit.num, digit.notation))))[2:])
        raise NotationValueError(f"Попытка перевода в ту же СС.")

    @staticmethod
    def digit_to_dec(digit: Digit):
        if digit.notation != 10:
            if digit.notation == 1:
                digit.notation = 10
                digit.num = str(len(digit.num))
            return Digit(10, str(int(digit.num, digit.notation)))
        raise NotationValueError(f"Попытка перевода в ту же СС.")

    @staticmethod
    @Decorator.uppercase_translation
    def digit_to_hex(digit: Digit):
        if digit.notation != 16:
            if digit.notation == 1:
                digit.notation = 10
                digit.num = str(len(digit.num))
            return Digit(16, hex(int(digit.num, digit.notation))[2:])
        raise NotationValueError(f"Попытка перевода в ту же СС.")


def execute_application():
    try:
        number = Digit(10, '1000')
        print(f"Число до перевода: СС - {number.notation}, значение - {number.num}")
        try:
            calculator = NumberSystemsCalculator()

            number = calculator.digit_to_hex(number)
            print(f"Число после перевода в {number.notation}-ую СС: {number.num}")

            number = calculator.digit_to_oct(number)
            print(f"Число после перевода в {number.notation}-ую СС: {number.num}")

            number = calculator.digit_to_bin(number)
            print(f"Число после перевода в {number.notation}-ую СС: {number.num}")

            number = calculator.digit_to_dec(number)
            print(f"Число после перевода в {number.notation}-ую СС: {number.num}")

        except NotationValueError as e:
            print(e)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    execute_application()
