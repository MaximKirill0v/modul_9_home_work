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

    def __str__(self):
        return f"Название книги: '{self.book_title}'\n" \
               f"Год выпуска книги: {self.book_release}\n" \
               f"Издательство: {self.publisher}\n" \
               f"Жанр: {self.genre}\n" \
               f"Автор: {self.author}\n" \
               f"Цена: {self.price}р."


def execute_application():
    book_1 = Book("Вниз по волшебной реке", "2019", "АСТ", "Приключения", "Успенский Э.Н.", "250")
    print(book_1)


if __name__ == '__main__':
    execute_application()
