from UnitConverter import UnitConverter


# Задание 1.
# Создайте класс для перевода из метрической системы в английскую и
# наоборот. Функциональность необходимо реализовать в виде статических
# методов.
def execute_application():
    unit = 10
    # перевод миллиметров в дюймы
    result = UnitConverter.millimeters_to_inches(unit)
    print(f"{unit} миллиметров равно {result:.3f} дюймов.")

    # перевод дюймов в миллиметры
    result = UnitConverter.inches_to_millimeters(unit)
    print(f"{unit} дюймов равно {result:.3f} миллиметров.")

    # перевод метров в футы
    result = UnitConverter.meters_to_foot(unit)
    print(f"{unit} метров равно {result:.3f} футов.")

    # перевод футов в метры
    result = UnitConverter.foot_to_meters(unit)
    print(f"{unit} футов равно {result:.3f} метров.")

    # перевод килограммов в фунты
    result = UnitConverter.kilograms_to_lb(unit)
    print(f"{unit} килограммов равно {result:.3f} фунтов.")

    # перевод фунтов в килограммы
    result = UnitConverter.lb_to_kilograms(unit)
    print(f"{unit} фунтов равно {result:.3f} килограммов.")


if __name__ == '__main__':
    execute_application()
