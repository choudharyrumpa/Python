class Employee:
    language="python" # this is a class attribute
    salary=120000
harry=Employee()
harry.language="Javascript"# this is an instance attribute
print(harry.language,harry.salary)
