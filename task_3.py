with open('products.csv', 'w', encoding='utf-8') as file:
    file.write("Яблоки,100,50\n")
    file.write("Бананы,80,30\n")
    file.write("Молоко,120,20\n")
    file.write("Хлеб,40,100\n")

print("Файл products.csv создан\n")

products = []

with open('products.csv', 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip():
            name, price, quantity = line.strip().split(',')
            products.append([name, int(price), int(quantity)])

while True:
    print("\nМеню")
    print("1. Добавить новый товар")
    print("2. Поиск товара по названию")
    print("3. Рассчитать общую стоимость всех товаров")
    print("4. Сохранить данные и выйти")

    choice = input("Выбери действие (1-4): ")

    if choice == "1":
        name = input("Название товара: ")
        price = int(input("Цена: "))
        quantity = int(input("Количество: "))
        products.append([name, price, quantity])
        print("Товар добавлен)")

    elif choice == "2":
        search = input("Введи название товара: ").lower()
        found = False
        for product in products:
            if product[0].lower() == search:
                print(f"Найдено {product[0]} | Цена: {product[1]} | Количество: {product[2]}")
                found = True
        if not found:
            print("Товар не найден...")

    elif choice == "3":
        total = 0
        for product in products:
            total += product[1] * product[2]
        print(f"Общая стоимость товаров на складе: {total} руб.")

    elif choice == "4":
        with open('products.csv', 'w', encoding='utf-8') as file:
            for product in products:
                file.write(f"{product[0]},{product[1]},{product[2]}\n")
        print("Данные сохранены в products.csv")
        break

    else:
        print("Что-то не так... Попробуй заново")
