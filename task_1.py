with open('resource/text.txt', 'w', encoding='utf-8') as f:
    f.write("Привет\n")
    f.write("Как дела?\n")
    f.write("Что делаешь?\n")
    f.write("Чем занимаешься?\n")
    f.write("Сколько лет?\n")

with open('resource/text.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

count_lines = len(lines)
print(f"Количество строк: {count_lines}")

count_words = 0
for line in lines:
    words = line.split()
    count_words += len(words)
print(f"Количество слов: {count_words}")

long_string = ""
for line in lines:
    if len(line) > len(long_string):
        long_string = line
print(f"Самая длинная строка: {long_string}")