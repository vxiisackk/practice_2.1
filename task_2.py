with open('students.txt', 'w', encoding='utf-8') as file:
    file.write("Иванов Иван:5,4,3,5\n")
    file.write("Петров Петр:4,3,4,4\n")
    file.write("Сидорова Мария:5,5,5,5\n")

with open('students.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

good_students = []
max_mid = -1
best_student = " "
best_grade = 0

for row in lines:
    row = row.strip()
    if not row:
        continue
    name, grades_mid = row.split(':')
    grades = [int(v) for v in grades_mid.split(',')]
    mid = sum(grades) / len(grades)
    if mid > 4.0:
        good_students.append(row)
    if mid > max_mid:
        max_mid = mid
        best_student = name
        best_grade = mid

with open('result.txt', 'w', encoding='utf-8') as file:
    for mid in good_students:
        file.write(mid + '\n')

print("Файл result.txt создан, yeppie!\n")
print(f"Студент с наивысшим средним баллом: {best_student} ({best_grade:.1f})")
