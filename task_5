import json

library_file = "library.json"

initial_books = [
    {
        "id": 1,
        "title": "Мастер и Маргарита",
        "author": "Булгаков",
        "year": 1967,
        "available": True
    },
    {
        "id": 2,
        "title": "Преступление и наказание",
        "author": "Достоевский",
        "year": 1866,
        "available": False
    }
]

with open(library_file, 'w', encoding='utf-8') as file:
    json.dump(initial_books, file, ensure_ascii=False, indent=4)

with open(library_file, 'r', encoding='utf-8') as file:
    books = json.load(file)

print("Библиотека успешно загружена!\n")

while True:
    print("=== Система учёта книг ===")
    print("1. Просмотр всех книг")
    print("2. Поиск по автору или названию")
    print("3. Добавить новую книгу")
    print("4. Изменить статус доступности")
    print("5. Удалить книгу по ID")
    print("6. Экспорт доступных книг в TXT")
    print("7. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        if not books:
            print("Библиотека пуста")
        else:
            for book in books:
                status = "Доступна" if book["available"] else "Взята"
                print(f"{book['id']}. {book['title']} — {book['author']} ({book['year']}) [{status}]")

    elif choice == "2":
        keyword = input("Введите автора или часть названия: ").lower()
        found = False
        for book in books:
            if keyword in book["title"].lower() or keyword in book["author"].lower():
                status = "Доступна" if book["available"] else "Взята"
                print(f"{book['id']}. {book['title']} — {book['author']} ({book['year']}) [{status}]")
                found = True
        if not found:
            print("Нет такого...")

    elif choice == "3":
        title = input("Название: ")
        author = input("Автор: ")
        year = int(input("Год издания: "))
        new_id = max([b["id"] for b in books] or [0]) + 1
        books.append({
            "id": new_id,
            "title": title,
            "author": author,
            "year": year,
            "available": True
        })
        with open(library_file, 'w', encoding='utf-8') as file:
            json.dump(books, file, ensure_ascii=False, indent=4)
        print(f"Книга добавлена (ID {new_id})")

    elif choice == "4":
        book_id = int(input("ID книги: "))
        for book in books:
            if book["id"] == book_id:
                book["available"] = not book["available"]
                status = "Доступна" if book["available"] else "Взята"
                print(f"Статус изменён: теперь {status}")
                with open(library_file, 'w', encoding='utf-8') as file:
                    json.dump(books, file, ensure_ascii=False, indent=4)
                break
        else:
            print("Нет такой книги...")

    elif choice == "5":
        book_id = int(input("ID книги для удаления: "))
        new_books = [b for b in books if b["id"] != book_id]
        if len(new_books) != len(books):
            books = new_books
            with open(library_file, 'w', encoding='utf-8') as file:
                json.dump(books, file, ensure_ascii=False, indent=4)
            print("Книга удалена")
        else:
            print("Нет такой книги...")

    elif choice == "6":
        with open('available_books.txt', 'w', encoding='utf-8') as file:
            for book in books:
                if book["available"]:
                    file.write(f"{book['id']}. {book['title']} — {book['author']} ({book['year']})\n")
        print("Список доступных книг экспортирован в available_books.txt")

    elif choice == "7":
        print("Пака")
        break

    else:
        print("Что-то не так...")
