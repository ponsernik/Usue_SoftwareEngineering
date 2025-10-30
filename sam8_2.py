class Auditorium:
    def __init__(self, number, group, count_s):
        self.group = group
        self.count_s = count_s
        self.number = number
        self.busy = False


    def test(self):
        print(f"В аудитории {self.number} находится группа {self.group} в составе {self.count_s} человек")

    def use(self):
        self.busy = True
        print(f"Аудитория {self.number} занята")

in_auditorium = Auditorium("TALK","ИВТ-23-2", "25")
in_auditorium.test()
in_auditorium.use()