# Задание 2.
# Реализуйте класс «Книга». Необходимо хранить в полях класса:
# название книги, год выпуска, издателя, жанр, автора, цену. Реализуйте
# конструктор по умолчанию и метод для вывода данных. Реализуйте доступ к
# отдельным полям класса через методы класса (геттеры и сеттеры).
# Реализуйте в классе «Книга» дополнительный метод класса и
# статический метод.
class Book:
    def __init__(self, book_title: str = " ", book_release: int = 0, publisher: str = " ", genre: str = " ",
                 author: str = " ", price: float = 0):
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
               f"Цена: {self.__price}р.\n"

    @staticmethod
    def read_data_books_in_file(path: str):
        """Считывает базу данных из файла"""
        try:
            with open(path, "r", encoding="utf-8") as file:
                data_books = file.read().strip().split('\n')
                print(f"Файл '{path}' успешно считан.\n")
                return data_books
        except FileNotFoundError:
            print(f"Не удалось открыть файл по указанному пути '{path}'")

    @classmethod
    def init_from_data_books(cls, data_books: list, name_book: str):
        """Создаёт объект класса Book по названию книги"""
        found = False
        for line in data_books:
            if line.lower().startswith(name_book.lower()):
                found = True
                line = line.split(", ")
                book_title = line[0]
                book_release = line[1]
                publisher = line[2]
                genre = line[3]
                author = line[4]
                price = line[5]
                return cls(book_title, int(book_release), publisher, genre, author, float(price))
        if found is False:
            print(f"Книги с названием '{name_book}' нет в базе данных.\n")

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
    path = "./data_books.txt"
    data_books = Book.read_data_books_in_file(path)

    data_book_1 = Book.init_from_data_books(data_books, "Властелин колец")
    if data_book_1:
        print(data_book_1)

    data_book_2 = Book.init_from_data_books(data_books, "Вниз по волшебной реке")
    if data_book_2:
        print(data_book_2)

    data_book_3 = Book.init_from_data_books(data_books, "Гарри Поттер")
    if data_book_3:
        print(data_book_3)

    book_4 = Book()
    if book_4:
        print(book_4)


if __name__ == '__main__':
    execute_application()
