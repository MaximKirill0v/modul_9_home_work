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

    @property
    def num(self):
        return self.__num

    @staticmethod
    def __is_notation(notation: str):
        return isinstance(notation, int) and notation > 0

    def __is_num(self, number: str):
        if self.__notation == 2:
            for num in number:
                if num not in '01':
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
                if num not in '0123456789abcdefABCDEF':
                    return False
            return True

    def __setattr__(self, key, value):
        if key == '_Digit__notation' and value not in (2, 8, 10, 16):
            raise ValueError(f"Не поддерживаемая СС: {value}.")
        if key == '_Digit__notation' and not self.__is_notation(value):
            raise ValueError(f"Не корректная запись системы счисления: {value}")
        if key == '_Digit__num' and not self.__is_num(value):
            raise ValueError(f"Не корректная запись числа: {value} в системе счисления {self.__notation}")
        super().__setattr__(key, value)

    def __str__(self):
        return f"Число: {self.__num}, система счисления: {self.__notation}"


class NumberSystemsCalculator:

    @staticmethod
    def digit_to_bin(digit: Digit):
        if digit.notation != 2:
            return Digit(2, bin(int(str(int(digit.num, digit.notation))))[2:])
        raise NotationValueError(f"Попытка перевода в ту же СС.")

    @staticmethod
    def digit_to_oct(digit: Digit):
        if digit.notation != 8:
            return Digit(8, oct(int(str(int(digit.num, digit.notation))))[2:])
        raise NotationValueError(f"Попытка перевода в ту же СС.")

    @staticmethod
    def digit_to_dec(digit: Digit):

        if digit.notation != 10:
            return Digit(10, str(int(digit.num, digit.notation)))
        raise NotationValueError(f"Попытка перевода в ту же СС.")

    @staticmethod
    def digit_to_hex(digit: Digit):
        if digit.notation != 16:
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
