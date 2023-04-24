from abc import ABC, abstractmethod


# Задание 2.
# Рассмотрим принцип инверсии зависимостей. Исправьте следующий код таким
# образом, чтобы классы и верхних, и нижних уровней зависели от одних и тех же
# абстракций, а не от конкретных реализаций.
# class AnonymousAuthentication:
# def do_authentication(self): pass
# class GithubAuthentication:
# def doAuthentication(self): pass
# class FacebookAuthentication:
# def doAuthentication(self): pass
# class Permissions:
# def __init__(self, auth: AnonymousAuthentication)
# self.auth = auth
# def getPermissions(self):
# self.auth.doAuthentication()
class Authentication(ABC):
    @staticmethod
    @abstractmethod
    def do_authentication():
        pass


class AnonymousAuthentication(Authentication):
    def do_authentication(self):
        pass


class GithubAuthentication(Authentication):

    def do_authentication(self):
        pass


class FacebookAuthentication(Authentication):

    def do_authentication(self):
        pass


class Permissions:

    def __init__(self, auth: AnonymousAuthentication):
        self.__auth = auth

    def get_permissions(self):
        self.__auth.do_authentication()


def execute_application():
    pass


if __name__ == '__main__':
    execute_application()
