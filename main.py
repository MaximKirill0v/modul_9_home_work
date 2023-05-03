from abc import ABC, abstractmethod


# Метод send_message должен отправлять сообщение в соответствии с типом отправки: по смс, по емейл и т.д.
# Методам ваших классов не хватает параметров, чтобы выполнять свой функционал,
# вместо этого в классы для чего-то были добавлены атрибуты почты и номера телефона.
# Получается что для каждого клиента будь у него и отправка по номеру и по почте придется создать 2 экземпляра класса?
# Не рационально! Продумать другую реализацию...

# Задание 1.
# Принцип открытости-закрытости закрепим на примере созданного в
# задании 1 класса по отправке сообщений NotificationService.
# Допустим нам необходимо кроме отправки сообщения по электронной
# почте отправлять еще смс сообщения. И мы можем дописать метод sendMessage
# таким образом:
# def sendMessage(typeMessage: str, message: str) {
# if (typeMessage == "email") {
# //send email
# }
# if (typeMessage == "sms") {
# //send sms
# }
# Но в данном случае мы нарушим второй принцип, потому что класс
# должен быть закрыт для модификации, но открыт для расширения.
# Для того чтобы придерживаться принципа открытости-закрытости
# нам необходимо спроектировать наш код таким образом, чтобы каждый мог
# повторно использовать нашу функцию, просто расширив ее. Поэтому
# определим абстрактный класс NotificationService и в нем поместим метод
# sendMessage.
# Далее создайте класс EmailNotification, который наследуется от
# NotificationService и реализует метод отправки сообщений по электронной
# почте.
# Создайте аналогично класс MobileNotification, который будет отвечать
# за отправку смс сообщений.
# Проектируя таким образом код мы не будем нарушать принцип
# открытости-закрытости, так как мы расширяем нашу функциональность, а не
# изменяем (модифицируем) наш класс.

class Client:
    def __init__(self, email: str, phone_number: str):
        self.__email = email
        self.__phone_number = phone_number

    @property
    def email(self):
        return self.__email

    @property
    def phone_number(self):
        return self.__phone_number


class NotificationService(ABC):
    @abstractmethod
    def send_message(self):
        pass


class EmailNotification(NotificationService):
    def __init__(self, client: Client):
        self.__email = client.email

    def send_message(self):
        print(f"Сообщение отправлено по электронной почте по адресу: '{self.__email}'")


class MobileNotification(NotificationService):
    def __init__(self, client: Client):
        self.__phone_number = client.phone_number

    def send_message(self):
        print(f"Сообщение отправлено на номер: '{self.__phone_number}'")


def execute_application():
    client = Client("maximkir@gmail.com", "8-903-777-44-33")

    email = EmailNotification(client)
    phone_number = MobileNotification(client)
    email.send_message()
    phone_number.send_message()


if __name__ == '__main__':
    execute_application()
