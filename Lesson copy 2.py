class School:
    def __init__(self, group):
        self.group = group
        self.students = []

    def add_passenger(self, *args):
        for passenger in args:
            self.students.append(passenger)

    def print_students_names(self):
        if self.students:
            print(f"Names of {self.group} students:")
            for student in self.students:
                print(student.name)
        else:
            print(f"There are no students in {self.group}")


class Human:
    def __init__(self, name):
        self.name = name


nick = Human("Nick")
kate = Human("Kate")
artem = Human("Artem")
jane = Human("Jane")
yevhen = Human("Yevhen")


school1 = School("Group1")
school2 = School("Group2")


school1.add_passenger(nick, kate, artem, jane, yevhen)


school2.add_passenger(nick, kate)

school1.print_students_names()
school2.print_students_names()