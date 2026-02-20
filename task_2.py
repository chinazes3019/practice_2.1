with open('resource/students.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

students = []
best_average_score = 0

for line in lines:
    colon = line.split(':')
    name = colon[0]
    grades = colon[1].split(',')

    count = 0
    for grade in grades:
        count += int(grade)
    average_score = count / len(grades)
    if average_score > 4.0:
        students.append(f"{name}: {average_score}")

    if average_score > best_average_score:
        best_average_score = average_score
        best_student = name

with open('resource/result.txt', 'w', encoding='utf-8') as f:
    for student in students:
        f.write(f"{student}\n")

print(f"Студент с наивысшим средним баллом: {best_student}, Балл: {best_average_score}")