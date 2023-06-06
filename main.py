
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
    def __init__(self, notation: str, num: str):
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
        if isinstance(notation, str):
            return notation in ('bin', 'oct', 'dec', 'hex')
        return False

    def __is_num(self, number: str):
        if self.__notation == 'bin':
            for num in number:
                if num not in '01':
                    return False
            return True

        elif self.__notation == 'oct':
            for num in number:
                if num not in '01234567':
                    return False
            return True

        elif self.__notation == 'dec':
            for num in number:
                if num not in '0123456789':
                    return False
            return True

        elif self.__notation == 'hex':
            for num in number:
                if num not in '0123456789abcdefABCDEF':
                    return False
            return True

    def __setattr__(self, key, value):
        if key == '_Digit__notation' and not self.__is_notation(value):
            raise ValueError(f"Не корректная запись системы счисления: {value}")
        if key == '_Digit__num' and not self.__is_num(value):
            raise ValueError(f"Не корректная запись числа: {value} в системе счисления {self.__notation}")
        super().__setattr__(key, value)

    def __str__(self):
        return f"Число: {self.__num}, система счисления: {self.__notation}"


class NumberSystemsCalculator:
    __notation_dict = {'bin': 2, 'oct': 8, 'dec': 10, 'hex': 16}

    def digit_to_bin(self, digit: Digit):
        if digit.notation != 'bin':
            return Digit('bin', bin(int(str(int(digit.num, self.__notation_dict[digit.notation]))))[2:])
        raise NotationValueError(f"Ошибка конвертации. Перевод в ту же СС.")

    def digit_to_oct(self, digit: Digit):
        if digit.notation != 8:
            return Digit('oct', oct(int(str(int(digit.num, self.__notation_dict[digit.notation]))))[2:])
        raise NotationValueError(f"Ошибка конвертации. Перевод в ту же СС.")

    def digit_to_dec(self, digit: Digit):
        if digit.notation != 10:
            return Digit('dec', str(int(digit.num, self.__notation_dict[digit.notation])))
        raise NotationValueError(f"Ошибка конвертации. Перевод в ту же СС.")

    def digit_to_hex(self, digit: Digit):
        if digit.notation != 16:
            return Digit('hex', hex(int(digit.num, self.__notation_dict[digit.notation]))[2:])
        raise NotationValueError(f"Ошибка конвертации. Перевод в ту же СС.")


def execute_application():
    try:
        number = Digit('dec', '1000')
        try:
            calculator = NumberSystemsCalculator()

            print(calculator.digit_to_hex(number))

            print(calculator.digit_to_oct(number))

            print(calculator.digit_to_bin(number))

            print(calculator.digit_to_dec(number))

        except NotationValueError as e:
            print(e)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    execute_application()
