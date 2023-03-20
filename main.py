# Задание 2.
# Реализуйте класс «Книга». Необходимо хранить в полях класса:
# название книги, год выпуска, издателя, жанр, автора, цену. Реализуйте
# конструктор по умолчанию и метод для вывода данных. Реализуйте доступ к
# отдельным полям класса через методы класса (геттеры и сеттеры).
class Book:
    def __init__(self, book_title: str, book_release: int, publisher: str, genre: str, author: str, price: float):
        self.__book_title = book_title
        self.__book_release = book_release
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    def __str__(self):
        return f"Название книги: '{self.__book_title}'\n" \
               f"Год выпуска книги: {self.__book_release}\n" \
               f"Издательство: {self.__publisher}\n" \
               f"Жанр: {self.__genre}\n" \
               f"Автор: {self.__author}\n" \
               f"Цена: {self.__price}р."


def execute_application():
    my_book = Book("Вниз по волшебной реке", 2019, "АСТ", "Приключения", "Успенский Э.Н.", 250)
    print(my_book)


if __name__ == '__main__':
    execute_application()
