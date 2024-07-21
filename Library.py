import json

from Book import Book


def view_books(books):
    """
    Вывод стиска книг books
    :param books: []
    :return: Nane
    """
    headers = ["ID", "Title", "Author", "Year", "Status"]
    table = []
    for book in books:
        table_book = [book["id"], book["title"], book["author"], book["year"]]
        if book["status"] == 1:
            table_book.append("в наличии")
        else:
            table_book.append("выдана")
        table.append(table_book)

    col_widths = [max(len(str(row[i])) for row in ([headers] + table)) for i in range(len(headers))]
    row_format = " | ".join("{:<" + str(width) + "}" for width in col_widths)
    print(row_format.format(*headers))
    print("-+-".join('-' * width for width in col_widths))

    for row in table:
        print(row_format.format(*row))


class Library:
    """
        filename (название файла для хранения данных)
        books ([], список экзепляров класса Book)
        next_id (int, Следюущий id для новой записи)
    """
    def __init__(self, filename="data/books.json"):
        self.filename = filename
        self.books = self.get_all_books()
        self.next_id = self.get_last_id()
        self.json_dump()

    def get_last_id(self):
        elem = self.books[-1]
        return int(elem['id']) + 1

    def get_next_id(self):
        return int(self.next_id) + 1

    def get_all_books(self):
        """
        Получает данные из json файла и форминует [] книг
        :return: [] - список всех книг
        """
        books = []
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
            for item in data:
                book = Book(
                    id=item.get('id'),
                    title=item.get('title'),
                    author=item.get('author'),
                    year=item.get('year'),
                    status=item.get('status')
                )
                books.append(book.to_dict())
        except Exception as e:
            print(f"ERROR: Произошла ошибка: {e}")
        return books

    def commit_to_json(self, books):
        """
        Сохраняет список в json формате и записывает в файл
        :param books: []
        :return: Nane
        """
        with open(self.filename, 'w', encoding='utf-8') as json_file:
            json.dump(books, json_file, ensure_ascii=False, indent=4)

    def add_book(self, book):
        """
        Добавление книги к списку библиотеки и запись списка в файл
        :param book: Book
        :return: Nane
        """
        book.id = self.next_id
        self.next_id = self.get_next_id()
        self.books.append(book.to_dict())
        try:
            self.commit_to_json(self.books)
            self.json_dump()
            print("Книга добавлена!")
        except Exception as e:
            print(f"ERROR: Произошла ошибка: {e}")
            self._swap_files()

    def delete_book(self, del_id):
        """
        удаление книги из списка библиотеки и запись списка в файл
        :param del_id: int
        :return: None
        """
        books_exc = [book for book in self.books if book['id'] != del_id]
        if len(books_exc) == len(self.books):
            print("Книга не найдена")
            return
        try:
            self.commit_to_json(books_exc)
            self.json_dump()
            print("Книга удалена!")
        except Exception as e:
            print(f"ERROR: Произошла ошибка: {e}")
            self._swap_files()

    def search_book(self, search_word):
        """
        Поиск книги по списку библиотке и подходящих книг
        :param search_word: string
        :return: Nane
        """
        search_books = [
            book for book in self.books
            if book['title'] == search_word or
               book['author'] == search_word or
               book['year'] == search_word
        ]
        view_books(search_books)

    def view_all_books(self):
        view_books(self.books)

    def change_status(self, id, status):
        """
        изменяет поле ['status'] в элементах списка подходящих по id
        :param id: int
        :param status: int
        :return: Nane
        """
        for book in self.books:
            if book['id'] == int(id):
                book['status'] = status
        try:
            self.commit_to_json(self.books)
            self.json_dump()
            print("Статус изменен!")
        except Exception as e:
            print(f"ERROR: Произошла ошибка: {e}")
            self._swap_files()

    def json_dump(self):
        """
        создание резервной копии json файла
        :return: Nane
        """
        try:
            with open(self.filename, 'r', encoding='utf-8') as source_file:
                data = source_file.read()
            with open("data/dump_library.json", 'w', encoding='utf-8') as destination_file:
                destination_file.write(data)
        except Exception as e:
            print(f"ERROR: Произошла ошибка: {e}")

    def _swap_files(self):
        """
        Заменя файла с данными, резервной копии
        :return: Nane
        """
        try:
            with open("data/dump_library.json", 'r', encoding='utf-8') as source_file:
                data = source_file.read()
            with open(self.filename, 'w', encoding='utf-8') as destination_file:
                destination_file.write(data)
        except Exception as e:
            print(f"ERROR: Произошла ошибка: {e}")
