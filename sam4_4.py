def average(*numbers):
    if not numbers:
        return "Ошибка: не передано ни одного числа"

    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    test_cases = [
        [10, 20, 30],
        [5, 15],
        [100],
        [1.1, 2.2, 3.3, 4.4],
        []
    ]

    for i, numbers in enumerate(test_cases, 1):
        print(f"Тест {i}: {numbers}")
        result = average(*numbers)
        print(f"Результат: {result}\n")