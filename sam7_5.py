with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print("Текст из файла:")
print(text)
print()

all_chars = len(text)
no_space_chars = len(text.replace(" ", ""))
words = text.split()
word_count = len(words)
sentences = text.count('.') + text.count('!') + text.count('?')
longest_word = max(words, key=len)

print("Результат анализа:")
print(f"Символов: {all_chars} (без пробелов: {no_space_chars})")
print(f"Слов: {word_count}")
print(f"Предложений: {sentences}")
print(f"Самое длинное слово: {longest_word}")