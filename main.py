from car import *
from mixin_engine import *
from mixin_tyre import *


# Задание 1.
# Используя механизм множественного наследования разработайте класс
# «Автомобиль». Создайте несколько классов-наследников согласно
# классификации. Используя классы-миксины «примешайте» к классам
# наследникам методы, которые выводят информацию об объекте из классов
# «Колесо», «Двигатель», «Двери» и т.п.
def execute_application():
    gas_engine = Engine()
    gas_car = CarGasEngine("Mazda", "Кроссовер", "Серый металлик", 2014, 95)
    gas_car.info()
    # Проверка статуса двигателя
    gas_car.get_status_engine(gas_engine)
    # Проверка давления в колесе
    gas_car_tyre = TyrePressure()
    try:
        print(gas_car.get_status_tyre(gas_car_tyre, 2.0))
    except Exception as e:
        print(e)
    # Проверка состояния кондиционера
    conditioner = Conditioner()
    gas_car.get_status_conditioner(conditioner)
    print()

    diesel_engine = Engine()
    diesel_car = CarDieselEngine("Рено", "Универсал", "Белый", 2010, "ДТЛ")
    diesel_car.info()
    # Проверка статуса двигателя
    diesel_engine.state = True
    diesel_car.get_status_engine(diesel_engine)
    # Проверка давления в колесе
    diesel_car_tyre = TyrePressure()
    try:
        print(diesel_car.get_status_tyre(diesel_car_tyre, 1.8))
    except Exception as e:
        print(e)
    # Проверка состояния кондиционера
    conditioner.status_conditioner = True
    diesel_car.get_status_conditioner(conditioner)


if __name__ == '__main__':
    execute_application()
