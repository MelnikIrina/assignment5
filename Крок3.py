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
    student['середня оцінка'] = round(average, 2)

for student in all_students:
    print(f"{student['Прізвище']} {student['Ім'я']}: середня оцінка - {student['середня оцінка']}")
