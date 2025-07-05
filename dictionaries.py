# Lesson 5 - Dictionaries

# Creating a dictionary
student = {"name": "John", "age": 20, "course": "CS"}
print("Student dictionary:", student)

# Accessing values
print("Name:", student["name"])

# Adding a key-value pair
student["grade"] = "A"
print("After adding grade:", student)

# Lesson 6 - Dictionaries Part 2

# Looping through dictionary
person = {"name": "Jane", "age": 30, "city": "Cape Town"}
for key, value in person.items():
    print(key, ":", value)

# Updating values
person["age"] = 31
print("Updated age:", person["age"])

# Deleting a key
del person["city"]
print("After deleting city:", person)