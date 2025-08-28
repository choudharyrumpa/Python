# Python program to demonstrate all conditional statements

# Taking an input number
num = int(input("Enter a number: "))

# 1. Simple if statement
if num > 0:
    print("The number is positive.")

# 2. if-else statement
if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

# 3. if-elif-else ladder
if num > 0:
    print("It is greater than 0.")
elif num == 0:
    print("It is equal to 0.")
else:
    print("It is less than 0.")

# 4. Nested if
if num >= 0:
    if num == 0:
        print("Number is Zero (checked using nested if).")
    else:
        print("Number is Positive (checked using nested if).")
else:
    print("Number is Negative (checked using nested if).")

# 5. Shorthand if (single statement)
if num == 100: print("You entered exactly 100!")

# 6. Shorthand if-else (ternary operator)
result = "Even" if num % 2 == 0 else "Odd"
print(f"Ternary operator says the number is {result}.")

# 7. Multiple conditions in single if using logical operators
if num > 0 and num < 10:
    print("The number is between 1 and 9.")
elif num >= 10 and num <= 99:
    print("The number is between 10 and 99.")
else:
    print("The number is either negative, zero, or >= 100.")

# 8. Using 'not' operator
if not (num < 0):
    print("Number is not negative.")
else:
    print("Number is negative.")

print("\n✅ Program executed successfully!")
