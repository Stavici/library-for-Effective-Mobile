from Book import Book
from Library import Library


def current_year():
    """
    Проверка кореектности введенного года
    :return: string
    """
    while True:
        try:
            year = input("Ведите год издания книги: ")
            if 0 <= int(year) <= 2024:
                return year
            else:
                print(f"Пожалуйста, введите год в диапазоне от 0 до 2024.")
        except ValueError:
            print("Пожалуйста, введите допустимое число.")


def current_id(library):
    """
    Проверка корректности ввода id
    :param library: Library
    :return: string
    """
    while True:
        try:
            id = input("Введите id книги: ")
            if 0 <= int(id) < library.get_last_id():
                return id
            else:
                print(f"Пожалуйста, введите правильный id.")
        except ValueError:
            print("Пожалуйста, введите допустимое число.")


def current_status():
    """
    Проверка выбора статуса и преобразования его в цифровой вид
    :return: int - выбранный статус книги (1 или 2)
    """
    while True:
        try:
            print("Выберете статус книги: ")
            print("1. В наличии")
            print("2. Выдана")
            status = int(input())
            if status == 1 or status == 2:
                return status
            else:
                print("Введите корректные данные")
        except ValueError:
            print("Введите корректные данные")


def add_book(library):
    """
    Добавление книги в библиотеку
    :param library: Library
    :return: None
    """
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = current_year()
    book = Book('', title, author, year, 1)
    library.add_book(book)


def del_book(library):
    """
    Удаление книги из библиотеки
    :param library: Library
    :return: None
    """
    del_id = current_id(library)
    library.delete_book(int(del_id))


def search_book(library):
    """
    Поиск книги в библиотеки
    :param library: Library
    :return: None
    """
    search_word = input("Для поиска введи название, автор или год: ")
    library.search_book(search_word)


def get_all(library):
    """
    Вывод всех книг
    :param library: Library
    :return: None
    """
    library.view_all_books()


def change_status(library):
    """
    Изменение статуса выбранной книги
    :param library: Library
    :return: None
    """
    book_id = current_id(library)
    status = current_status()
    library.change_status(book_id, status)


def book_menu():
    """
     Отображает меню библиотеки и обрабатывает выбор пользователя.
    :return: None
    """
    library = Library()

    choices = {
        '1': add_book,
        '2': del_book,
        '3': search_book,
        '4': get_all,
        '5': change_status,
        '6': lambda _: print("Выход...") or exit()
    }

    menu = {
        'Меню:': "",
        '1': "Добавить книгу",
        '2': "Удалить книгу",
        '3': "Поиск",
        '4': "Вывести все книги",
        '5': "Изменить статус книги",
        '6': "Выход"
    }

    while True:
        for key, value in menu.items():
            print(f"{key}. {value}")
        choice = input("Выберите пункт меню: ")
        if choice in choices:
            choices[choice](library)
            if choice != '3':
                input("Нажмите Enter для возврата в меню...")
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == '__main__':
    book_menu()

