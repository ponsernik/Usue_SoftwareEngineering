with open('input.txt', 'r') as f:
    content = f.read()

letters = 0
for char in content:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        letters += 1

words = len(content.split())
lines = len(content.splitlines())

print("Input file contains:")
print(f"  {letters} letters")
print(f"  {words} words")
print(f"  {lines} lines")