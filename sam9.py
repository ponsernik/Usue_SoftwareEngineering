# Класс для представления помидора
class Tomato:
    # Все возможные стадии созревания помидора
    states = ["отсутствует", "цветение", "зеленый", "красный"]

    def __init__(self, index):
        # Индекс помидора на кусте (нумеруем с 0)
        self._index = index
        # Начальная стадия созревания - первая из списка
        self._state = self.states[0]

    def grow(self):
        # Переводим помидор на следующую стадию, если он еще не созрел
        if self._state != self.states[-1]:
            # Находим текущую стадию в списке и берем следующую
            self._state = self.states[self.states.index(self._state) + 1]

    def is_ripe(self):
        # Проверяем, созрел ли помидор (достиг последней стадии)
        return self._state == self.states[-1]


# Класс для представления куста с помидорами
class TomatoBush:
    def __init__(self, num):
        # Создаем список помидоров на кусте
        # num - количество помидоров на кусте
        self.tomatoes = [Tomato(i) for i in range(num)]

    def grow_all(self):
        # Растим все помидоры на кусте
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        # Проверяем, все ли помидоры на кусте созрели
        # all() возвращает True только если все элементы True
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        # Собираем урожай - очищаем список помидоров
        self.tomatoes.clear()


# Класс для представления садовника
class Gardener:
    def __init__(self, name, plant):
        # Имя садовника
        self.name = name
        # Растение, за которым ухаживает садовник
        self._plant = plant

    def work(self):
        # Садовник работает - ухаживает за растением
        print(f"Садовник {self.name} работает")
        self._plant.grow_all()

    def harvest(self):
        # Сбор урожая
        if self._plant.all_are_ripe():
            # Если все помидоры созрели - собираем их
            self._plant.give_away_all()
            print(f"Садовник {self.name} собирает урожай")
        else:
            # Если не все созрели - выводим сообщение
            print(f"Садовник {self.name} не собрал урожай. Томаты не созрели")

    @staticmethod
    def knowledge_base():
        # Статический метод - выводит справочную информацию
        print("Cправка по садоводству:")
        print("1. Помидоры проходят 4 стадии созревания:")
        print("- отсутствует")
        print("- цветение")
        print("- зеленый")
        print("- красный")
        print("2. Садовник должен ухаживать за кустом, чтобы помидоры росли")
        print("3. Урожай можно собрать только когда все помидоры красные\n")


# Тестирование программы
if __name__ == "__main__":
    # Выводим справку по садоводству
    Gardener.knowledge_base()

    # Создаем куст с 3 помидорами
    bush = TomatoBush(3)
    # Создаем садовника с именем Иван для ухода за кустом
    gardener = Gardener("Иван", bush)

    # Последовательность действий:
    # 1. Садовник ухаживает за кустом первый раз
    gardener.work()
    # 2. Пытается собрать урожай (еще рано)
    gardener.harvest()
    # 3. Продолжает ухаживать
    gardener.work()
    # 4. Еще раз ухаживает
    gardener.work()
    # 5. Собирает урожай (теперь все помидоры созрели)
    gardener.harvest()