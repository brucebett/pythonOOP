class Person:
    def __init__(self, name, gender, marital_status, residence):
        self.name = name
        self.gender = gender
        self.marital_status = marital_status
        self.residence = residence

    def salutation(self):
        print("Hello, my name is " + self.name)

    def full_name(self):
        return self.name + " "


class MyEmployee:
    def __init__(self, first_name, last_name, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary

    def describe_employee(self):
        print("Name: " + self.first_name + " ", self.last_name)


class ManagerEmployee(MyEmployee):
    def __init__(self, first_name, last_name, age, salary, gender):
        super().__init__(first_name, last_name, age, salary)
        self.gender = gender


class DeveloperEmployee(MyEmployee):
    def __init__(self, first_name, last_name, age, salary, prog_language):
        super().__init__(first_name, last_name, age, salary)
        self.prog_language = prog_language


class HumanResourceEmployee(MyEmployee):
    def __init__(self, first_name, last_name, age, salary, employee_status):
        super().__init__(first_name, last_name, age, salary)
        self.employee_status = employee_status

