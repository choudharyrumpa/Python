# ------------------------------
# FUNCTIONS IN PYTHON - COMPLETE GUIDE
# ------------------------------

# 1. Simple function (without parameters, without return)
def greet():
    print("Hello! Welcome to Python Functions.")

# 2. Function with parameters
def add(a, b):
    return a + b

# 3. Function with default arguments
def power(base, exp=2):
    return base ** exp

# 4. Function with keyword arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

# 5. Function with variable-length arguments (*args)
def total_sum(*numbers):
    return sum(numbers)

# 6. Function with keyword variable-length arguments (**kwargs)
def person_details(**details):
    for key, value in details.items():
        print(f"{key} : {value}")

# 7. Returning multiple values
def calculate(a, b):
    return a + b, a - b, a * b, a / b

# 8. Anonymous function (lambda)
square = lambda x: x * x

# 9. Function inside another function (nested)
def outer():
    def inner():
        print("This is an inner function")
    inner()

# 10. Function as an argument (higher-order function)
def apply_function(func, value):
    return func(value)

# 11. Function returning another function (closure)
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

# 12. Recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# 13. Using map, filter, reduce with functions
from functools import reduce
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))      # map
evens = list(filter(lambda x: x % 2 == 0, nums)) # filter
product = reduce(lambda x, y: x * y, nums)       # reduce

# ------------------------------
# FUNCTION CALLS / DEMONSTRATION
# ------------------------------

greet()
print("Addition:", add(5, 3))
print("Power (default exp=2):", power(4))
print("Power (exp=3):", power(2, 3))
introduce(name="Alice", age=25)
print("Total Sum:", total_sum(10, 20, 30, 40))
person_details(Name="Ravi", Age=30, Country="India")

s, d, m, q = calculate(10, 5)
print("Results -> Sum:", s, "Diff:", d, "Mul:", m, "Div:", q)

print("Square of 6 (lambda):", square(6))

outer()
print("Apply function:", apply_function(square, 7))

times3 = multiplier(3)
print("Closure (5 * 3):", times3(5))

print("Factorial of 5:", factorial(5))

print("Squares using map:", squared)
print("Even numbers using filter:", evens)
print("Product using reduce:", product)
