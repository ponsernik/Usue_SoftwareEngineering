expenses = []

print("УЧЕТ РАСХОДОВ")

while True:
    print("\n1 - Добавить расход")
    print("2 - Показать все расходы")
    print("3 - Выйти")

    choice = input("Выберите: ")

    if choice == "1":
        what = input("На что потратили? ")
        how_much = input("Сколько рублей? ")

        expense = f"{what} - {how_much} руб."
        expenses.append(expense)

        with open("my_expenses.txt", "w", encoding="utf-8") as f:
            for item in expenses:
                f.write(item + "\n")

        print("Расход добавлен!")

    elif choice == "2":
        print("\nМОИ РАСХОДЫ")
        if len(expenses) == 0:
            print("Пока нет расходов")
        else:
            total = 0
            for i, expense in enumerate(expenses, 1):
                print(f"{i}. {expense}")
                if "руб." in expense:
                    try:
                        amount = float(expense.split(" - ")[1].replace(" руб.", ""))
                        total += amount
                    except:
                        pass
            print(f"\nВсего потрачено: {total} руб.")

    elif choice == "3":
        print("Пока!")
        break

    else:
        print("Не понял, выберите 1, 2 или 3")