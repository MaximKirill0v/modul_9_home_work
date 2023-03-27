# Задание 1.
# Создайте класс для конвертирования температуры из Цельсия в
# Фаренгейты и наоборот. У класса должно быть два статических метода: для
# перевода из Цельсия в Фаренгейты и для перевода из Фаренгейта в Цельсия.

class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(temperature: float):
        return temperature * 1.8 + 32

    @staticmethod
    def fahrenheit_to_celsius(temperature: float):
        return (temperature - 32) / 1.8


def interface():
    """
    Выводит данные интерфейса в консоль.
    :return:
    """
    print("Введите '1', если хотите перевести из градусов Цельсия в градусы по Фаренгейту,\n"
          "Введите '2', если хотите перевести из градусов по Фаренгейту в градусы Цельсия\n"
          "Введите '0', если хотите завершить программу.")


def execute_application():
    interface()
    interface_data = input("==> ")
    while interface_data != '0':
        if interface_data == '1':
            try:
                temperature_celsius = float(input("Введите температуру в градусах по Цельсию: "))
                res_temperature = Temperature.celsius_to_fahrenheit(temperature_celsius)
                print(f"Температура в переводе на градусы по Фаренгейту равна {res_temperature}F.\n")
                interface()
                interface_data = input("==> ")
            except ValueError:
                print("Введённое значение не корректно. Повторите ввод.")
                interface()
                interface_data = input("==> ")
        elif interface_data == '2':
            try:
                temperature_fahrenheit = float(input("Введите температуру в градусах по Фаренгейту: "))
                res_temperature = Temperature.fahrenheit_to_celsius(temperature_fahrenheit)
                print(f"Температура в переводе на градусы по Цельсию равна {res_temperature}C.\n")
                interface()
                interface_data = input("==> ")
            except ValueError:
                print("Введённое значение не корректно. Повторите ввод.")
                interface()
                interface_data = input("==> ")
        else:
            interface()
            interface_data = input("==> ")


if __name__ == '__main__':
    execute_application()
