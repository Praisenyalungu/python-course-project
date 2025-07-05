# Lesson 4: Numeric Data
a = 5
b = 3.2
c = a + b
print("Sum:", c)
age = 22
name = "Praise"
is_student = True

print("Name:", name)
print("Age:", age)
print("Is Student:", is_student)
x = 10
y = 4

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)
print("Exponent:", x ** y)
print("Floor Division:", x // y)
num = 7

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# Lesson 9: Nested If & Logical Operators
age = 20
has_id = True

if age >= 18 and has_id:
    print("Access granted")
else:
    print("Access denied")
# Lesson 10: For Loops
for i in range(5):
    print("Iteration:", i)

# While loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# Lesson 11: Loop Control
for i in range(10):
    if i == 5:
        continue  # Skip 5
    if i == 8:
        break  # Stop at 8
    print(i)

