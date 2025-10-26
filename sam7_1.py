import re
from collections import Counter

with open('python_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = re.findall(r'\b[а-яёa-z]+\b', text.lower())

total_words = len(words)
word_counts = Counter(words)
most_common_word, most_common_count = word_counts.most_common(1)[0]

print(f"Общее количество слов: {total_words}")
print(f"Самое частое слово: '{most_common_word}' ({most_common_count} раз)")
print("\nТоп-10 слов:")
for word, count in word_counts.most_common(10):
    print(f"'{word}': {count}")