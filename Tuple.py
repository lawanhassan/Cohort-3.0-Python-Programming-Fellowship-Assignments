
# Tuple Exercises: Level 1

# 1. Create an empty tuple
empty_tuple = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Alice', 'Emma')
brothers = ('John', 'Mark')

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# 4. How many siblings do you have?
num_of_siblings = len(siblings)
print(f"I have {num_of_siblings} siblings.")

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
father = 'Robert'
mother = 'Susan'
family_members = siblings + (father, mother)

# Tuple Exercises: Level 2

# 1. Unpack siblings and parents from family_members
siblings, father, mother = family_members[:-2], family_members[-2], family_members[-1]
print(f"Siblings: {siblings}, Father: {father}, Mother: {mother}")

# 2. Create fruits, vegetables, and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'cheese', 'butter')

food_stuff_tp = fruits + vegetables + animal_products
print("Food Stuff Tuple:", food_stuff_tp)

# 3. Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food Stuff List:", food_stuff_lt)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
middle_item = food_stuff_tp[len(food_stuff_tp)//2]
print(f"The middle item in the tuple is: {middle_item}")

# 5. Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(f"First three items: {first_three}")
print(f"Last three items: {last_three}")

# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp
# food_stuff_tp is now deleted and cannot be accessed.

# Check if an item exists in tuple:

# 1. Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
is_estonia_nordic = 'Estonia' in nordic_countries
print(f"Is Estonia a nordic country? {is_estonia_nordic}")

# 2. Check if 'Iceland' is a nordic country
is_iceland_nordic = 'Iceland' in nordic_countries
print(f"Is Iceland a nordic country? {is_iceland_nordic}")
