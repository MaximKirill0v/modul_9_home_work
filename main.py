from type_engine import *


# Задание 1.
# Используя механизм множественного наследования разработайте класс
# «Автомобиль». Создайте несколько классов-наследников согласно
# классификации. Используя классы-миксины «примешайте» к классам
# наследникам методы, которые выводят информацию об объекте из классов
# «Колесо», «Двигатель», «Двери» и т.п.
def execute_application():
    gas_car = GasEngine("Мазда", "Кроссовер", "Серый", "Бензин", 95)
    gas_car.info()
    gas_car.start_engine()

    diesel_car = DieselEngine("Рено", "Универсал", "Серебряный", "Дизель", 1300, 2200)
    diesel_car.info()
    diesel_car.start_engine()

    electro_car = ElectroEngine("Тесла", "Седан", "Чёрный", "Электро", 550)
    electro_car.info()
    diesel_car.stop_engine()


if __name__ == '__main__':
    execute_application()
