# Задание 1.
# Допустим у нас есть класс RentCarService и в нем есть несколько
# методов: найти машину по номеру, забронировать машину по номеру,
# распечатать заказ на бронирование, получить информацию о машине,
# отправить сообщение клиенту с информацией о его брони.
# У данного класса есть несколько зон ответственности, что является
# нарушением принципа единой ответственности, так как отвечает за разные
# действия.
# Необходимо создать класс PrinterService и вынести туда функционал по
# печати.
# Работу связанную с получением информации о машине перенести в
# класс CarInfoService.
# Метод по отправке сообщений перенести в класс NotificationService.
# Метод поиска машины по номеру в класс CarService.

class PrinterService:
    @staticmethod
    def printer_service():
        print("Заказ на бронирование распечатан.")


class CarInfoService:
    @staticmethod
    def car_info_service():
        print("Информация о машине.")


class NotificationService:
    @staticmethod
    def notification_service():
        print("Сообщение клиенту о его брони успешно отправлено.")


class CarService:
    @staticmethod
    def car_service():
        print("Информация о машине по номеру.")


class RentCarService:
    @staticmethod
    def rent_car_service():
        print("Машина забронирована по номеру.")


def execute_application():
    PrinterService.printer_service()
    CarInfoService.car_info_service()
    NotificationService.notification_service()
    CarService.car_service()
    RentCarService.rent_car_service()


if __name__ == '__main__':
    execute_application()
