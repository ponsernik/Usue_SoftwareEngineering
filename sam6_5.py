def find_car_period(parking_log, car_number):
    if car_number not in parking_log:
        return ()
    first_entry = -1
    for i in range(len(parking_log)):
        if parking_log[i] == car_number:
            first_entry = i
            break
    second_entry = -1
    for i in range(first_entry + 1, len(parking_log)):
        if parking_log[i] == car_number:
            second_entry = i
            break
    if second_entry == -1:
        result = []
        for i in range(first_entry, len(parking_log)):
            result.append(parking_log[i])
        return tuple(result)
    else:
        result = []
        for i in range(first_entry, second_entry + 1):
            result.append(parking_log[i])
        return tuple(result)

print(find_car_period((123, 456, 789, 123, 999, 888), 123))  # (123, 456, 789, 123)
print(find_car_period((111, 222, 333, 444), 555))  # ()
print(find_car_period((777, 888, 999, 777, 111, 222), 777))  # (777, 888, 999, 777)
print(find_car_period((101, 202, 303, 404), 101))  # (101, 202, 303, 404)