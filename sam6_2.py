def remover(tuple_data, element):
    temp_list = list(tuple_data)

    if element in temp_list:
        temp_list.remove(element)

    return tuple(temp_list)

print(remover((1, 2, 3), 1))
print(remover((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remover((2, 4, 6, 6, 4, 2), 9))