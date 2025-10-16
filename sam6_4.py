def get_slice(tuple_data, element):
    if element not in tuple_data:
        return ()
    first_index = tuple_data.index(element)
    try:
        second_index = tuple_data.index(element, first_index + 1)
    except ValueError:
        return tuple_data[first_index:]

    return tuple_data[first_index:second_index + 1]
print(get_slice((1, 2, 3), 8))
print(get_slice((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(get_slice((1, 2, 8, 5, 1, 2, 9), 8))