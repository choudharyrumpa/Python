class Employee:
    language="python" # this is a class attribute
    salary=120000
    def getInfo(self):
        print(f"The language is {self.language}.The salary is{self.salary}")
    @staticmethod
    def greet():
        print("Good morning")
harry=Employee()
harry.getInfo() # or Employee.getInfo(harry)
harry.greet()