
# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Golden Retriever'
dog['legs'] = 4
dog['age'] = 3

# Print the dog dictionary
print("Dog dictionary:", dog)

# Create a student dictionary
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'Data Analysis'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main Street'
}

# Get the length of the student dictionary
print("Length of student dictionary:", len(student))

# Get the value of skills and check the data type
skills = student['skills']
print("Skills:", skills)
print("Data type of skills:", type(skills))

# Modify the skills values by adding one or two skills
student['skills'].extend(['Machine Learning', 'Web Development'])
print("Updated skills:", student['skills'])

# Get the dictionary keys as a list
keys = list(student.keys())
print("Dictionary keys:", keys)

# Get the dictionary values as a list
values = list(student.values())
print("Dictionary values:", values)

# Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print("Student dictionary as list of tuples:", student_items)

# Delete one of the items in the dictionary
del student['address']
print("Student dictionary after deleting address:", student)

# Delete one of the dictionaries
del dog
