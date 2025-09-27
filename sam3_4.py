word = input('Введите предложение: ')
arr = ['a', 'e', 'i', 'o', 'u']
bad_word = "ugly"
len_word = len(word) - 3

# длина предложения
print("Длина предложения: ", len(word))

# нижний регистр
lower_word = word.lower()
print("Предложение в нижнем регистре: ", lower_word)

# подсчет гласных
count = 0
for i in lower_word:
    if i in arr:
        count += 1
print(count)

# замена слова
print("Замена слова: ", lower_word.replace('ugly', 'beauty'))

# проверка начала и конца
if (word[:3] == "The") and (word[len_word:] == "end"):
    print("Да, предложение начинается с The и заканчивается на end")
else:
    print("Нет, предложение не прошло проверку")