class Employee:
    language="python" # this is a class attribute
    salary=120000
    def getInfo(self):
        print(f"The language is {self.language}.The salary is{self.salary}")
    def __init__(self, name,salary,language):# dunder method which is automatically called when an object is create
        self.name= name
        self.salary=salary
        self.language=language
        print("I am creating an object")
    @staticmethod
    def greet():
        print("Good morning")
harry=Employee("Harry",130000,"Javascript")
harry.name="Harry"
print(harry.name,harry.salary,harry.language)
