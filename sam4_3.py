import datetime
import time

def display_current_time():
    for i in range(5):
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%H:%M:%S")
        print(f"Текущее время: {formatted_time}")
        time.sleep(1)

if __name__ == '__main__':
    print("Запуск вывода времени на протяжении 5 секунд...")
    display_current_time()
    print("Программа завершена.")