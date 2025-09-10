class Employee:
    language="py" # this is a class attribute
    salary=120000
harry=Employee()
harry.name="Harry"# this is an instance attribute
print( harry.name,harry.language,harry.salary)
rohan=Employee()
rohan.name="Rohan"
print( rohan.name,rohan.salary,rohan.language)
# Here name is instance attribute and salary and language
#are class attribute as they directly belong to the class