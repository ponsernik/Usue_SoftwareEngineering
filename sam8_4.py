class Auditorium:
    def __init__(self, number, group, count_s):
        self.group = group
        self._count_s = count_s
        self.__number = number
        self.___busy = False


    def test(self):
        print(f"В аудитории {self.__number} находится группа {self.group} в составе {self._count_s} человек")

    def use(self):
        self.___busy = True
        print(f"Аудитория {self.__number} занята")

in_auditorium = Auditorium(201,"ИВТ-23-2", "25")
print(in_auditorium._count_s)
in_auditorium.test()