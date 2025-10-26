import re

with open('input.txt', 'r') as f:
    bad_words = f.read().split()

text = input("Введите текст: ")

for word in bad_words:
    pattern = re.compile(re.escape(word), re.IGNORECASE)
    text = pattern.sub('*' * len(word), text)

print("Результат:")
print(text)