# 1. String Declaration
str1 = "Hello"
str2 = 'World'
str3 = """This is
a multi-line
string"""

# 2. String Concatenation
full_str = str1 + " " + str2
print("Concatenated String:", full_str)

# 3. String Length
print("Length of string:", len(full_str))

# 4. Indexing
print("First character:", full_str[0])
print("Last character:", full_str[-1])

# 5. Slicing
print("Slice [0:5]:", full_str[0:5])   # Hello
print("Slice [-5:]:", full_str[-5:])   # World

# 6. Looping through string
print("Characters in string:")
for ch in full_str:
    print(ch, end=' ')
print()

# 7. String Methods
print("Uppercase:", full_str.upper())
print("Lowercase:", full_str.lower())
print("Title Case:", full_str.title())
print("Replaced:", full_str.replace("World", "Python"))
print("Count of 'l':", full_str.count('l'))
print("Starts with 'Hello':", full_str.startswith("Hello"))
print("Ends with 'World':", full_str.endswith("World"))

# 8. Strip and Whitespace
str_with_spaces = "   Hello Python   "
print("Original:", repr(str_with_spaces))
print("Stripped:", repr(str_with_spaces.strip()))

# 9. Split and Join
csv = "apple,banana,grape"
fruits = csv.split(",")
print("Split list:", fruits)
joined = "-".join(fruits)
print("Joined with '-':", joined)

# 10. String Formatting
name = "Rumpa"
age = 25
print("Formatted with f-string:", f"My name is {name} and I am {age} years old.")
print("Formatted with format():", "My name is {} and I am {} years old.".format(name, age))

# 11. Escape Characters
print("She said: \"Hello!\"")
print("Path with backslash: C:\\Users\\Name")

# 12. String is immutable
original = "hello"
modified = original.replace("h", "j")
print("Original:", original)   # won't change
print("Modified:", modified)

# 13. Checking content
s = "Python3"
print("Is alphanumeric?", s.isalnum())
print("Is alphabet only?", s.isalpha())
print("Is digit only?", s.isdigit())

# 14. Raw Strings (useful for regex, file paths)
print(r"This is a raw string:\nNot interpreted as newline")

# 15. Multiline and Triple Quotes
long_text = """This is a
multi-line string
using triple quotes."""
print(long_text)
