def read_file_safe(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()

            if not content:
                raise ValueError("файл пустой")
            else:
                print(f"Содержимое файла: {content}")

    except FileNotFoundError:
        print(f"Файл {filename} не найден")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == '__main__':
    with open('empty_file.txt', 'w', encoding='utf-8') as f:
        pass

    with open('data_file.txt', 'w', encoding='utf-8') as f:
        f.write("Тестовые данные для проверки")

    print("Тест с пустым файлом:")
    read_file_safe('empty_file.txt')

    print("\nТест с файлом, содержащим данные:")
    read_file_safe('data_file.txt')