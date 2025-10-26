import csv

all_students = []

with open('dataset.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        all_students.append(row)

print("Усього студентів:", len(all_students))
print("Перший запис:", all_students[0])
