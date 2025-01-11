
import math
from statistics import mean, median, mode, pstdev, variance

# Level 1
def add_two_numbers(a, b):
    return a + b

def area_of_circle(r):
    return math.pi * r ** 2

def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    return "All arguments must be numbers."

def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def check_season(month):
    seasons = {
        'Winter': ['December', 'January', 'February'],
        'Spring': ['March', 'April', 'May'],
        'Summer': ['June', 'July', 'August'],
        'Autumn': ['September', 'October', 'November']
    }
    for season, months in seasons.items():
        if month in months:
            return season
    return "Invalid month"

def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def solve_quadratic_eqn(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        return "No real roots"

def print_list(lst):
    for item in lst:
        print(item)

def reverse_list(arr):
    return arr[::-1]

def capitalize_list_items(lst):
    return [item.upper() for item in lst]

def add_item(lst, item):
    lst.append(item)
    return lst

def remove_item(lst, item):
    lst.remove(item)
    return lst

def sum_of_numbers(n):
    return sum(range(1, n + 1))

def sum_of_odds(n):
    return sum(i for i in range(1, n + 1) if i % 2 != 0)

def sum_of_even(n):
    return sum(i for i in range(1, n + 1) if i % 2 == 0)

# Level 2
def evens_and_odds(n):
    evens = len([i for i in range(n + 1) if i % 2 == 0])
    odds = len([i for i in range(n + 1) if i % 2 != 0])
    return f"The number of evens is {evens}. The number of odds is {odds}."

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def is_empty(variable):
    return not bool(variable)

def calculate_mean(lst):
    return mean(lst)

def calculate_median(lst):
    return median(lst)

def calculate_mode(lst):
    return mode(lst)

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    return variance(lst)

def calculate_std(lst):
    return pstdev(lst)

# Level 3
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_items_unique(lst):
    return len(lst) == len(set(lst))

def all_items_same_type(lst):
    return all(type(i) == type(lst[0]) for i in lst)

def is_valid_variable(var):
    import keyword
    return var.isidentifier() and not keyword.iskeyword()

def most_spoken_languages(data, top_n=10):
    languages = {}
    for country in data:
        for lang in country['languages']:
            languages[lang] = languages.get(lang, 0) + 1
    return sorted(languages.items(), key=lambda x: x[1], reverse=True)[:top_n]

def most_populated_countries(data, top_n=10):
    return sorted(data, key=lambda x: x['population'], reverse=True)[:top_n]

# List Comprehension Exercises
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [i for i in numbers if i <= 0]

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]

tuples_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country[0].upper(), country[0][:3].upper(), city.upper()] for sublist in countries for country, city in sublist]
countries_dict = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [' '.join(name) for sublist in names for name in sublist]

# Lambda for slope calculation
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
