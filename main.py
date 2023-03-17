# Задание 2.
# Реализуйте класс «Книга». Необходимо хранить в полях класса:
# название книги, год выпуска, издателя, жанр, автора, цену. Реализуйте
# конструктор по умолчанию и метод для вывода данных.
class Book:
    book_title: str
    book_release: str
    publisher: str
    genre: str
    author: str
    price: str

    def __init__(self, book_title: str, book_release: str, publisher: str, genre: str, author: str, price: str):
        self.book_title = book_title
        self.book_release = book_release
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price


def execute_application():
    book_1 = Book("Вниз по волшебной реке", "2019", "АСТ", "Приключения", "Успенский Э.Н.", "250")


if __name__ == '__main__':
    execute_application()
