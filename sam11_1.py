def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci = fib()
count = 0

for num in fibonacci:
    count += 1
    if count >= 200 and count <= 205:
        print(f"Число Фибоначчи {count}: {num}")
    elif count > 205:
        break