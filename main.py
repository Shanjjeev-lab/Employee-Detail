class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber  = idnumber

    def display(self):
        print("Name:", self.name, "ID:", self.idnumber)

class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        Person.__init__(self, name, idnumber)
        self.salary = salary
        self.post = post

employee1 = Employee("John Robes", 100, 185,"Marine Biology")
employee1.display()
