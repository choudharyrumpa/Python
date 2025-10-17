# Example: Exception Handling in Python

try:
    # Code that might cause an exception
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    result = num1 / num2   # This line may raise ZeroDivisionError
    print("Result:", result)

except ValueError:
    # Handles error if user enters something that cannot be converted to an integer
    print("Error: Please enter valid numbers only!")

except ZeroDivisionError:
    # Handles error if user tries to divide by zero
    print("Error: Division by zero is not allowed!")

else:
    # Runs only if no exception occurs
    print("Division successful!")

finally:
    # Runs no matter what happens (useful for cleanup code)
    print("Program execution completed.")
