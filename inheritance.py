class Employee():
    company="ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

# class Programmer():
#     company="ITC Infotech"
#     def show(self):
#         print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

#     def showlanguage(self):
#         print(f"The name of the Employee is {self.name} and he is good with {self.language} language")

class Programmer():
    company="ITC Infotech"
    def showlanguage(self):
        print(f"The name of the Employee is {self.name} and he is good with {self.language} language")

a=Employee()
b=Programmer()
print(a.company,b.company)

