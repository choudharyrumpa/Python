# ---------- Other Program Using Set Methods ----------
print("=== STUDENT SUBJECT ANALYSIS USING SET METHODS ===")

# Subjects chosen by students
student_A_subjects = {"Math", "Science", "English", "History"}
student_B_subjects = {"Science", "English", "Geography", "Art"}

print("Student A subjects:", student_A_subjects)
print("Student B subjects:", student_B_subjects)

# Find common subjects (intersection)
common_subjects = student_A_subjects.intersection(student_B_subjects)
print("\nCommon subjects:", common_subjects)

# Find unique subjects for each student (difference)
unique_A = student_A_subjects.difference(student_B_subjects)
unique_B = student_B_subjects.difference(student_A_subjects)
print("Subjects only Student A takes:", unique_A)
print("Subjects only Student B takes:", unique_B)

# Find all subjects available (union)
all_subjects = student_A_subjects.union(student_B_subjects)
print("All subjects between both students:", all_subjects)

# Symmetric difference (subjects not shared)
not_shared = student_A_subjects.symmetric_difference(student_B_subjects)
print("Subjects not shared between students:", not_shared)

# Check subset / superset
print("Is Student A taking all subjects Student B takes?", student_B_subjects.issubset(student_A_subjects))
print("Is all_subjects a superset of Student A's subjects?", all_subjects.issuperset(student_A_subjects))

# Check if disjoint (no subjects in common)
print("Are Student A and Student B's subjects completely different?", student_A_subjects.isdisjoint(student_B_subjects))
