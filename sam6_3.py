def dictionary(digits):
    counter = {}
    for char in digits:
        num = int(char)
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    sorted_items = []
    for num, count in counter.items():
        sorted_items.append((count, num))
    sorted_items.sort(reverse=True)

    top_numbers = []
    for i in range(min(3, len(sorted_items))):
        count, num = sorted_items[i]
        top_numbers.append(num)
    top_numbers.sort()
    result = {}
    for num in top_numbers:
        result[num] = counter[num]
    return result
digits = "1111111122233344455555566778889999999000"
print(dictionary(digits))