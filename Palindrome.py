# Function to check if a string is a palindrome
def is_palindrome(text):
    # Remove spaces and convert to lowercase for uniform comparison
    text = text.replace(" ", "").lower()
    
    # Reverse the string using slicing
    reversed_text = text[::-1]
    
    # Check if original string and reversed string are the same
    if text == reversed_text:
        return True
    else:
        return False

# --- Main Program ---

# Ask the user to enter a string
user_input = input("Enter a word or sentence to check if it's a palindrome: ")

# Call the function and print the result
if is_palindrome(user_input):
    print("✅ It is a palindrome!")
else:
    print("❌ It is not a palindrome.")
