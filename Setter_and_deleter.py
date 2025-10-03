# Example: Using property, setter, and deleter

class Student:
    def __init__(self, name, marks):
        self._name = name           # private attribute (convention: underscore _)
        self._marks = marks

    # Getter method using @property
    @property
    def marks(self):
        return self._marks

    # Setter method for marks
    @marks.setter
    def marks(self, value):
        if value < 0 or value > 100:
            print(" Marks must be between 0 and 100.")
        else:
            self._marks = value
            print("Marks updated successfully.")

    # Deleter method
    @marks.deleter
    def marks(self):
        print("Marks deleted!")
        del self._marks

# ------------------------------
# Testing the Student class
# ------------------------------
s1 = Student("Riya", 85)

print("Initial Marks:", s1.marks)   # calls getter

s1.marks = 95                       # calls setter
print("Updated Marks:", s1.marks)

s1.marks = 150                      # invalid (setter blocks it)

del s1.marks                        # calls deleter
