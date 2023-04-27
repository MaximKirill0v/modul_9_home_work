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

    def __is_fraction(self, other):
        if not isinstance(other, Fraction | int | float):
            raise TypeError(f"Невозможно выполнить операции сравнения между типами {self.__class__.__name__} и "
                            f"{other.__class__.__name__}")

    def __hash__(self):
        return hash((self.__numerator, self.__denominator))

    def __eq__(self, other):
        self.__is_fraction(other)
        if isinstance(other, Fraction):
            return self.__numerator == other.__numerator and self.__denominator == other.__denominator
        if isinstance(other, int | float):
            return self.__numerator / self.__denominator == other

    def __ne__(self, other):
        self.__is_fraction(other)
        if isinstance(other, Fraction):
            return self.__numerator != other.__numerator or self.__denominator != other.__denominator
        if isinstance(other, int | float):
            return self.__numerator / self.__denominator != other


def execute_application():
    fraction_1 = None
    fraction_2 = None
    try:
        fraction_1 = Fraction(5, 10)
        fraction_2 = Fraction(5, 5)
    except DenominatorError as e:
        print(e)

    try:
        print(f"Сравнение на равенство дробей:", fraction_1 == fraction_2)
        print(f"Сравнение на равенство дроби и целого числа:", fraction_1 == 1)
        print(f"Сравнение на равенство дроби и числа с плавающей точкой:", fraction_1 == 0.5)

        print(f"\nСравнение на не равенство дробей:", fraction_1 != fraction_2)
        print(f"Сравнение на не равенство дроби и целого числа:", fraction_1 != 1)
        print(f"Сравнение на не равенство дроби и числа с плавающей точкой:", fraction_1 != 0.5)
    except TypeError as e:
        print(e)


if __name__ == '__main__':
    execute_application()
