# Задание 1.
# Реализуйте класс Retailltem (товарная единица), который содержит
# данные о товаре в магазине. Этот класс должен хранить данные в атрибутах:
# описание товара, количество единиц на складе и цена. После написания
# этого класса напишите программу, которая создает три объекта Retailitem.
# Создайте класс CashRegister (Кассовый аппарат), который может
# использоваться вместе с классом Retailltem. Класс CashRegister должен иметь
# внутренний список объектов Retailltem, а также приведенные ниже методы:
# Метод purchase_item() (приобрести товар) в качестве аргумента
# принимает объект Retailltem. При каждом вызове метода purchase_item()
# объект Retailltem, передан­ный в качестве аргумента, должен быть добавлен в
# список.
# Метод get_total () (получить сумму покупки) возвращает общую
# стоимость всех объектов Retailltem, хранящихся во внутреннем списке
# объекта CashRegister.
# Метод show_iterns () (показать товары) выводит данные об объектах
# Retailltem, хранящихся во внутреннем списке объекта CashRegister.
# Метод clear () (очистить) должен очистить внутренний список объекта
# CashRegister.
# Продемонстрируйте класс CashRegister в программе, которая
# позволяет пользователю выбрать несколько товаров для покупки. Когда
# пользователь готов рассчитаться за покупку, программа должна вывести
# список всех товаров, которые он выбрал для покупки, а также их общую
# стоимость.

class RetailItem:
    def __init__(self, info_item: str, number_of_units: int = 0, price: float = 0):
        self.__info_item = info_item
        self.__number_of_units = number_of_units
        self.__price = price

    @property
    def info_item(self):
        return self.__info_item

    @property
    def number_of_units(self):
        return self.__number_of_units

    @number_of_units.setter
    def number_of_units(self, value):
        self.__number_of_units = value

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f"Наименование товара: {self.__info_item}, Количество единиц на складе: {self.__number_of_units}," \
               f" Цена: {self.__price} р."


class CashRegister:
    def __init__(self):
        self.__all_items = dict()

    @property
    def all_items(self):
        return self.__all_items

    def purchase_item(self, item: RetailItem, quantity: int = 1):
        """
        Добавляет в словарь продукты для покупки.
        :param item: RetailItem: товарная единица.
        :param quantity: int: количество товарных единиц для покупки.
        :return:
        """

        if quantity <= item.number_of_units:  # Если товара на складе хватает по наличию.
            item.number_of_units -= quantity
            if item.info_item in self.__all_items:
                self.__all_items[item.info_item]["Количество"] += quantity
            else:
                self.__all_items[item.info_item] = {"Количество": quantity, "Цена": item.price}

        else:  # Если товара на складе недостаточно.
            max_quantity = item.number_of_units
            item.number_of_units = 0

            if item.info_item in self.__all_items:  # Если товар уже есть в корзине
                self.__all_items[item.info_item]["Количество"] += max_quantity
                print(f"Товара {item.info_item} на складе не достаточно."
                      f" В корзину положено {max_quantity} шт.")

            else:
                self.__all_items[item.info_item] = {"Количество": max_quantity, "Цена": item.price}
                print(f"Товара {item.info_item} на складе не достаточно. В корзину положено {max_quantity} шт.")

    def get_total(self) -> float:
        """
        Возвращает итоговую стоимость корзины.
        :return:
                float: итоговая стоимость корзины.
        """
        return sum(values["Цена"] * values["Количество"] for values in self.__all_items.values())

    def show_items(self):
        """
        Выводит в консоль информацию о покупаемых товарах.
        :return:
        """
        if len(self.__all_items) == 0:
            print("Пока ваша корзина пустая.")
        else:
            print(f"Наименование товара    Цена       Количество")
            for key, values in self.__all_items.items():
                print(key.ljust(22), str(values["Цена"]).ljust(10), str(values["Количество"]).ljust(5))

    def clear(self):
        """
        Очищает словарь товаров.
        :return:
        """
        self.__all_items.clear()
        print("Спасибо за покупку.")


def execute_application():
    chocolate = RetailItem("Snickers", 10, 60)
    lemonade = RetailItem("Дюшес", 10, 45)
    chips = RetailItem("Lays", 20, 100)
    ice_cream = RetailItem("Нота-Му", 20, 75)

    cash_register = CashRegister()
    cash_register.purchase_item(chocolate, 5)
    cash_register.purchase_item(lemonade, 4)
    cash_register.purchase_item(chips, 2)
    cash_register.purchase_item(ice_cream, 4)
    cash_register.purchase_item(chocolate, 3)

    cash_register.show_items()
    print(f"\nИтоговая стоимость: {cash_register.get_total()} р.")

    cash_register.clear()


if __name__ == '__main__':
    execute_application()
