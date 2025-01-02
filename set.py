
# Sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Sets Exercises: Level 1

# 1. Find the length of the set it_companies
length_it_companies = len(it_companies)
print(f"The length of the it_companies set is: {length_it_companies}")

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(f"Updated it_companies set: {it_companies}")

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update({'Tesla', 'Spotify', 'Snapchat'})
print(f"After adding multiple companies: {it_companies}")

# 4. Remove one of the companies from the set it_companies
it_companies.remove('Snapchat')  # Removes 'Snapchat'
print(f"After removing a company: {it_companies}")

# 5. What is the difference between remove and discard?
# `remove()` raises a KeyError if the item doesn't exist, while `discard()` does not raise an error.
# Example: 
# it_companies.remove('NonExistent')  # This would raise an error
# it_companies.discard('NonExistent')  # This will not raise an error

# Sets Exercises: Level 2

# 1. Join A and B
union_A_B = A.union(B)
print(f"Union of A and B: {union_A_B}")

# 2. Find A intersection B
intersection_A_B = A.intersection(B)
print(f"Intersection of A and B: {intersection_A_B}")

# 3. Is A subset of B
is_subset = A.issubset(B)
print(f"Is A a subset of B? {is_subset}")

# 4. Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)
print(f"Are A and B disjoint sets? {are_disjoint}")

# 5. Join A with B and B with A
join_A_B = A | B
join_B_A = B | A
print(f"Join A with B: {join_A_B}")
print(f"Join B with A: {join_B_A}")

# 6. What is the symmetric difference between A and B
symmetric_diff = A.symmetric_difference(B)
print(f"Symmetric difference between A and B: {symmetric_diff}")

# 7. Delete the sets completely
del A
del B
print("Sets A and B are deleted.")

# Sets Exercises: Level 3

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(f"Length of age list: {len(age)}")
print(f"Length of age set: {len(age_set)}")

# The list has duplicates, so the set will have a smaller length since it only contains unique values.
print(f"Are the list and set lengths different? {len(age) != len(age_set)}")

# 2. Explain the difference between the following data types: string, list, tuple, and set
# - String: A sequence of characters (immutable).
# - List: An ordered collection of items (mutable).
# - Tuple: An ordered collection of items (immutable).
# - Set: An unordered collection of unique items (mutable, but no duplicates allowed).

# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()  # Split the sentence into words
unique_words = set(words)  # Use a set to find unique words
print(f"Unique words in the sentence: {unique_words}")
print(f"Number of unique words: {len(unique_words)}")
