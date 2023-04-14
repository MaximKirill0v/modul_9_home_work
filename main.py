from type_engine import *
from mixin_file import *


# Задание 1.
# Используя механизм множественного наследования разработайте класс
# «Автомобиль». Создайте несколько классов-наследников согласно
# классификации. Используя классы-миксины «примешайте» к классам
# наследникам методы, которые выводят информацию об объекте из классов
# «Колесо», «Двигатель», «Двери» и т.п.
def execute_application():
    tyres_gas_car = Tyre([2.0, 2.1, 2.2, 1.9])
    gas_car = GasEngine("Мазда", "Кроссовер", "Серый", 130000, "Бензин", 95)
    gas_car.info()
    gas_car.start_engine()
    print(gas_car.get_info_tyres(tyres_gas_car))
    print(gas_car.get_mileage_before_maintenance(gas_car.car_mileage) + "\n")

    tyres_diesel_car = Tyre([1.8, 2.0, 2.1, 2.3])
    diesel_car = DieselEngine("Рено", "Универсал", "Серебряный", 90000, "Дизель", 1300, 2200)
    diesel_car.info()
    diesel_car.start_engine()
    print(diesel_car.get_info_tyres(tyres_diesel_car))
    print(diesel_car.get_mileage_before_maintenance(diesel_car.car_mileage) + "\n")

    tyres_electro_car = Tyre([2.5, 2.4, 1.9, 2.0])
    electro_car = ElectroEngine("Тесла", "Седан", "Чёрный", 35000, "Электро", 550)
    electro_car.info()
    diesel_car.stop_engine()
    print(electro_car.get_info_tyres(tyres_electro_car))
    print(electro_car.get_mileage_before_maintenance(electro_car.car_mileage) + "\n")

    # tires = [StatusTireMixin.get_status_tires() for _ in range(4)]
    # print(tires)


if __name__ == '__main__':
    execute_application()
