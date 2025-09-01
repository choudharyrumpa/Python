# Demonstrating all loop conditions in one program

# 1. FOR LOOP
print("=== FOR LOOP ===")
for i in range(1, 6):   # simple for loop
    print("Number:", i)

# 2. WHILE LOOP
print("\n=== WHILE LOOP ===")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# 3. NESTED LOOP (for inside while)
print("\n=== NESTED LOOP (While + For) ===")
x = 1
while x <= 3:
    for y in range(1, 4):
        print(f"x={x}, y={y}")
    x += 1

# 4. BREAK statement
print("\n=== BREAK in loop ===")
for i in range(1, 10):
    if i == 5:
        print("Breaking the loop at", i)
        break
    print(i)

# 5. CONTINUE statement
print("\n=== CONTINUE in loop ===")
for i in range(1, 10):
    if i % 2 == 0:   # skip even numbers
        continue
    print("Odd number:", i)

# 6. ELSE with FOR LOOP
print("\n=== ELSE with FOR LOOP ===")
for i in range(3):
    print("Iteration:", i)
else:
    print("Loop finished without break!")

# 7. ELSE with WHILE LOOP
print("\n=== ELSE with WHILE LOOP ===")
n = 1
while n <= 3:
    print("n =", n)
    n += 1
else:
    print("While loop ended normally (no break).")
