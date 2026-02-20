import csv

FILENAME = "resource/products.csv"
product_dict = {}

def read_csv(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            product_dict[row["Название"]] = {
                "Цена": row["Цена"],
                "Количество": row["Количество"]
            }
        return product_dict

def write_csv(filename):
    with open(filename, "a", encoding="utf-8", newline='') as file:
        print("Введите через запятую значения которые "
                "хотите добавить в таблицу, в формате:\n"
                "Название Цена Количество\n"
                "Пример: Кружка 67 42")

        writer = csv.writer(file)

        while True:
            print("-" * 20 + "\nЧтобы выйти, введите 0.")
            new_data = input("Ввод: ")
            if new_data == "0":
                main(FILENAME)
            try:
                name, price, count = new_data.split(" ")
                writer.writerow([name, float(price), int(count)])
                print(f"Товар '{name}' добавлен!")
            except ValueError:
                print("Ошибка: введите 3 значения через пробел, в формате:"
                      "Название Цена Количество")

def find_product(products, name):
    for key, value in products.items():
        if key.lower() == name.lower():
            return print(f"Найдено!\n"
                         f"--------------------\n"
                         f"Название: {key}\n"
                         f"Цена: {value["Цена"]}\n"
                         f"Количество: {value["Количество"]}")
    return print(f'Товар "{name}" не найден.')

def calculating_total_price(products):
    result = 0
    for key, value in products.items():
        price = float(value["Цена"])
        quantity = int(value["Количество"])
        result += price * quantity
    return result

def main(filename):
    print("-" * 20 + "\nМеню\n" + "-" * 20)
    choice = input("1 - Добавить новые товары.\n"
                   "2 - Поиск товара по названию.\n"
                   "3 - Расчёт общей стоимости всех товаров на складе.\n"
                   "0 - Выйти\n"
                   "--------------------\n"
                   "Выбор: ")
    match choice:
        case "1":
            write_csv(filename)
            input("Нажмите Enter чтобы продолжить...")
            main(FILENAME)
        case "2":
            name = input("Введите название.\n"
                         "Ввод: ")
            print("-" * 20)
            find_product(read_csv(filename), name)
            input("Нажмите Enter чтобы продолжить...")
            main(FILENAME)
        case "3":
            print(f"Общая стоимость всех товаров на складе:\n"
                  f"{calculating_total_price(read_csv(filename))}")
            input("Нажмите Enter чтобы продолжить...")
            main(FILENAME)
        case "0":
            quit()

if __name__ == "__main__":
    main(FILENAME)
