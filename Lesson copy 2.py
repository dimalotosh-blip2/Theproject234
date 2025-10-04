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

# Assuming a Human class exists with a 'name' attribute
class Human:
    def __init__(self, name):
        self.name = name

# Creating Human objects
nick = Human("Nick")
kate = Human("Kate")
artem = Human("Artem")
jane = Human("Jane")
yevhen = Human("Yevhen")

# Creating two different instances from the *same* School class
school1 = School("Group1")
school2 = School("Group2")

# Adding students to the first school
school1.add_passenger(nick, kate, artem, jane, yevhen)


school2.add_passenger(nick, kate)

school1.print_students_names()
school2.print_students_names()