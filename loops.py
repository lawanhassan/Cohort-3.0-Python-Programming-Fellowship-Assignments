
# Exercises: Level 1

# 1. Iterate 0 to 10 using for and while loops
print("Iterate 0 to 10 using for loop:")
for i in range(11):
    print(i, end=" ")
print("\nIterate 0 to 10 using while loop:")
i = 0
while i <= 10:
    print(i, end=" ")
    i += 1

# Iterate 10 to 0 using for and while loops
print("\n\nIterate 10 to 0 using for loop:")
for i in range(10, -1, -1):
    print(i, end=" ")
print("\nIterate 10 to 0 using while loop:")
i = 10
while i >= 0:
    print(i, end=" ")
    i -= 1

# 2. Print a triangle
print("\n\nTriangle:")
for i in range(1, 8):
    print('#' * i)

# 3. Create an 8x8 grid
print("\n8x8 Grid:")
for _ in range(8):
    print("# " * 8)

# 4. Print multiplication pattern
print("\nMultiplication Pattern:")
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# 5. Iterate through a list and print items
languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
print("\nLanguages:")
for lang in languages:
    print(lang)

# 6. Print even numbers from 0 to 100
print("\nEven Numbers from 0 to 100:")
for i in range(0, 101, 2):
    print(i, end=" ")

# 7. Print odd numbers from 0 to 100
print("\n\nOdd Numbers from 0 to 100:")
for i in range(1, 101, 2):
    print(i, end=" ")

# Exercises: Level 2

# 8. Sum of all numbers from 0 to 100
total_sum = sum(range(101))
print(f"\n\nSum of all numbers (0-100): {total_sum}")

# 9. Sum of evens and odds from 0 to 100
even_sum = sum(i for i in range(101) if i % 2 == 0)
odd_sum = sum(i for i in range(101) if i % 2 != 0)
print(f"The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.")

# Exercises: Level 3

# 10. Extract countries containing "land"
try:
    from data.countries import countries  # Ensure this import works in your directory structure
    land_countries = [country for country in countries if 'land' in country.lower()]
    print("\nCountries containing 'land':", land_countries)
except ImportError:
    print("\nError: 'countries' data module not found. Ensure the file structure is correct.")

# 11. Reverse fruit list
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = fruits[::-1]
print("\nReversed Fruits:", reversed_fruits)

# 12. Analyze countries_data
try:
    from data.countries_data import countries_data  # Ensure this import works in your directory structure

    # Total number of languages
    all_languages = set(lang for country in countries_data for lang in country['languages'])
    print("\nTotal number of languages:", len(all_languages))

    # Ten most spoken languages
    from collections import Counter
    language_counter = Counter(lang for country in countries_data for lang in country['languages'])
    most_spoken_languages = language_counter.most_common(10)
    print("Ten most spoken languages:", most_spoken_languages)

    # Ten most populated countries
    populated_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]
    most_populated_countries = [(country['name'], country['population']) for country in populated_countries]
    print("Ten most populated countries:", most_populated_countries)
except ImportError:
    print("\nError: 'countries_data' module not found. Ensure the file structure is correct.")
