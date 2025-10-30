class Auditorium:
    def status(self):
        pass

class LectureAuditorium(Auditorium):
    def status(self):
        print("Лекционная аудитория: свободна для занятия")

class ComputerAuditorium(Auditorium):
    def status(self):
        print("Компьютерный класс: системы запущены")

class Laboratory(Auditorium):
    def status(self):
        print("Лаборатория: оборудование готово к работе")

lecture = LectureAuditorium()
computer = ComputerAuditorium()
lab = Laboratory()

lecture.status()
computer.status()
lab.status()