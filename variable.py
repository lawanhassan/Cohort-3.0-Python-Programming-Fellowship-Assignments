
##Level 1
# Declaring individual variables
first_name = "Kabiru"
last_name = "Adamu"
full_name = first_name + " " + last_name
country = "Nigeria"
city = "Kano"
age = 20
year = 2024
is_married = False
is_true = True
is_light_on = False

# Declaring multiple variables on one line
a, b, c = 10, 20, 30

# Print statements for testing
print("First Name:", first_name)
print("Last Name:", last_name)
print("Full Name:", full_name)
print("Country:", country)
print("City:", city)
print("Age:", age)
print("Year:", year)
print("Is Married:", is_married)
print("Is True:", is_true)
print("Is Light On:", is_light_on)
print("Multiple variables: a =", a, ", b =", b, ", c =", c)

##Level 2
# Checking the data type of variables
print("Data type of first_name:", type(first_name))
print("Data type of last_name:", type(last_name))
print("Data type of full_name:", type(full_name))
print("Data type of country:", type(country))
print("Data type of city:", type(city))
print("Data type of age:", type(age))
print("Data type of year:", type(year))
print("Data type of is_married:", type(is_married))
print("Data type of is_true:", type(is_true))
print("Data type of is_light_on:", type(is_light_on))

# Using len() to find the length of the first name
length_first_name = len(first_name)
print("Length of first name:", length_first_name)

# Comparing the length of the first name and last name
length_last_name = len(last_name)
print("Length of last name:", length_last_name)
print("Is the first name longer than the last name?", length_first_name > length_last_name)

# Declaring numbers and performing operations
num_one = 5
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

# Printing the results
print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponentiation:", exp)
print("Floor Division:", floor_division)

# Calculating the area and circumference of a circle
radius = 30  # Radius in meters
pi = 3.14159
area_of_circle = pi * radius**2
circum_of_circle = 2 * pi * radius

# Printing area and circumference
print("Area of the circle:", area_of_circle)
print("Circumference of the circle:", circum_of_circle)

# Taking radius as user input to calculate the area
radius_input = float(input("Enter the radius of a circle: "))
area_of_circle_user = pi * radius_input**2
print("Area of the circle with user input radius:", area_of_circle_user)

# Taking user input for personal details
user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_country = input("Enter your country: ")
user_age = int(input("Enter your age: "))

# Printing user details
print("User's First Name:", user_first_name)
print("User's Last Name:", user_last_name)
print("User's Country:", user_country)
print("User's Age:", user_age)

# Checking Python reserved keywords
print("Python Reserved Keywords:")
help('keywords')