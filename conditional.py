
# Exercises: Level 1

# 1. Get user input and check age for driving eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

# 2. Compare ages
my_age = 25  # Replace with your age
your_age = int(input("Enter your age: "))
if your_age > my_age:
    difference = your_age - my_age
    print(f"You are {difference} year{'s' if difference > 1 else ''} older than me.")
elif your_age < my_age:
    difference = my_age - your_age
    print(f"I am {difference} year{'s' if difference > 1 else ''} older than you.")
else:
    print("We are the same age.")

# 3. Compare two numbers
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

# Exercises: Level 2

# 1. Grade students based on scores
score = int(input("Enter your score: "))
if 80 <= score <= 100:
    print("A")
elif 70 <= score <= 89:
    print("B")
elif 60 <= score <= 69:
    print("C")
elif 50 <= score <= 59:
    print("D")
elif 0 <= score <= 49:
    print("F")
else:
    print("Invalid score.")

# 2. Determine the season
month = input("Enter the month: ").capitalize()
if month in ['September', 'October', 'November']:
    print("The season is Autumn.")
elif month in ['December', 'January', 'February']:
    print("The season is Winter.")
elif month in ['March', 'April', 'May']:
    print("The season is Spring.")
elif month in ['June', 'July', 'August']:
    print("The season is Summer.")
else:
    print("Invalid month.")

# 3. Add fruit to the list if it doesn't exist
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ").lower()
if fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit)
    print(f"The updated list of fruits: {fruits}")

# Exercises: Level 3

# Person dictionary
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Check if the person has 'skills' key and print the middle skill
if 'skills' in person:
    skills = person['skills']
    middle = len(skills) // 2
    print(f"The middle skill is: {skills[middle]}")

# 2. Check if the person has 'Python' skill
if 'skills' in person:
    print("Python" in person['skills'])

# 3. Determine the person's title based on skills
if set(person['skills']) == {'JavaScript', 'React'}:
    print("He is a front end developer.")
elif all(skill in person['skills'] for skill in ['Node', 'Python', 'MongoDB']):
    print("He is a backend developer.")
elif all(skill in person['skills'] for skill in ['React', 'Node', 'MongoDB']):
    print("He is a fullstack developer.")
else:
    print("Unknown title.")

# 4. Check if the person is married and lives in Finland
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")
