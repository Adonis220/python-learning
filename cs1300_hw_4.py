#hw section 3: 

#problem 1: movie ticket pricing
# asking for age and converting it to an integer
age = int(input("Enter your age: "))

# checking if matinee or not
matinee = input("Is this a matinee showing? (yes/no): ").lower()

# Determine age group and base pricing
if 0 <= age <= 12:
    age_group = "Child"
    if matinee == "yes":
        price = "$6.00"
    else:
        price = "$8.00"

elif 13 <= age <= 17:
    age_group = "Teen"
    if matinee == "yes":
        price = "$7.00"
    else:
        price = "$10.00"

elif 18 <= age <= 64:
    age_group = "Adult"
    if matinee == "yes":
        price = "$8.00"
    else:
        price = "$13.00"

elif age >= 65:
    age_group = "Senior"
    if matinee == "yes":
        price = "$6.00"
    else:
        price = "$7.00"

else:
    age_group = ""
    price = "Error"
    print("Invalid age entered.")
    print("Age must be a positive integer.")

print(f"Age group: {age_group}")
print(f"The ticket price is: {price}")


# Problem 2: Input Validator (With Detailed Errors)

errors = []

# 1. Collect all inputs
student_id = input("Enter student ID: ")
name = input("Enter full name: ")
age_input = input("Enter age: ")
major = input("Enter major: ")

# 2. Validate Student ID
if len(student_id) != 8:
    errors.append(f"Student ID must be exactly 8 characters (got {len(student_id)})")

if not student_id or not student_id[0].isalpha():
    errors.append("Student ID must start with a letter")

if len(student_id) >= 2 and not student_id[1:].isdigit():
    errors.append("Student ID must have 7 digits after the first letter")

# 3. Validate Name
if len(name.strip()) == 0:
    errors.append("Name cannot be empty")

# 4. Validate Age (using try/except)
try:
    age = int(age_input)
    if not (16 <= age <= 99):
        errors.append("Age must be between 16 and 99")
except ValueError:
    errors.append("Age must be a valid integer")

# 5. Validate Major
valid_majors = ["CS", "IT", "CE", "DS"]
if major.upper() not in valid_majors:
    errors.append(f"Major must be one of: CS, IT, CE, DS (got {major})")

# 6. Final Output
if len(errors) == 0:
    print(" Profile created successfully!")
    print(f"Student ID: {student_id}")
    print(f"Name: {name.strip()}")
    print(f"Age: {age}")
    print(f"Major: {major.upper()}")
else:
    print(" Profile has errors:")
    for error in errors:
        print(f"- {error}")


print("""
=============================
CAMPUS CAFÉ ORDER SYSTEM
==============================
1. Coffee - $3.50
2. Sandwich - $6.00
3. Salad - $5.50
4. Combo - $8.00
5. Exit
==============================
""")

menu_selection = input("Please select an item by entering the corresponding number: ")
if menu_selection == "1":
    coffee_size = input("Select coffee size (small/medium/large): ").lower()