# Задание 1.
# Создайте класс для конвертирования температуры из Цельсия в
# Фаренгейты и наоборот. У класса должно быть два статических метода: для
# перевода из Цельсия в Фаренгейты и для перевода из Фаренгейта в Цельсия.

class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(temperature: float):
        return temperature * 1.8 + 32


def execute_application():
    interface_data = input("Введите '1', если хотите перевести из градусов Цельсия в градусы по Фаренгейту,\n"
                           "Введите '2', если хотите перевести из градусов по Фаренгейту в градусы Цельсия\n"
                           "Введите '0', если хотите завершить программу.\n==> ")
    while interface_data != '0':
        if interface_data == '1':
            temperature_celsius = input("Введите температуру в градусах по Цельсию: ")
            if temperature_celsius.isdigit():
                res_temperature = Temperature.celsius_to_fahrenheit(float(temperature_celsius))
                print(f"Температура в переводе на градусы по Фаренгейту равна - {res_temperature}F.")
            else:
                print("Введённое значение не корректно. Повторите ввод.")
                interface_data = input("Повторите ввод: ")



if __name__ == '__main__':
    execute_application()
