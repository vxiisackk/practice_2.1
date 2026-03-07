from datetime import datetime

log_file = "calculator.log"

print("Последние 5 операций:")
try:
    with open(log_file, 'r', encoding='utf-8') as file:
        logs = file.readlines()
        for line in logs[-5:]:
            print(line.strip())
except FileNotFoundError:
    print("Лог-файл ещё не создан.")

print("Калькулятор с логированием запущен!\n")

while True:
    print("1. Выполнить вычисление")
    print("2. Очистить лог-файл")
    print("3. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        num1 = float(input("Первое число: "))
        op = input("Операция (+, -, *, /): ").strip()
        num2 = float(input("Второе число: "))

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("ты чудишь, делить на ноль нельзя...")
                continue
            result = num1 / num2
        else:
            print("Нет такой операции...")
            continue

        print(f"Результат: {result}")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {num1} {op} {num2} = {result}"

        with open(log_file, 'a', encoding='utf-8') as file:
            file.write(log_entry + "\n")

    elif choice == "2":
        with open(log_file, 'w', encoding='utf-8') as file:
            pass
        print("Лог-файл очищен!")

    elif choice == "3":
        print("Пака")
        break

    else:
        print("Что-то не так...")
