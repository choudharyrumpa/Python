# Python program demonstrating all set methods

# Initial sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
C = {7, 8, 9}

print("Initial Sets:")
print("A =", A)
print("B =", B)
print("C =", C)
print("="*50)

# 1. add()
print("1. add()")
A.add(10)
print("After A.add(10):", A)

# 2. clear()
print("\n2. clear()")
temp = {1, 2, 3}
temp.clear()
print("After clear():", temp)

# 3. copy()
print("\n3. copy()")
copy_A = A.copy()
print("Copy of A:", copy_A)

# 4. difference()
print("\n4. difference()")
print("A.difference(B):", A.difference(B))

# 5. difference_update()
print("\n5. difference_update()")
temp = A.copy()
temp.difference_update(B)
print("After A.difference_update(B):", temp)

# 6. discard()
print("\n6. discard()")
A.discard(10)
print("After A.discard(10):", A)

# 7. intersection()
print("\n7. intersection()")
print("A.intersection(B):", A.intersection(B))

# 8. intersection_update()
print("\n8. intersection_update()")
temp = A.copy()
temp.intersection_update(B)
print("After A.intersection_update(B):", temp)

# 9. isdisjoint()
print("\n9. isdisjoint()")
print("A.isdisjoint(C):", A.isdisjoint(C))

# 10. issubset()
print("\n10. issubset()")
print("{4,5}.issubset(A):", {4, 5}.issubset(A))

# 11. issuperset()
print("\n11. issuperset()")
print("A.issuperset({4,5}):", A.issuperset({4, 5}))

# 12. pop()
print("\n12. pop()")
temp = A.copy()
print("Popped element:", temp.pop())
print("After pop():", temp)

# 13. remove()
print("\n13. remove()")
temp = A.copy()
temp.remove(2)
print("After remove(2):", temp)

# 14. symmetric_difference()
print("\n14. symmetric_difference()")
print("A.symmetric_difference(B):", A.symmetric_difference(B))

# 15. symmetric_difference_update()
print("\n15. symmetric_difference_update()")
temp = A.copy()
temp.symmetric_difference_update(B)
print("After A.symmetric_difference_update(B):", temp)

# 16. union()
print("\n16. union()")
print("A.union(B):", A.union(B))

# 17. update()
print("\n17. update()")
temp = A.copy()
temp.update(C)
print("After A.update(C):", temp)

print("\n=== All set methods demonstrated successfully ===")
