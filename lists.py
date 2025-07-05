# Lesson 1 - Lists Part 1

# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Initial list:", fruits)

# Accessing elements
print("First fruit:", fruits[0])

# Modifying elements
fruits[1] = "blueberry"
print("After modifying second fruit:", fruits)

# Adding elements
fruits.append("orange")
print("After appending a fruit:", fruits)
# Lesson 2 - Lists Part 2

# Removing elements
numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print("After removing 3:", numbers)

# Popping elements
popped = numbers.pop()
print("Popped element:", popped)
print("List after pop:", numbers)

# Slicing
print("First two elements:", numbers[:2])