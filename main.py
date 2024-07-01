from first import Person, MyEmployee, ManagerEmployee, DeveloperEmployee, HumanResourceEmployee

person1 = Person("Alvin", "Male", "Single", "Kiambu")
person1.salutation()
person1.full_name()
# print(person1.name)
# print(person1.gender)
# print(person1.marital_status)
# print(person1.residence)
print(
    f"I am a {person1.gender} gentleman who is  {person1.marital_status} and I live  in {person1.residence} ")

person2 = Person("Bobo", "Female", "Single", "Nairobi")
person2.salutation()
(person2.full_name())
# print(person2.name)
# print(person2.gender)
# print(person2.marital_status)
# print(person2.residence)
print(f"I am a {person2.gender} who is currently  {person2.marital_status} and I reside  in {person2.residence} ")


MyEmployee1 = MyEmployee("Mary", "Njoki", 22, 20000)
print(MyEmployee1.first_name)
print(MyEmployee1.last_name)
print(MyEmployee1.age)
print(MyEmployee1.salary)
MyEmployee1.describe_employee()

ManagerEmployee1 = ManagerEmployee("Brian", "Bett", 32, 200000, "Male")
print(ManagerEmployee1.first_name)
print(ManagerEmployee1.last_name)
print(ManagerEmployee1.age)
print(ManagerEmployee1.salary)
print(ManagerEmployee1.gender)
ManagerEmployee1.describe_employee()


DeveloperEmployee1 = DeveloperEmployee("Frank", "Kiplagat", 25, 190000, "Python")
print(DeveloperEmployee1.first_name)
print(DeveloperEmployee1.last_name)
print(DeveloperEmployee1.age)
print(DeveloperEmployee1.salary)
print(DeveloperEmployee1.prog_language)
DeveloperEmployee1.describe_employee()


HumanResourceEmployee1 = HumanResourceEmployee("Judy", "Munyiva", 19, 25000, "Freelancer")
print(HumanResourceEmployee1.first_name)
print(HumanResourceEmployee1.last_name)
print(HumanResourceEmployee1.age)
print(HumanResourceEmployee1.salary)
print(HumanResourceEmployee1.employee_status)
HumanResourceEmployee1.describe_employee()
