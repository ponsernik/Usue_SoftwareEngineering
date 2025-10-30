class Auditorium:
    def __init__(self, group, count_s):
        self.group = group
        self.count_s = count_s

    def test(self):
        print(f"В аудитории находится группа {self.group} в составе {self.count_s} человек")

in_auditorium = Auditorium("ИВТ-23-2", "25")
in_auditorium.test()