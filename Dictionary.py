# Dictionary Methods Demonstration

# Create a sample dictionary
student = {
    "name": "Riya",
    "age": 21,
    "course": "Computer Science",
    "marks": {"Math": 90, "Python": 95}
}

print("Original Dictionary:", student)

# 1. keys() - returns all keys
print("\n1. Keys:", student.keys())

# 2. values() - returns all values
print("2. Values:", student.values())

# 3. items() - returns all key-value pairs
print("3. Items:", student.items())

# 4. get() - safely get a value (returns None if key not found)
print("4. Get age:", student.get("age"))
print("   Get unknown key:", student.get("grade", "Not Found"))

# 5. update() - update dictionary with another dictionary
student.update({"age": 22, "semester": 5})
print("5. After update:", student)

# 6. copy() - shallow copy
student_copy = student.copy()
print("6. Copy:", student_copy)

# 7. pop() - remove a key and return its value
removed = student.pop("course")
print("7. Popped value (course):", removed)
print("   After pop:", student)

# 8. popitem() - remove last inserted key-value pair
last_item = student.popitem()
print("8. Popped last item:", last_item)
print("   After popitem:", student)

# 9. setdefault() - return value if key exists; otherwise insert key with default value
default_val = student.setdefault("city", "Delhi")
print("9. Setdefault city:", default_val)
print("   After setdefault:", student)

# 10. clear() - remove all items
student_copy.clear()
print("10. After clear (student_copy):", student_copy)

# 11. fromkeys() - create dictionary from keys with default value
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print("11. Fromkeys:", new_dict)
