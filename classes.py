
import math
from collections import Counter

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        middle = n // 2
        if n % 2 == 0:
            return (sorted_data[middle - 1] + sorted_data[middle]) / 2
        return sorted_data[middle]

    def mode(self):
        frequencies = Counter(self.data)
        max_count = max(frequencies.values())
        mode = [key for key, value in frequencies.items() if value == max_count]
        return {"mode": mode[0], "count": max_count} if mode else None

    def var(self):
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / self.count()

    def std(self):
        return math.sqrt(self.var())

    def freq_dist(self):
        frequencies = Counter(self.data)
        total_count = self.count()
        return [(round((count / total_count) * 100, 1), value) for value, count in frequencies.items()]

    def describe(self):
        return {
            "Count": self.count(),
            "Sum": self.sum(),
            "Min": self.min(),
            "Max": self.max(),
            "Range": self.range(),
            "Mean": round(self.mean(), 1),
            "Median": self.median(),
            "Mode": self.mode(),
            "Variance": round(self.var(), 1),
            "Standard Deviation": round(self.std(), 1),
            "Frequency Distribution": self.freq_dist()
        }

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print("Count:", data.count())
print("Sum: ", data.sum())
print("Min: ", data.min())
print("Max: ", data.max())
print("Range: ", data.range())
print("Mean: ", data.mean())
print("Median: ", data.median())
print("Mode: ", data.mode())
print("Standard Deviation: ", data.std())
print("Variance: ", data.var())
print("Frequency Distribution: ", data.freq_dist())
print("Description: ", data.describe())

# Level 2
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, description, amount):
        self.incomes.append({"description": description, "amount": amount})

    def add_expense(self, description, amount):
        self.expenses.append({"description": description, "amount": amount})

    def total_income(self):
        return sum(item["amount"] for item in self.incomes)

    def total_expense(self):
        return sum(item["amount"] for item in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return {
            "Firstname": self.firstname,
            "Lastname": self.lastname,
            "Total Income": self.total_income(),
            "Total Expense": self.total_expense(),
            "Account Balance": self.account_balance(),
        }

# Example usage
person = PersonAccount("John", "Doe")
person.add_income("Salary", 5000)
person.add_income("Freelance", 1500)
person.add_expense("Rent", 1200)
person.add_expense("Utilities", 300)

print("Account Info:", person.account_info())
