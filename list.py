
# Exercises: Level 1

# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
fruits = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'mango']

# 3. Find the length of your list
length = len(fruits)
print(length)

# 4. Get the first item, the middle item, and the last item of the list
first_item = fruits[0]
middle_item = fruits[len(fruits)//2]
last_item = fruits[-1]

# 5. Declare a list called mixed_data_types
mixed_data_types = ['John Doe', 30, 5.9, 'Married', '1234 Elm Street']

# 6. Declare a list variable named it_companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle, and last company
print(it_companies[0])  # First company
print(it_companies[len(it_companies)//2])  # Middle company
print(it_companies[-1])  # Last company

# 10. Modify one of the companies
it_companies[1] = 'Alphabet'
print(it_companies)

# 11. Add an IT company
it_companies.append('Tesla')

# 12. Insert an IT company in the middle
it_companies.insert(len(it_companies)//2, 'Spotify')

# 13. Change one of the it_companies names to uppercase (excluding IBM)
it_companies[0] = it_companies[0].upper()

# 14. Join the it_companies with a string '#; '
joined_string = '#; '.join(it_companies)
print(joined_string)

# 15. Check if a certain company exists
print('Facebook' in it_companies)

# 16. Sort the list
it_companies.sort()

# 17. Reverse the list
it_companies.reverse()

# 18. Slice out the first 3 companies
print(it_companies[:3])

# 19. Slice out the last 3 companies
print(it_companies[-3:])

# 20. Slice out the middle IT company or companies
middle = len(it_companies)//2
print(it_companies[middle-1:middle+1] if len(it_companies) % 2 == 0 else it_companies[middle])

# 21. Remove the first IT company
it_companies.pop(0)

# 22. Remove the middle IT company
middle = len(it_companies)//2
it_companies.pop(middle)

# 23. Remove the last IT company
it_companies.pop()

# 24. Remove all IT companies
it_companies.clear()

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_list = front_end + back_end

# 27. Insert Python and SQL after Redux
full_stack = joined_list.copy()
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')

# Exercises: Level 2

# 1. Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(min(ages), max(ages))

# 2. Add the min age and the max age again
ages.append(min(ages))
ages.append(max(ages))

# 3. Find the median age
middle = len(ages)//2
median = (ages[middle] + ages[middle-1])/2 if len(ages) % 2 == 0 else ages[middle]

# 4. Find the average age
average_age = sum(ages) / len(ages)

# 5. Find the range of ages
range_ages = max(ages) - min(ages)

# 6. Compare (min - average) and (max - average)
comparison = abs(min(ages) - average_age) - abs(max(ages) - average_age)

# 7. Find the middle country
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle = len(countries)//2
middle_countries = countries[middle-1:middle+1] if len(countries) % 2 == 0 else countries[middle]

# 8. Divide the countries list
first_half = countries[:len(countries)//2 + 1] if len(countries) % 2 != 0 else countries[:len(countries)//2]
second_half = countries[len(countries)//2:] if len(countries) % 2 != 0 else countries[len(countries)//2:]

# 9. Unpack the first three countries and the rest as scandic_countries
first, second, third, *scandic_countries = countries