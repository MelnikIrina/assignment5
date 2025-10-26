import csv

all_students = []
with open('dataset.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        all_students.append(row)

for student in all_students:
    program = float(student['Основи програмування'])
    algebra = float(student['Лінійна алгебра'])
    geometry = float(student['Проекційна геометрія'])
    analysis = float(student['Математичний аналіз'])

    average = (program + algebra + geometry + analysis) / 4
    student['Середня оцінка'] = round(average, 2)

target_group = input("Ведіть назву ОДНІЄЇ групи для експорту (наприклад, MI-11): ")

group_students = [student for student in all_students if student['Група'] == target_group]

if group_students:
    fieldnames = [
        'Id', 'Прізвище', "Ім'я", 'Група',
        'Основи програмування', 'Лінійна алгебра',
        'Проекційна геометрія', 'Математичний аналіз',
        'Середня оцінка'
    ]

    filename = f"{target_group}.csv"

    with open(filename, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(group_students)

    print(f"Створено файл: {filename}")
else:
    print(f"Групу '{target_group}' не знайдено")
