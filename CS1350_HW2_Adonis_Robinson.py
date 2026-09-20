'''
1. Practice exercises of Unit 1.1, Unit 1.2, Unit 1.3 from Week 1 Lecture 1 lecture notes.

For each set 30 points, 5 for beginner, 10 for intermediate, 15 for advanced 

2. Practice exercises of Unit 2.1 Unit 2.2, Unit 2.3 from Week 1 Lecture 2 lecture notes.

For each set 30 points, 5 for beginner, 10 for intermediate, 15 for advanced 

Create CS1350_HW2_FirstName_LastName.py for the exercises. Check your code into your code repo, and paste the website URL to submit your homework assignment through Canvas.
Enter Web URL
'''
print("Unit 1.1: What Are Dictionaries?")
print("Beginner")

my_info = {"name": "Adonis", "age": 21, "Major": "Cybersecurity"}
print(my_info)

print("Intermediate")
print("part 1")

menu = {"burger": 5.99, "fries": 2.99, "soda": 1.99, "salad": 4.99}
print(menu)

print("part 2")
course_credits = {"CS1350": 3, "CS1360": 4, "CS1370": 3, "CS1380": 3}
print(course_credits)

print("Advanced")
weekly_temps= dict(monday=61, tuesday=62, wednesday=61, thursday=68, friday=70)
print(weekly_temps)

print("Unit 1.2: Accessing Dictionary Elements")

print("Beginner")
pet = {"name": "Buddy", "type": "dog", "age": 3}
print(pet["name"], pet["age"])

print("Intermediate")
if "color" in pet:
    print(pet["color"])
else:
    print("unknown")

print ("Advanced")
products = {"laptop": 999.99, "mouse": 29.99, "keyboard": 79.99}
product_name = input("Enter a product name: ")
if product_name in products: 
    print(f"The price of {product_name} is ${products[product_name]:.2f}")
else:
    print("Product not available.")

print("Unit 1.3: Modifying Dictionaries")
print("Beginner")
#empty diectionary
inventory = {}
# items added to the inventory dictionary
inventory['apples'] = 5
inventory['Eggs'] = 3
inventory['milk'] = 2
# my output. 
print(inventory)

print("Intermediate")
scores = {"Team A": 45, "Team B": 38}
print("Before update:", scores)
scores["Team B"] = 41
print("After update:", scores)
print("now poping Team A")
scores.pop("Team A")
print(scores)

print("Unit 2.1: How Dictionaries Work")
print("Beginner")
print("""
"student_name" # valid (reason:  It is a string, and strings are immutable/hashable, so they can be dictionary keys)
b) [1, 2, 3] # invalid (reason: It is a list, which is mutable and therefore unhashable.)
c) 100 # valid (reason: It is an integer, which is immutable and hashable.)
d) ("x", "y") # valid (reason:  It is a tuple containing hashable strings, so the tuple is hashable.)
e) {"a": 1} # invalid (reason:  It is a dictionary, which is mutable and unhashable.)
f) frozenset({1,2}) # valid (reason:  It is a frozenset, which is immutable and hashable.)
""")

print("Intermediate")
print("part 1")
# unfixed code: locations = {[40.7, -74.0]: "New York", [34.0, -118.2]: "Los Angeles"}
locations = {(40.7, -74.0): "New York", (34.0, -118.2): "Los Angeles"}
print(locations)

print("part 2")
print(" it will print {'a': 3, 'b': 4} and a len of 2")

print("part 3")

print("Hash value of my name:", hash("Adonis"))
print("Hash value of 100:", hash(100))

print("Advanced")
print ("part 1")

high_scores = {
    ("Alice", "Chess"): 950,
    ("Bob", "Tetris"): 1200,
    ("Charlie", "Pac-Man"): 1500
}

# Retrieve one score
print(high_scores[("Bob", "Tetris")])

print("part 2")
import time

# Create 100,000 elements
numbers = list(range(100000))
number_dict = {i: True for i in range(100000)}

# Element to search for
target = 99999

# Time list search
start = time.perf_counter()
target in numbers
list_time = time.perf_counter() - start

# Time dictionary search
start = time.perf_counter()
target in number_dict
dict_time = time.perf_counter() - start

# Print results
print("List search time:", list_time)
print("Dictionary search time:", dict_time)

if list_time < dict_time:
    print("List is faster by:", list_time - dict_time, "seconds")
else:
    print("Dictionary is faster by:", dict_time - list_time, "seconds")

print("Unit 2.2: The keys() and values() Methods")
print("Beginner")

temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}

# 1. Print all day names
print(temps.keys())

# 2. Print all temperatures
print(temps.values())

# 3. Print how many days
print(len(temps))

print("Intermediate")

temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}

# 1. Find and print the highest and lowest temperatures
print("Highest temperature:", max(temps.values()))
print("Lowest temperature:", min(temps.values()))

# 2. Check if "Friday" is in the dictionary
if "Friday" in temps:
    print("Friday is in the dictionary.")
else:
    print("Friday is not in the dictionary.")

# 3. Add Thursday only if it doesn't already exist
temps.setdefault("Thursday", 70)
print("After adding Thursday:", temps)

# 4. Demonstrate that dictionary views are dynamic
keys_view = temps.keys()
print("Keys before adding Friday:", keys_view)

temps["Friday"] = 80

print("Keys after adding Friday:", keys_view)

print("Advanced")
prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}

# 1. Calculate total value and average price
total = sum(prices.values())
average = total / len(prices)

print("Total value:", total)
print("Average price:", average)

# 2. Find most and least expensive items
most_expensive = max(prices.items(), key=lambda item: item[1])
least_expensive = min(prices.items(), key=lambda item: item[1])

print("Most expensive:", most_expensive[0], "-", most_expensive[1])
print("Least expensive:", least_expensive[0], "-", least_expensive[1])

# 3. Compare memory usage
keys_view = prices.keys()
keys_list = list(prices.keys())

print("Memory used by prices.keys():", keys_view.__sizeof__(), "bytes")
print("Memory used by list(prices.keys()):", keys_list.__sizeof__(), "bytes")

# prices.keys() returns a dynamic view, while list(prices.keys())
# creates a separate list containing all the keys.

# 4. Add 3 new products using update()
prices.update({
    "headphones": 199,
    "camera": 799,
    "speaker": 149
})

print("All products:")
for product, price in prices.items():
    print(product, "-", price)

print("Unit 2.3: The items() Method")
print("Beginner")

colors = {"apple": "red", "banana": "yellow", "grape": "purple"}

print("part 1")
for fruit, color in colors.items():
    print(fruit, "is", color)

print("part 2")
print("It will return [('apple', 'red'), ('banana', 'yellow'), ('grape', 'purple')]:")
print(list(colors.items()))

print("Intermediate")
print("part 1")
prices = {"coffee": 4.50, "tea": 3.00, "juice": 5.25}

for item, price in prices.items():
    tax_price = price * 1.10
    print(f"{item}: ${price:.2f} + tax = ${tax_price:.2f}")

print("part 2")
count = 0

for price in prices.values():
    if price > 4.00:
        count += 1

print(count)

print("part 3")
x = 10

y = 20

x, y = y, x

print("part 4")
numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

print(first)
print(middle)
print(last)

print("Advanced")
import time

scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}

# 1. Find the student with the highest score using items(), max(), and lambda
highest_student = max(scores.items(), key=lambda item: item[1])

print("Highest score:", highest_student)
# ('Carol', 92)


# 2. Create passed and failed dictionaries using iteration
passed = {}
failed = {}

for student, score in scores.items():
    if score >= 70:
        passed[student] = score
    else:
        failed[student] = score

print("Passed:", passed)
print("Failed:", failed)


# 3. Calculate the class average and each student's deviation
average = sum(scores.values()) / len(scores)

deviations = {}
for student, score in scores.items():
    deviations[student] = score - average

print("Class average:", average)
print("Deviations:", deviations)


# 4. Performance test: items() iteration vs keys() with lookup
large_scores = {f"Student{i}": i % 101 for i in range(50_000)}

iterations = 1_000

# Test items()
start = time.perf_counter()

for _ in range(iterations):
    total = 0
    for student, score in large_scores.items():
        total += score

items_time = time.perf_counter() - start


# Test keys() + dictionary lookup
start = time.perf_counter()

for _ in range(iterations):
    total = 0
    for student in large_scores.keys():
        total += large_scores[student]

keys_time = time.perf_counter() - start


print(f"items() time:       {items_time:.6f} seconds")
print(f"keys() + lookup:    {keys_time:.6f} seconds")
print(f"items() is faster by approximately "
      f"{keys_time / items_time:.2f}x")
