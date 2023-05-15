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
class InitializationValueError(Exception):
    def __init__(self, text):
        self.__text = text


class Fraction(InitializationValueError):
    def __init__(self, numerator: int, denominator: int = 1):
        self.__numerator = numerator
        self.__denominator = denominator

    @staticmethod
    def __get_fraction_reduction(numerator: int, denominator: int):

        num_1 = abs(numerator)
        num_2 = abs(denominator)
        while num_1 != 0 and num_2 != 0:
            if num_1 > num_2:
                num_1 %= num_2
            else:
                num_2 %= num_1
        if num_1 > 0:
            numerator = numerator / num_1
            denominator = denominator / num_1
        else:
            numerator = numerator / num_2
            denominator = denominator / num_2
        return int(numerator), int(denominator)

    @staticmethod
    def __is_valid_numerator(number: int):
        return isinstance(number, int)

    @staticmethod
    def __is_valid_denominator(number: int):
        return isinstance(number, int) and number > 0

    def __setattr__(self, key, value):
        if key == "_Fraction__numerator" and not self.__is_valid_numerator(value):
            raise InitializationValueError(f"Не корректный тип числителя: {value}")
        if key == "_Fraction__denominator" and not self.__is_valid_denominator(value):
            raise InitializationValueError(f"Не корректное значение знаменателя: {value}")
        object.__setattr__(self, key, value)

    def __str__(self):
        if self.__denominator == 1:
            return f"{int(self.__numerator)}"
        return f"{int(self.__numerator)}/{int(self.__denominator)}"

    def __is_fraction(self, other):
        if not isinstance(other, Fraction | int | float):
            raise TypeError(f"Невозможно выполнить арифметические операции между типами {self.__class__.__name__} и "
                            f"{other.__class__.__name__}.")

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
                fraction = self.__get_fraction_reduction(int(t), int(self.__denominator))
                return Fraction(*fraction)
            else:
                temp_numerator = (self.__numerator * other.__denominator + other.__numerator * self.__denominator)
                temp_denominator = self.__denominator * other.__denominator
                fraction = self.__get_fraction_reduction(int(temp_numerator), int(temp_denominator))
                return Fraction(*fraction)
        if isinstance(other, int):
            temp_numerator = self.__numerator + other * self.__denominator
            fraction = self.__get_fraction_reduction(int(temp_numerator), int(self.__denominator))
            return Fraction(*fraction)

    def __iadd__(self, other):
        self.__is_fraction(other)
        if isinstance(other, Fraction):
            if self.__denominator == other.__denominator:
                self.__numerator = self.__numerator + other.__numerator
                self.__get_fraction_reduction(self.__numerator, self.__denominator)
                return self
            else:
                self.__numerator = (self.__numerator * other.__denominator + other.__numerator * self.__denominator)
                self.__denominator = self.__denominator * other.__denominator
                self.__get_fraction_reduction(self.__numerator, self.__denominator)
                return self
        if isinstance(other, int):
            self.__numerator = self.__numerator + other * self.__denominator
            self.__get_fraction_reduction(self.__numerator, self.__denominator)
            return self

    def __sub__(self, other):
        self.__is_fraction(other)
        if isinstance(other, Fraction):
            if self.__denominator == other.__denominator:
                t = self.__numerator - other.__numerator
                fraction = self.__get_fraction_reduction(int(t), int(self.__denominator))
                return Fraction(*fraction)
            else:
                temp_numerator = (self.__numerator * other.__denominator - other.__numerator * self.__denominator)
                temp_denominator = self.__denominator * other.__denominator
                fraction = self.__get_fraction_reduction(int(temp_numerator), int(temp_denominator))
                return Fraction(*fraction)
        if isinstance(other, int):
            temp_numerator = self.__numerator - other * self.__denominator
            fraction = self.__get_fraction_reduction(int(temp_numerator), int(self.__denominator))
            return Fraction(*fraction)

    def __isub__(self, other):
        self.__is_fraction(other)
        if isinstance(other, Fraction):
            if self.__denominator == other.__denominator:
                self.__numerator = self.__numerator - other.__numerator
                self.__get_fraction_reduction(self.__numerator, self.__denominator)
                return self
            else:
                self.__numerator = (self.__numerator * other.__denominator - other.__numerator * self.__denominator)
                self.__denominator = self.__denominator * other.__denominator
                self.__get_fraction_reduction(self.__numerator, self.__denominator)
                return self
        if isinstance(other, int):
            self.__numerator = self.__numerator - other * self.__denominator
            self.__get_fraction_reduction(self.__numerator, self.__denominator)
            return self

    def __mul__(self, other):
        self.__is_fraction(other)
        if isinstance(other, Fraction):
            fraction = self.__get_fraction_reduction(int(self.__numerator * other.__numerator),
                                                     int(self.__denominator * other.__denominator))
            return Fraction(*fraction)
        if isinstance(other, int):
            fraction = self.__get_fraction_reduction(int(self.__numerator * other), int(self.__denominator))
            return Fraction(*fraction)

    def __imul__(self, other):
        self.__is_fraction(other)
        if isinstance(other, Fraction):
            self.__numerator = self.__numerator * other.__numerator
            self.__denominator = self.__denominator * self.__denominator
            self.__get_fraction_reduction(self.__numerator, self.__denominator)
            return self
        if isinstance(other, int):
            self.__numerator = self.__numerator * other
            self.__get_fraction_reduction(self.__numerator, self.__denominator)
            return self

    def __truediv__(self, other):
        self.__is_fraction(other)
        if isinstance(other, Fraction):
            temp_numerator = self.__numerator * other.__denominator
            temp_denominator = self.__denominator * other.__numerator
            fraction = self.__get_fraction_reduction(int(temp_numerator), int(temp_denominator))
            return Fraction(*fraction)
        if isinstance(other, int):
            temp_denominator = self.__denominator * other
            fraction = self.__get_fraction_reduction(int(self.__numerator), int(temp_denominator))
            return Fraction(*fraction)

    def __itruediv__(self, other):
        self.__is_fraction(other)
        if isinstance(other, Fraction):
            self.__numerator = self.__numerator * other.__denominator
            self.__denominator = self.__denominator * other.__numerator
            self.__get_fraction_reduction(self.__numerator, self.__denominator)
            return self
        if isinstance(other, int):
            self.__denominator = self.__denominator * other
            self.__get_fraction_reduction(self.__numerator, self.__denominator)
            return self


def execute_application():
    fraction_1 = None
    fraction_2 = None
    number = 4
    try:
        fraction_1 = Fraction(4, 8)
        fraction_2 = Fraction(2, 6)

        try:
            print(f"Сравнение на равенство дробей:", fraction_1 == fraction_2)
            print(f"Сравнение на равенство дроби и целого числа:", fraction_1 == 1)
            print(f"Сравнение на равенство дроби и числа с плавающей точкой:", fraction_1 == 0.5)

            print(f"\nСравнение на не равенство дробей:", fraction_1 != fraction_2)
            print(f"Сравнение на не равенство дроби и целого числа:", fraction_1 != 1)
            print(f"Сравнение на не равенство дроби и числа с плавающей точкой:", fraction_1 != 0.5)

            print(f"\nСравнение дробей на оператор меньше:", fraction_1 < fraction_2)
            print(f"Сравнение дроби и целого числа на оператор меньше:", fraction_1 < 10)
            print(f"Сравнение дроби и числа с плавающей точкой на оператор меньше:", fraction_1 < 1.2)

            print(f"\nСравнение дробей на оператор больше:", fraction_1 > fraction_2)
            print(f"Сравнение дроби и целого числа на оператор больше:", fraction_1 > 10)
            print(f"Сравнение дроби и числа с плавающей точкой на оператор больше:", fraction_1 > 1.2)

            print(f"\nСравнение дробей на оператор меньше либо равно:", fraction_1 <= fraction_2)
            print(f"Сравнение дроби и целого числа на оператор меньше либо равно:", fraction_1 <= 10)
            print(f"Сравнение дроби и числа с плавающей точкой на оператор меньше либо равно:", fraction_1 <= 1.2)

            print(f"\nСравнение дробей на оператор больше либо равно:", fraction_1 >= fraction_2)
            print(f"Сравнение дроби и целого числа на оператор больше либо равно:", fraction_1 >= 10)
            print(f"Сравнение дроби и числа с плавающей точкой на оператор больше либо равно:", fraction_1 >= 1.2)

            print(f"\nОперация сложения двух дробей: {fraction_1} + {fraction_2} =", fraction_1 + fraction_2)
            print(f"Операция сложения дроби и целого числа: {fraction_1} + {number} =", fraction_1 + number)

            print(f"\nОперация сложения с присваиванием двух дробей: "
                  f"{fraction_1} += {fraction_2}, ответ fraction_1 = {fraction_1 + fraction_2}")

            print(f"Операция сложения c присваиванием дроби и целого числа:"
                  f" {fraction_1} += {number}, ответ fraction_1 = {fraction_1 + number}")

            print(f"\nОперация вычитания двух дробей: {fraction_1} - {fraction_2} =", fraction_1 - fraction_2)
            print(f"Операция вычитания дроби и целого числа: {fraction_1} - {number} =", fraction_1 - number)

            print(f"\nОперация вычитания с присваиванием двух дробей: "
                  f"{fraction_1} -= {fraction_2}, ответ fraction_1 = {fraction_1 - fraction_2}")

            print(f"Операция вычитания c присваиванием дроби и целого числа:"
                  f" {fraction_1} -= {number}, ответ fraction_1 = {fraction_1 - number}")

            print(f"\nОперация умножения дробей: {fraction_1} * {fraction_2} =", fraction_1 * fraction_2)
            print(f"Операция умножения дроби на число: {fraction_1} * {number} =", fraction_1 * number)

            print(f"\nОперация умножения с присваиванием дробей {fraction_1} *= {fraction_2}"
                  f" ответ fraction_1 = {fraction_1 * fraction_2}")
            print(f"Операция умножения  с присваиванием дроби на число {fraction_1} *= {number}"
                  f" ответ fraction_1 = {fraction_1 * number}")

            print(f"\nОперация деления дробей: {fraction_1} / {fraction_2} =", fraction_1 / fraction_2)
            print(f"Операция деления дроби на число: {fraction_1} / {number} =", fraction_1 / number)

            print(f"\nОперация деления с присваиванием дробей {fraction_1} /= {fraction_2}"
                  f" ответ fraction_1 = {fraction_1 / fraction_2}")
            print(f"Операция деления  с присваиванием дроби на число {fraction_1} /= {number}"
                  f" ответ fraction_1 = {fraction_1 / number}")

        except TypeError as e:
            print(e)

    except InitializationValueError as e:
        print(e)


if __name__ == '__main__':
    execute_application()
