
# Task 1: Concatenate 'Thirty', 'Days', 'Of', 'Python' to a single string
string1 = ' '.join(['Thirty', 'Days', 'Of', 'Python'])
print(string1)  # Output: 'Thirty Days Of Python'

# Task 2: Concatenate 'Coding', 'For', 'All' to a single string
string2 = ' '.join(['Coding', 'For', 'All'])
print(string2)  # Output: 'Coding For All'

# Task 3: Declare a variable named company and assign it to an initial value
company = "Coding For All"
print(company)  # Output: 'Coding For All'

# Task 4: Print the length of the company string
print(len(company))  # Output: 15

# Task 5: Change all the characters to uppercase letters
print(company.upper())  # Output: 'CODING FOR ALL'

# Task 6: Change all the characters to lowercase letters
print(company.lower())  # Output: 'coding for all'

# Task 7: Use capitalize(), title(), swapcase() methods
print(company.capitalize())  # Output: 'Coding for all'
print(company.title())  # Output: 'Coding For All'
print(company.swapcase())  # Output: 'cODING fOR aLL'

# Task 8: Cut (slice) out the first word of the string
first_word_removed = company[7:]  # From index 7 till end
print(first_word_removed)  # Output: 'For All'

# Task 9: Check if 'Coding For All' contains the word 'Coding'
contains_coding = 'Coding' in company
print(contains_coding)  # Output: True

# Task 10: Replace 'Coding' with 'Python' in 'Coding For All'
company_replaced = company.replace('Coding', 'Python')
print(company_replaced)  # Output: 'Python For All'

# Task 11: Change 'Python for Everyone' to 'Python for All' using replace
python_for_all = 'Python for Everyone'.replace('Everyone', 'All')
print(python_for_all)  # Output: 'Python for All'

# Task 12: Split the string 'Coding For All' using space as the separator
split_string = company.split()
print(split_string)  # Output: ['Coding', 'For', 'All']

# Task 13: Split the string 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon' at the comma
split_comma = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(', ')
print(split_comma)

# Task 14: What is the character at index 0 in 'Coding For All'
first_char = company[0]
print(first_char)  # Output: 'C'

# Task 15: What is the last index of the string 'Coding For All'
last_index = len(company) - 1
print(last_index)  # Output: 14

# Task 16: What character is at index 10 in 'Coding For All'
char_at_10 = company[10]
print(char_at_10)  # Output: 'r'

# Task 17: Create an acronym for 'Python For Everyone'
acronym = ''.join([word[0] for word in 'Python For Everyone'.split()])
print(acronym)  # Output: 'PFE'

# Task 18: Create an acronym for 'Coding For All'
acronym2 = ''.join([word[0] for word in 'Coding For All'.split()])
print(acronym2)  # Output: 'CFA'

# Task 19: Use index to determine the position of the first occurrence of 'C' in 'Coding For All'
position_C = company.index('C')
print(position_C)  # Output: 0

# Task 20: Use index to determine the position of the first occurrence of 'F' in 'Coding For All'
position_F = company.index('F')
print(position_F)  # Output: 7

# Task 21: Use rfind to determine the position of the last occurrence of 'l' in 'Coding For All People'
last_position_l = company.rfind('l')
print(last_position_l)  # Output: 14

# Task 22: Use index or find to find the position of the first occurrence of 'because'
sentence = 'You cannot end a sentence with because because because is a conjunction'
position_because = sentence.find('because')
print(position_because)  # Output: 34

# Task 23: Use rindex to find the position of the last occurrence of 'because'
position_because_last = sentence.rindex('because')
print(position_because_last)  # Output: 50

# Task 24: Slice out 'because because because' from the sentence
phrase = sentence[34:51]
print(phrase)  # Output: 'because because because'

# Task 25: Find the position of the first occurrence of 'because'
position_first_because = sentence.find('because')
print(position_first_because)  # Output: 34

# Task 26: Slice out 'because because because' in the sentence again
phrase_again = sentence[34:51]
print(phrase_again)  # Output: 'because because because'

# Task 27: Check if 'Coding For All' starts with 'Coding'
starts_with_coding = company.startswith('Coding')
print(starts_with_coding)  # Output: True

# Task 28: Check if 'Coding For All' ends with 'coding'
ends_with_coding = company.endswith('coding')
print(ends_with_coding)  # Output: False

# Task 29: Remove the left and right trailing spaces from the string
stripped_string = '   Coding For All      '.strip()
print(stripped_string)  # Output: 'Coding For All'

# Task 30: Check which variable returns True when we use the method isidentifier()
print('30DaysOfPython'.isidentifier())  # Output: True
print('thirty_days_of_python'.isidentifier())  # Output: True

# Task 31: Join the list with a hash with space string
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(python_libraries)
print(joined_libraries)  # Output: 'Django # Flask # Bottle # Pyramid # Falcon'

# Task 32: Use the new line escape sequence to separate sentences
print("I am enjoying this challenge.\nI just wonder what is next.")

# Task 33: Use a tab escape sequence to write the following lines
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# Task 34: Use string formatting to display the area of a circle
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# Task 35: String formatting for mathematical operations
print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6:.2f}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")
