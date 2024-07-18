from library import Library


def main():
    library = Library()

    while True:
        print("\nСистема управления библиотекой")
        print("1. Добавить книгу")
        print("2. Список книг")
        print("3. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания книги: "))
            library.add_book(title, author, year)
        elif choice == "2":
            library.list_books()
        elif choice == "3":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()