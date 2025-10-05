class Employee:
    def __init__(self, name, pos, salary):
        self.name = name
        self.pos = pos
        self.salary = salary

class Department:
    def __init__(self):
        self.employees = []

    def add(self, emp):
        self.employees.append(emp)

    def remove(self, name):
        self.employees = [e for e in self.employees if e.name != name]

    def total_salary(self):
        return sum(e.salary for e in self.employees)


e1 = Employee("Олег", "Менеджер", 20000)
e2 = Employee("Марія", "Бухгалтер", 18000)

dep = Department()
dep.add(e1)
dep.add(e2)

print(dep.total_salary())
dep.remove("Олег")
print(dep.total_salary())
