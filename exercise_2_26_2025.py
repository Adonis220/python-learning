#unt 1 exercises 

#exercise 1 (beginner)
groceries = []
groceries.append("milk")
groceries.append("eggs")
groceries.append("bread")
print(groceries)

#exercise 2 (intermediate)
numbers = [10, 30, 40]
numbers.insert(1, 20)
numbers.insert(0, 5)
numbers.append(50)
numbers.extend([60, 70, 80])
print(numbers)

#exercise 3 (advanced)
# Case 1:
a = [1, 2]
a.append([3, 4])
# What is a? [1, 2, [3, 4]]
# Case 2:
b = [1, 2]
b.extend([3, 4])
# What is b? [1, 2, 3, 4]
# Case 3:
c = [1, 2]
c.append("hi")
# What is c? [1, 2, 'hi']
# Case 4:
d = [1, 2]
d.extend("hi")
# What is d? [1, 2, 'h', 'i']

# Now run the code and check your predictions.
# Write a comment explaining why Case 3 and Case 4 differ. 
#Case 3 and 4 are diffrent because 3 is a string and 4 is a list. 

#unit 2 exercises
#exercise 1 (beginner)
animals = ["cat", "dog", "bird", "dog", "fish"]
animals.remove("bird")
animals.pop(3)
print(animals)

#exercise 2 (intermediate)
queue = ["Alice", "Bob", "Charlie", "David", "Eve"]
#remove david
queue.remove("David")
print
#serve first person in line and remove from queue
print(queue[0] + " was served")
queue.pop(0)
print(queue)
#last person gives up and leaves the queue
queue.pop(-1)
print(queue)

#exercise 3 (advanced)
scores = [85, 92, 78, 64, 95, 88]

# 1. Safely try to remove the value 100 from scores.
# If it is not in the list, print "100 not found."
if 100 in scores:
    scores.remove(100)
else:
    print("100 not found")

# 2. Safely try to pop index 10.
# If the index is out of range, print an appropriate message.
if 10 in scores:
    scores.pop(scores.index(10))
else:
    print("index 10 not in range")

#score check before deleting middle 2 elements
print(scores)

# 3. Delete the middle two elements using del with a slice.
# (Calculate the indices based on the list length.)
length = len(scores)
mid = length // 2
del scores[mid-1:mid+1]

# 4. Print the final list.
print(scores)

#mini unit 3 exercises
#exercise 1 (beginner)

colors = ["red", "blue", "green", "yellow", "blue"]

# 1. Check if "blue" is in the list. Print the result.
if "blue" in colors:
    print("blue is in the list")

# 2. Check if "purple" is NOT in the list. Print the result.
if "purple" not in colors:
    print("purple is NOT in the list")

# 3. Find the index of "green". Print it.
if "green" in colors:
    print("green is at index", colors.index("green"))

# 4. Count how many times "blue" appears. Print the count.
blue_count = colors.count("blue")
print("blue appears", blue_count, "times")

#exercise 2 (intermediate)
students = ["Alice", "Bob", "Charlie", "David", "Alice"]

# 1. Ask the user to type a student name (use input()).
name = input("Enter a student name: ")
# 2. Print the index of their first occurrence.
if name in students:
    print(name, "is at index", students.index(name))
    # - Print how many times their name appears.
    count = students.count(name)
    print(name, "appears", count, "times")
# 3. If the name is NOT in the list:
#- Print a message: "[name] is not enrolled."
else:
    print(name, "is not in enrolled")

#exercise 3 (advanced)
inventory = ["hammer", "nails", "screwdriver", "nails", "wrench", "nails"]

# 1. Count how many "nails" are in inventory. Print the count.
nail_count = inventory.count("nails")
print("There are", nail_count, "nails in inventory.")
# 2. Find the index of the first "nails". Print it.
nail_index = inventory.index("nails")
if "nails" in inventory:
    print("The first 'nails' is at index", nail_index)
    # 3. Remove the first "nails" using remove().
    inventory.remove("nails")

# 4. Find the index of the next "nails" (it moved!). Print it.
if "nails" in inventory:
    print("The next 'nails' is at index", inventory.index("nails"))
    remove_index = inventory.index("nails")
#final nail check
if nail_count == 0:
    print("No nails in inventory")
else:
    print(nail_count, "nails in inventory")


