1import json

LIBRARY = "resource/library.json"
AVAILABLE_BOOKS = "resource/available_books.txt"

def load_db(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_db(data):
    with open(LIBRARY, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def write_book(filename):
    books = load_db(filename)
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = input("Введите год выхода книги: ")
    available = input("Книга в наличии? (да/нет): ")
    match available.lower():
        case "да":
            available = True
        case "нет":
            available = False
        case _:
            quit("Вы ввели нет то значение, "
                 "нужно было вводить да, либо нет.")
    new_book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "year": year,
        "available": available,
    }

    books.append(new_book)
    save_db(books)

def view_all_books(filename):
    books = load_db(filename)
    print("-" * 20, "\nСписок всех книг")
    print("-" * 20)
    if not books:
        print("Библиотека пуста")
    else:
        for book in books:
            if book["available"]:
                status = "В наличии"
            else:
                status = "Отсутствует"
            print(f"ID {book['id']} | {book['title']} | {book['author']} | "
                  f"{book['year']} | {status}")
        print("-" * 20)

def find_book(filename):
    i = True
    books = load_db(filename)
    while i:
        choice = input("Способ по которому искать книгу:\n"
                       "1 - По автору\n"
                       "2 - По названию\n"
                       "3 - По ID\n"
                       "0 - Назад\n"
                       "Выбор: ")
        match choice:
            case "1":
                name = input("Введите автора: ")
                if not books:
                    print("Библиотека пуста")
                else:
                    for book in books:
                        if book["author"].lower() == name.lower():
                            print("-" * 20)
                            print("Найдено!")
                            print("-" * 20)
                            if book["available"]:
                                status = "В наличии"
                            else:
                                status = "Отсутствует"
                            print(f"ID {book['id']} | {book['title']} | "
                                  f"{book['author']} | "
                                  f"{book['year']} | {status}")
                            print("-" * 20)
                            return book

            case "2":
                name = input("Введите название: ")
                if not books:
                    print("Библиотека пуста")
                else:
                    for book in books:
                        if book["title"].lower() == name.lower():
                            print("-" * 20)
                            print("Найдено!")
                            print("-" * 20)
                            if book["available"]:
                                status = "В наличии"
                            else:
                                status = "Отсутствует"
                            print(f"ID {book['id']} | {book['title']} | "
                                  f"{book['author']} | "
                                  f"{book['year']} | {status}")
                            print("-" * 20)
                            return book
            case "3":
                try:
                    name = int(input("Введите ID: "))
                except ValueError:
                    quit("Нужно было вводить число!")
                if not books:
                    print("Библиотека пуста")
                else:
                    for book in books:
                        if int(book["id"]) == name:
                            print("-" * 20)
                            print("Найдено!")
                            print("-" * 20)
                            if book["available"]:
                                status = "В наличии"
                            else:
                                status = "Отсутствует"
                            print(f"ID {book['id']} | {book['title']} | "
                                  f"{book['author']} | "
                                  f"{book['year']} | {status}")
                            print("-" * 20)
                            return book
            case "0":
                i = False
            case _:
                quit("Нужно вводить число из списка!")

def change_status(filename):
    library = load_db(filename)
    print("Выберите книгу:")
    book = find_book(filename)
    choice_change = input("Выбор статуса:\n"
                   "1 - Взята\n"
                   "2 - Возвращена\n"
                   "Выбор: ")
    match choice_change:
        case "1":
            for lib in library:
                if lib["id"] == book["id"]:
                    lib["available"] = False
        case "2":
            for lib in library:
                if lib["id"] == book["id"]:
                    lib["available"] = True
        case _:
            quit("Нужно вводить число из списка!")
    save_db(library)

def delete_book_with_id(filename):
    books = load_db(filename)
    book_id = input("Введите id книги которую хотите удалить\n"
                    "Выбор: ")
    for i, book in enumerate(books):
        if int(book["id"]) == int(book_id):
            print("-" * 20)
            print("Найдено!")
            print("-" * 20)
            if book["available"]:
                status = "В наличии"
            else:
                status = "Отсутствует"
            print(f"ID {book['id']} | {book['title']} | "
                  f"{book['author']} | "
                  f"{book['year']} | {status}")
            print("-" * 20)

            choice = input("Удалить?\n"
                           "1 - Да\n"
                           "2 - Нет\n"
                           "Выбор: ")
            match choice:
                case "1":
                    books.pop(i)
                    for j in range(len(books)):
                        books[j]["id"] = j + 1
                    save_db(books)
                    break
                case "2":
                    main()
                case _:
                    quit("Нужно вводить число из списка!")

def export_books(filename, name_txt_file):
    books = load_db(filename)
    available_books = []

    for book in books:
        if book["available"]:
            available_books.append(book)
    with open(name_txt_file, "w", encoding="utf-8") as file:
        file.write(f"{'ID':<5} {'Название':<25} {'Автор':<18} {'Год':<6}\n")
        file.write("-" * 60 + "\n")

        for book in available_books:
            file.write(f"{book['id']:<5} {book['title']:<25} "
                    f"{book['author']:<18} {book['year']:<6}\n")

def main():
    i = True
    print("-" * 20, "\nСистема учёта книг в библиотеке\n", "-" * 20)
    while i:
        print("-" * 20)
        choice = input("Возможности программы:\n"
                       "1 - Просмотр всех книг.\n"
                       "2 - Поиск по автору/названию.\n"
                       "3 - Добавление новой книги.\n"
                       "4 - Изменение статуса доступности (взята/возвращена).\n"
                       "5 - Удаление книги по ID.\n"
                       "6 - Экспорт списка доступных книг в текстовый файл.\n"
                       "0 - Выход.\n"
                       "Выбор: ")
        match choice:
            case "1":
                view_all_books(LIBRARY)
            case "2":
                find_book(LIBRARY)
            case "3":
                write_book(LIBRARY)
            case "4":
                change_status(LIBRARY)
            case "5":
                delete_book_with_id(LIBRARY)
            case "6":
                export_books(LIBRARY, AVAILABLE_BOOKS)
            case "0":
                i = False
            case _:
                quit("Для выбора действия нужно выбирать цифру из списка!")

if __name__ == "__main__":
    main()