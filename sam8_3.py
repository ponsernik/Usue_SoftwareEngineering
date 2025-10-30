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


class Laboratory(Auditorium):
    def __init__(self, number, group, count_s, equipment):
        super().__init__(number, group, count_s)
        self.equipment = equipment

    def conduct_experiment(self):
        print(f"В лаборатории {self.number} проводится эксперимент с {self.equipment}")


print("Обычная аудитория")
in_auditorium = Auditorium("101", "ИВТ-23-1", 20)
in_auditorium.test()
in_auditorium.use()

print("\nЛаборатория")
in_lab = Laboratory("205", "ПИЭ-23-1", 15, "электричеством")
in_lab.test()
in_lab.use()
in_lab.conduct_experiment()