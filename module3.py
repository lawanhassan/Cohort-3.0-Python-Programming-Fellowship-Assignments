
# Question 1: What is your age as an integer variable?
age = 25

# Question 2: What is your height as a float variable?
height = 5.9

# Question 3: What is a complex number? Declare a variable that stores a complex number.
complex_number = 3 + 4j

# Question 4: Write a script that prompts the user to enter the base and height of a triangle. 
# Then, calculate the area of the triangle (area = 0.5 * base * height).
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print(f"The area of the triangle is {area}")

# Question 5: Write a script that prompts the user to enter side a, side b, and side c of a triangle. 
# Then, calculate the perimeter of the triangle (perimeter = a + b + c).
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print(f"The perimeter of the triangle is {perimeter}")

# Question 6: Write a script that prompts the user to enter the length and width of a rectangle. 
# Then, calculate its area (area = length * width) and perimeter (perimeter = 2 * (length + width)).
length = float(input("Enter length: "))
width = float(input("Enter width: "))
rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)
print(f"The area of the rectangle is {rectangle_area}")
print(f"The perimeter of the rectangle is {rectangle_perimeter}")

# Question 7: Write a script that prompts the user to enter the radius of a circle. 
# Then, calculate its area (area = pi * r * r) and circumference (c = 2 * pi * r), where pi = 3.14.
radius = float(input("Enter radius of the circle: "))
pi = 3.14
circle_area = pi * (radius ** 2)
circle_circumference = 2 * pi * radius
print(f"The area of the circle is {circle_area}")
print(f"The circumference of the circle is {circle_circumference}")

# Question 8: What is the slope of the equation y = 2x - 2? 
# Also, calculate the Euclidean distance between points (2, 2) and (6, 10).
slope = 2  # As the coefficient of x is 2
print(f"The slope of y = 2x - 2 is {slope}")
distance = ((6 - 2) ** 2 + (10 - 2) ** 2) ** 0.5
print(f"The Euclidean distance between point (2, 2) and point (6, 10) is {distance}")

# Question 9: Compare the slopes from Task 8. Are they equal?
print(f"Are the slopes equal? {slope == 2}")

# Question 10: What is the value of y in the equation y = x^2 + 6x + 9 for different x values? 
# Try to use different x values and figure out at which x value y is going to be 0.
for x in range(-10, 11):
    y = x ** 2 + 6 * x + 9
    if y == 0:
        print(f"x = {x} makes y = 0")
        break

# Question 11: What is the length of 'python' and 'dragon'? 
# Make a comparison between the lengths of 'python' and 'dragon'.
python_len = len('python')
dragon_len = len('dragon')
print(f"Is the length of 'python' equal to the length of 'dragon'? {python_len == dragon_len}")

# Question 12: Use the 'and' operator to check if 'on' is found in both 'python' and 'dragon'.
print(f"Is 'on' in both 'python' and 'dragon'? {'on' in 'python' and 'on' in 'dragon'}")

# Question 13: Use the 'in' operator to check if the word 'jargon' is in the following sentence.
sentence = "I hope this course is not full of jargon."
print(f"Is 'jargon' in the sentence? {'jargon' in sentence}")

# Question 14: Find the length of the word 'python', convert it to float, and then to a string.
length_python = len('python')
length_float = float(length_python)
length_string = str(length_float)
print(f"The length of 'python' as a float is {length_float} and as a string is {length_string}")

# Question 15: How can you check if a number is even or not using Python?
number = 6
print(f"Is the number even? {number % 2 == 0}")

# Question 16: Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(f"Is 7 // 3 equal to int(2.7)? {7 // 3 == int(2.7)}")

# Question 17: Check if the type of '10' is equal to the type of 10.
print(f"Is type of '10' equal to type of 10? {type('10') == type(10)}")

# Question 18: Check if int('9.8') is equal to 10.
print(f"Is int('9.8') equal to 10? {int(9.8) == 10}")

# Question 19: Write a script that prompts the user to enter hours worked and the rate per hour. 
# Then, calculate the weekly pay.
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
weekly_pay = hours * rate_per_hour
print(f"Your weekly earning is {weekly_pay}")

# Question 20: Write a script that prompts the user to enter the number of years they have lived. 
# Calculate the number of seconds they have lived, assuming 1 year = 365 days.
years_lived = int(input("Enter number of years you have lived: "))
seconds_lived = years_lived * 365 * 24 * 60 * 60  # Approximate for 1 year = 365 days
print(f"You have lived for {seconds_lived} seconds.")

# Question 21: Display the following table:
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
