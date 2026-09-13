class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_name(self):
        return name
    def get_salary(self):
        return salary
    def set_salary(self, salary):
        self.salary = salary
    def set_name(self, name):
        self.name = name
    def raise_salary(self):
        return self.salary  * 1.1

john = Employee("John", 0)
john.set_salary(5000)
print("Salary:", int(john.raise_salary()))

