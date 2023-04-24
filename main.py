from abc import ABC, abstractmethod


# Задание 1.
# Рассмотрим принцип разделения интерфейсов.
# Допустим у нас имеется абстрактный класс Payments и в нем есть три метода:
# оплата WebMoney, оплата банковской карточкой и оплата по номеру телефона.
# class Payments(ABC):
# @abstarctmethod
# def payWebMoney(self): pass
# @abstarctmethod
# def payCreditCard(self): pass
# @abstarctmethod
# def payPhoneNumber(self): pass
# Выполните разделение интерфейса таким образом, чтобы можно было реализовать
# два класса-сервиса, которые будут у себя реализовывать различные виды проведения
# оплат (класс InternetPaymentService и TerminalPaymentService). При этом
# TerminalPaymentService не должен поддерживать проведение оплат по номеру телефона

class PaymentWebMoney(ABC):
    @staticmethod
    @abstractmethod
    def pay_web_money():
        pass


class PaymentCreditCard(ABC):
    @staticmethod
    @abstractmethod
    def pay_credit_card():
        pass


class PaymentPhoneNumber(ABC):
    @staticmethod
    @abstractmethod
    def pay_phone_number():
        pass


class InternetPaymentService(PaymentWebMoney, PaymentCreditCard, PaymentPhoneNumber):
    @staticmethod
    def pay_web_money():
        print("Вы произвели оплату с помощью Web Money.")

    @staticmethod
    def pay_credit_card():
        print("Вы произвели оплату банковской картой.")

    @staticmethod
    def pay_phone_number():
        print("Вы произвели оплату по номеру телефона.")


class TerminalPaymentService(PaymentWebMoney, PaymentCreditCard):
    @staticmethod
    def pay_web_money():
        print("Вы произвели оплату с помощью Web Money.")

    @staticmethod
    def pay_credit_card():
        print("Вы произвели оплату банковской картой.")


def execute_application():
    pay_1 = InternetPaymentService
    pay_1.pay_phone_number()

    pay_2 = TerminalPaymentService
    pay_2.pay_web_money()


if __name__ == '__main__':
    execute_application()
