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

    @property
    def book_title(self):
        return self.__book_title

    @book_title.setter
    def book_title(self, book_title: str):
        self.__book_title = book_title

    @property
    def book_release(self):
        return self.__book_release

    @book_release.setter
    def book_release(self, book_release: int):
        self.__book_release = book_release

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre: str):
        self.__genre = genre

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


def execute_application():
    my_book = Book("Вниз по волшебной реке", 2019, "АСТ", "Приключения", "Успенский Э.Н.", 250)
    print(my_book)
    print(my_book.book_title)
    print(my_book.book_release)
    print(my_book.publisher)
    print(my_book.genre)
    print(my_book.author)
    print(my_book.price)


if __name__ == '__main__':
    execute_application()
