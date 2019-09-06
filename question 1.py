class Employee:
    numEmployees = 0

    def __init__(self, name="", family="", salary="", department=""):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.numEmployees += 1

    def fillFromUser(self):
        self.name = str(input("Name of the employee: "))
        self.family = str(input("Family of the employee: "))
        self.salary = str(input("Salary of the employee: "))
        self.department = str(input("Department of the employee: "))

    def __str__(self):
        outStr: str = "Name: " + self.name + "\n"
        outStr += "Family: " + self.family + "\n"
        outStr += "Salary: " + str(self.salary) + "\n"
        outStr += "Department: " + self.department + "\n"
        return outStr


def avgSal(employees):
    average = 0
    numEmps = employees[0].__class__.numEmployees

    for i in employees:
        average += int(i.salary)
    return average / numEmps


class FulltimeEmployee(Employee):
    def __init__(self, name="", family="", salary="", department="", hours=40):
        Employee.__init__(self, name, family, salary, department)
        self.hours = hours

theEmps = list()
theEmps.append( Employee("John", "White", 3600, "Sales"))
theEmps.append(FulltimeEmployee("Alice", "Wonderland", 74000, "IT", 43))
theEmps.append(FulltimeEmployee())
theEmps[2].fillFromUser()

for i in theEmps:
    print(i)
print(avgSal(theEmps))
