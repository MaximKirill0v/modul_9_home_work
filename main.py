# Задание 1.
# Создайте класс Обыкновенная дробь. Используя перегрузку операторов
# реализуйте для него арифметические операции и операции сравнения для
# работы с обыкновенными дробями.
# В классе должна быть реализована следующая функциональность:
# * Сложение дробей;
# * Вычитание дробей;
# * Умножение дробей;
# * Деление дробей.
# * Сравнение дробей
# В т.ч. Перегрузка операций должна работать с целыми числам
class DenominatorError(Exception):
    def __init__(self, text):
        self.__text = text


class Fraction(DenominatorError):
    def __init__(self, numerator: int, denominator: int):
        num_1 = abs(numerator)
        num_2 = abs(denominator)
        if denominator > 0:
            if num_1 % num_2 == 0 or num_2 % num_1 == 0:
                while num_1 != 0 and num_2 != 0:
                    if num_1 > num_2:
                        num_1 %= num_2
                    else:
                        num_2 %= num_1
                if num_1 > 0:
                    self.__numerator = numerator / num_1
                    self.__denominator = denominator / num_1
                else:
                    self.__numerator = numerator / num_2
                    self.__denominator = denominator / num_2
            else:
                self.__numerator = numerator
                self.__denominator = denominator
        else:
            raise DenominatorError("Знаменатель не может быть меньше или равен нулю.")

    def __str__(self):
        if self.__denominator == 1:
            return f"{int(self.__numerator)}"
        return f"{int(self.__numerator)}/{int(self.__denominator)}"


def execute_application():
    try:
        fraction = Fraction(10, 5)
        print(fraction)

    except DenominatorError as e:
        print(e)


if __name__ == '__main__':
    execute_application()
