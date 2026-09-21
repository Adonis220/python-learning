print("Unit 3.1: Iterating Through Dictionaries")
print("Beginner")

inventory = {"apples": 50, "bananas": 30, "oranges": 25}

print(" 1. Print each product name using default iteration")
for product in inventory:
    print(product)

print(" 2. Calculate total items using values()")
total_items = sum(inventory.values())
print("Total items:", total_items)

print(" 3. Print each product with quantity using items()")
for product, quantity in inventory.items():
    print(product, quantity)

print("Intermediate")

prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}

print(" 1. Print products sorted alphabetically")
for product in sorted(prices):
    print(product)

print(" 2. Print products sorted by price (cheapest first)")
for product, price in sorted(prices.items(), key=lambda item: item[1]):
    print(product, price)

print(" 3. Find and print the most expensive item using items()")
most_expensive = max(prices.items(), key=lambda item: item[1])
print("Most expensive:", most_expensive[0], most_expensive[1])

print ("Advanced")

temps = {"Mon": 72, "Tue": 68, "Wed": 75, "Thu": 80, "Fri": 65}

print(" 1. Calculate average temperature using values()")
average = sum(temps.values()) / len(temps)
print("Average temperature:", average)

print(" 2. Find hottest and coldest days in a single loop")
hottest_day = coldest_day = None
hottest_temp = float("-inf")
coldest_temp = float("inf")

for day, temp in temps.items():
    if temp > hottest_temp:
        hottest_temp = temp
        hottest_day = day

    if temp < coldest_temp:
        coldest_temp = temp
        coldest_day = day

print("Hottest:", hottest_day, hottest_temp)
print("Coldest:", coldest_day, coldest_temp)

print(" 3. Count how many days were above the average")
above_average = sum(1 for temp in temps.values() if temp > average)
print("Days above average:", above_average)

print("Unit 3.2: Advanced Iteration & Nested Dictionaries")
products = {
    "laptop": {"price": 999, "stock": 15},
    "phone": {"price": 699, "stock": 50}
}

print(" 1. Print the laptop's price")
print("Laptop price:", products["laptop"]["price"])

print(" 2. Print each product with its stock level")
for product, details in products.items():
    print(product, "stock:", details["stock"])

print("intermediate")

print(" 1. Create a dictionary using zip()")
countries = ["USA", "Canada", "Mexico"]
capitals = ["Washington", "Ottawa", "Mexico City"]

country_capitals = dict(zip(countries, capitals))
print(country_capitals)


print(" 2. Add a new product to products")
products = {
    "laptop": {"price": 999, "stock": 15},
    "phone": {"price": 699, "stock": 50}
}

products["tablet"] = {"price": 449, "stock": 30}
print(products)


print(" 3. Safely remove all products with stock < 20")
# Use a list of keys so the dictionary isn't changed while iterating over it.
for product in list(products):
    if products[product]["stock"] < 20:
        del products[product]

print(products)

print("Advanced")

company = {
    "Engineering": {"Alice": 95000, "Bob": 85000},
    "Marketing": {"Carol": 75000, "Dave": 70000}
}

print(" 1. Print all employees with their salaries (nested iteration)")
for department, employees in company.items():
    print(department)
    for employee, salary in employees.items():
        print(" ", employee, salary)

print(" 2. Calculate the average salary per department")
for department, employees in company.items():
    average = sum(employees.values()) / len(employees)
    print(department, "average salary:", average)

print(" 3. Find the highest-paid employee across all departments")
highest_employee = None
highest_salary = 0

for department, employees in company.items():
    for employee, salary in employees.items():
        if salary > highest_salary:
            highest_salary = salary
            highest_employee = employee

print("Highest-paid employee:", highest_employee, highest_salary)

print("Unit 3.3: Dictionary Patterns & Transformations")
print("Beginner")

print(" 1. Map numbers 1-5 to their cubes using dictionary comprehension")
cubes = {num: num ** 3 for num in range(1, 6)}
print(cubes)


print(" 2. Convert Fahrenheit temperatures to Celsius using dictionary comprehension")
temps = {"Mon": 72, "Tue": 68, "Wed": 75}

celsius = {day: (temp - 32) * 5 / 9 for day, temp in temps.items()}
print(celsius)

print(" intermediate")
scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}

print(" 1. Create passing dict with only scores >= 70")
passing = {student: score for student, score in scores.items() if score >= 70}
print(passing)


print(" 2. Create letter_grades dict")
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

letter_grades = {student: get_grade(score) for student, score in scores.items()}
print(letter_grades)


print(" 3. Invert student_ids to look up by ID")
student_ids = {"Alice": 101, "Bob": 102}

ids_to_students = {student_id: student for student, student_id in student_ids.items()}
print(ids_to_students)

print("Unit 1: Set Theory and Python Sets ")
print("Beginner")

print(" 1. Create a set of vowels")
vowels = {"a", "e", "i", "o", "u"}
print(vowels)

print(" 2. Create a set from the list")
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

unique_numbers = set(numbers)
print(unique_numbers)
print("Number of elements:", len(unique_numbers))
print("A set automatically removes duplicate values.")

print(". What's wrong with empty =?")
print("This is a syntax error because = needs a value on the right side.")

print(" intermediate")
print("part 1")
text = "mississippi"

unique_characters = set(text)

print(unique_characters)
print("Number of unique letters:", len(unique_characters))

print("part 2")
emails = ["a@b.com", "c@d.com", "a@b.com", "e@f.com", "c@d.com"]

unique_emails = list(set(emails))

print(unique_emails)

print("part 3")
print("Why does this fail? s = {[1, 2], [3, 4]}")
print("This fails because lists are mutable and unhashable, so they cannot be added to a set.")

print ("Advanced")
print("part 1")
import time

numbers_list = list(range(1_000_000))
numbers_set = set(numbers_list)

# Check in list
start = time.time()
999999 in numbers_list
list_time = time.time() - start

# Check in set
start = time.time()
999999 in numbers_set
set_time = time.time() - start

print("List lookup:", list_time)
print("Set lookup:", set_time)

print("part 2")
permissions = frozenset({"read", "write"})

roles = {
    permissions: "Admin"
}

print(roles[permissions])

print("part 3")

edges = [(1, 2), (2, 3), (1, 3), (3, 4)]

nodes = set()

for edge in edges:
    nodes.update(edge)

print(nodes)

print("Unit 2: Set Operations")
print("Beginner")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(" 1. Union - all unique numbers")
union = a | b
print("Union:", union)

print(" 2. Intersection - numbers in both sets")
intersection = a & b
print("Intersection:", intersection)

print(" 3. Difference - numbers only in set a")
difference = a - b
print("Difference:", difference)


print(" intermediate")
morning_shift = {"Alice", "Bob", "Carol"}
evening_shift = {"Carol", "Dave", "Eve"}
weekend_shift = {"Alice", "Eve", "Frank"}

print(" 1. Employees who work ALL shifts")
all_shifts = morning_shift & evening_shift & weekend_shift
print("All shifts:", all_shifts)

print(" 2. Employees who work at least one shift")
any_shift = morning_shift | evening_shift | weekend_shift
print("At least one shift:", any_shift)

print(" 3. Employees who ONLY work morning")
only_morning = morning_shift - evening_shift - weekend_shift
print("Only morning:", only_morning)

print(" 4. Employees who work exactly one shift")
all_employees = morning_shift | evening_shift | weekend_shift

exactly_one = {
    employee for employee in all_employees
    if sum(employee in shift for shift in
           [morning_shift, evening_shift, weekend_shift]) == 1
}

print("Exactly one shift:", exactly_one)

print("Advanced")
prereqs_met = {"Alice", "Bob", "Carol", "Dave"}
has_space = {"Bob", "Carol", "Eve", "Frank"}
paid_tuition = {"Alice", "Carol", "Eve"}

print(" 1. Students eligible to enroll (must meet ALL three criteria)")
eligible = prereqs_met & has_space & paid_tuition
print("Eligible:", eligible)

print(" 2. Students who met prereqs but haven't paid tuition")
unpaid = prereqs_met - paid_tuition
print("Met prereqs but haven't paid:", unpaid)

print(" 3. Students who need to meet prereqs OR pay tuition")
# Consider everyone mentioned in any of the sets.
all_students = prereqs_met | has_space | paid_tuition

needs_action = {
    student for student in all_students
    if student not in prereqs_met or student not in paid_tuition
}

print("Need to meet prereqs or pay tuition:", needs_action)

print("Unit 3: Set Methods, Comprehensions & Patterns")
print("Beginner")

print("1. Add and remove elements")
numbers = {1, 2, 3}

numbers.add(4)
numbers.remove(1)

print(numbers)

print("2. Set comprehension for even numbers from 0–20")
even_numbers = {x for x in range(21) if x % 2 == 0}

print(even_numbers)

print("3. discard() vs remove()")
numbers = {1, 2, 3}


numbers.discard(5)
print(numbers)

numbers = {1, 2, 3}

if 5 in numbers:
    numbers.remove(5)

print(numbers)

print("Intermediate")
print(" part 1" )
numbers = [4, 5, 2, 4, 8, 5, 2, 1, 9, 4]

seen = set()
unique_numbers = []

for number in numbers:
    if number not in seen:
        seen.add(number)
        unique_numbers.append(number)

print(unique_numbers)

print(" part 2" )
sentence = "To be or not to be that is the question"

unique_words = {word.lower() for word in sentence.split()}

print(unique_words)

print(" part 3" )
expected = set(range(1, 11))  # 1 through 10
actual = {1, 2, 4, 5, 7, 8, 10}

missing = expected - actual

print("Missing numbers:", missing)

print("Advanced")
print(" part 1" )
def find_duplicates(lst):
    seen = set()
    duplicates = set()

    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return duplicates


print(find_duplicates([1, 2, 2, 3, 3, 3, 4]))

print(" part 2" )
alice = {"Python", "SQL", "Excel", "Tableau"}
bob = {"Python", "Java", "SQL", "AWS"}
carol = {"Python", "R", "SQL", "Tableau"}

print("1. Skills that ALL three have")
all_three = alice & bob & carol
print("All three have:", all_three)

print("2. Skills that ONLY Alice has")
only_alice = alice - bob - carol
print("Only Alice has:", only_alice)

print("3. All unique skills across the team")
all_skills = alice | bob | carol
print("All unique skills:", all_skills)

print(" part 3" )
def common_chars(str1, str2):
    return set(str1) & set(str2)

print(common_chars("hello", "world"))
