with open('text.txt', 'w', encoding='utf-8') as file:
    file.write("первая строка респект умом\n")
    file.write("строка и тут слов больше уму не постижимо ого!\n")
    file.write("мало.\n")
    file.write("а вы знали, что смешав бензин с апельсиновым соком, можно изготовить напалм?\n")
    file.write("тут еще и пятая строка есть ... \n")

print("Файл text.txt создан. yeppie! \n")

with open('text.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

nor = len(lines)
print(f"1. Количество строк в файле: {nor}")

nWord = 0
for row in lines:
    wir = row.split()
    nWord += len(wir)

print(f"2. Количество слов в файле: {nWord}")

muchLong = max(lines, key=len). strip()
print(f"3. Самая длинная строка:\n {muchLong}")
