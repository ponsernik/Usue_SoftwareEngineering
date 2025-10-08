visits = [8734, 2345, 8201, 6621, 9999, 1234,
          5678, 8201, 8888, 4321, 3365, 1478,
          9865, 5555, 7777, 9998, 1111, 2222,
          3333, 4444, 5556, 6666, 5410, 7778,
          8889, 4445, 1439, 9604, 8201, 3365,
          7502, 3016, 4928, 5837, 8201, 2643,
          5017, 9682, 8530, 3250, 7193, 9051,
          4506, 1987, 3365, 5410, 7168, 7777,
          9865, 5678, 8201, 4445, 3016, 4506, 4506]

print("Было выдано чеков:", len(visits))

unique_visits = []
for code in visits:
    if code not in unique_visits:
        unique_visits.append(code)
print("Количество людей, посетивших ресторан:", len(unique_visits))

counter = {}
for code in visits:
    if code in counter:
        counter[code] += 1
    else:
        counter[code] = 1

max_visits = 0
frequent_visitor = None
for code, count in counter.items():
    if count > max_visits:
        max_visits = count
        frequent_visitor = code

print(f"Работник {frequent_visitor} посетил ресторан {max_visits} раз")