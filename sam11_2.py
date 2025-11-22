def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci = fib()
count = 0

with open("fib.txt", "w", encoding="utf-8") as file:
    for num in fibonacci:
        count += 1
        if count >= 200 and count <= 205:
            file.write(f"{num}\n")
        elif count > 205:
            break