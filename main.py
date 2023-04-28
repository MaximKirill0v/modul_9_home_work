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
    def __init__(self, numerator: int, denominator: int = 1):
        num_1 = abs(numerator)
        num_2 = abs(denominator)
        if denominator > 0:
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

    def __lt__(self, other):
        self.__is_fraction(other)
        if isinstance(other, Fraction):
            return self.__numerator / self.__denominator < other.__numerator / other.__denominator
        if isinstance(other, int | float):
            return self.__numerator / self.__denominator < other

    def __gt__(self, other):
        self.__is_fraction(other)
        if isinstance(other, Fraction):
            return self.__numerator / self.__denominator > other.__numerator / other.__denominator
        if isinstance(other, int | float):
            return self.__numerator / self.__denominator > other

    def __le__(self, other):
        self.__is_fraction(other)
        if isinstance(other, Fraction):
            return self.__numerator / self.__denominator <= other.__numerator / other.__denominator
        if isinstance(other, int | float):
            return self.__numerator / self.__denominator <= other

    def __ge__(self, other):
        self.__is_fraction(other)
        if isinstance(other, Fraction):
            return self.__numerator / self.__denominator >= other.__numerator / other.__denominator
        if isinstance(other, int | float):
            return self.__numerator / self.__denominator >= other

    def __add__(self, other):
        self.__is_fraction(other)
        if isinstance(other, Fraction):
            if self.__denominator == other.__denominator:
                t = self.__numerator + other.__numerator
                return Fraction(int(t), int(self.__denominator))
            else:
                temp_numerator = (self.__numerator * other.__denominator + other.__numerator * self.__denominator)
                temp_denominator = self.__denominator * other.__denominator
                return Fraction(int(temp_numerator), int(temp_denominator))
        if isinstance(other, int):
            temp_numerator = self.__numerator + other * self.__denominator
            return Fraction(int(temp_numerator), int(self.__denominator))


def execute_application():
    fraction_1 = None
    fraction_2 = None
    try:
        fraction_1 = Fraction(1, 2)
        fraction_2 = Fraction(1, 5)
    except DenominatorError as e:
        print(e)

    try:
        # print(f"Сравнение на равенство дробей:", fraction_1 == fraction_2)
        # print(f"Сравнение на равенство дроби и целого числа:", fraction_1 == 1)
        # print(f"Сравнение на равенство дроби и числа с плавающей точкой:", fraction_1 == 0.5)
        #
        # print(f"\nСравнение на не равенство дробей:", fraction_1 != fraction_2)
        # print(f"Сравнение на не равенство дроби и целого числа:", fraction_1 != 1)
        # print(f"Сравнение на не равенство дроби и числа с плавающей точкой:", fraction_1 != 0.5)
        #
        # print(f"\nСравнение дробей на оператор меньше:", fraction_1 < fraction_2)
        # print(f"Сравнение дроби и целого числа на оператор меньше:", fraction_1 < 10)
        # print(f"Сравнение дроби и числа с плавающей точкой на оператор меньше:", fraction_1 < 1.2)
        #
        # print(f"\nСравнение дробей на оператор больше:", fraction_1 > fraction_2)
        # print(f"Сравнение дроби и целого числа на оператор больше:", fraction_1 > 10)
        # print(f"Сравнение дроби и числа с плавающей точкой на оператор больше:", fraction_1 > 1.2)
        #
        # print(f"\nСравнение дробей на оператор меньше либо равно:", fraction_1 <= fraction_2)
        # print(f"Сравнение дроби и целого числа на оператор меньше либо равно:", fraction_1 <= 10)
        # print(f"Сравнение дроби и числа с плавающей точкой на оператор меньше либо равно:", fraction_1 <= 1.2)
        #
        # print(f"\nСравнение дробей на оператор больше либо равно:", fraction_1 >= fraction_2)
        # print(f"Сравнение дроби и целого числа на оператор больше либо равно:", fraction_1 >= 10)
        # print(f"Сравнение дроби и числа с плавающей точкой на оператор больше либо равно:", fraction_1 >= 1.2)

        print(f"\nОперация сложения двух дробей:", fraction_1 + fraction_2)
        print(f"Операция сложения дроби и целого числа:", fraction_1 + 2)

    except TypeError as e:
        print(e)


if __name__ == '__main__':
    execute_application()
