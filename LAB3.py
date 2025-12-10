students = {}
while True:
    name = input("Введіть ім'я студента (або stop): ")
    if name.lower() == "stop":
        break
    grade = int(input("Введіть оцінку: "))
    students[name] = grade
print("Результати:")
for name, grade in students.items():
    print(name, grade)
if students:
    avg = sum(students.values()) / len(students) #len повертє кількіст елементів у списку
    print("Середній бал: ", avg)
    excellent = [name for name, grade in students.items() if 10 <= grade <= 12]
    good = [name for name, grade in students.items() if 7 <= grade <= 9]
    weak = [name for name, grade in students.items() if 4 <= grade <= 6]
    failed = [name for name, grade in students.items() if 1 <= grade <= 3]
    print("Відмінники: ", {len(excellent)}, excellent)
    print("Хорошисти: ", {len(good)}, good)
    print("Відстаючі: ", {len(weak)}, weak)
    print("Не здали: ", {len(failed)}, failed)
else: #в інших випадках

    print("Немає даних.")

