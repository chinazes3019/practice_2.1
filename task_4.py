from datetime import datetime

try:
    first_number = int(input("Введите первое число: "))
    operand = input("Введите операнд (+, -, *, /): ")
    second_number = int(input("Введите второе число: "))
except ValueError:
    quit("Вы ввели неверные данные")

if operand == "+":
    result = first_number + second_number
    log = f"{first_number} + {second_number} = {result}"
    print(log)
elif operand == "-":
    result = first_number - second_number
    log = f"{first_number} - {second_number} = {result}"
    print(log)
elif operand == "*":
    result = first_number * second_number
    log = f"{first_number} * {second_number} = {result}"
    print(log)
elif operand == "/":
    if second_number != 0:
        result = first_number / second_number
        log = f"{first_number} / {second_number} = {result}"
        print(log)
    else:
        result = "infinity"
        log = f"{first_number} / {second_number} = {result}"
        print(log)
else:
    print("Введён неправильный оператор")

time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
if operand == '+' or operand == '-' or operand == '*' or operand == '/':
    with open('resource/calculator.log', 'a+', encoding='utf-8') as f:
        f.write(f"[{time}] {log}\n")
        f.seek(0)
        lines = f.readlines()
        if lines:
            print("\nПоследние 5 операций:")
            for line in lines[-5:]:
                print(line, end='')
        else:
            print("Логи пусты.")

clear = input("\nОчистить логи? (да/нет): ")
if clear == 'да':
    with open('resource/calculator.log', 'w', encoding='utf-8') as f:
        f.write('')
    print("Логи очищены")
