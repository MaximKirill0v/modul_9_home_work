from abc import ABC, abstractmethod
from copy import copy


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

    @abstractmethod
    def do_authentication(self, nick_name: str):
        pass


class AnonymousAuthentication(Authentication):
    def do_authentication(self, nick_name: str):
        print(f"{nick_name} - вы прошли анонимную аутентификацию.")


class GithubAuthentication(Authentication):

    def do_authentication(self, nick_name: str):
        print(f"{nick_name} - вы прошли аутентификацию GitHub.")


class FacebookAuthentication(Authentication):

    def do_authentication(self, nick_name: str):
        print(f"{nick_name} - вы прошли аутентификацию на Facebook.")


class Permissions:

    def __init__(self, auth: AnonymousAuthentication):
        self.__auth = copy(auth)

    def get_permissions(self, nick_name: str):
        self.__auth.do_authentication(nick_name)


def execute_application():
    auth = AnonymousAuthentication()
    auth.do_authentication("Anonim")

    anonim = Permissions(auth)
    anonim.get_permissions("Maxim")


if __name__ == '__main__':
    execute_application()
