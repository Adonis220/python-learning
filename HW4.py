#problem 1 
'''
# Movie Ticket Pricing Program

age = int(input("Enter your age: "))

# Validate age
if age < 0:
    print("Error: Age cannot be negative.")
else:
    matinee_input = input("Is this a matinee showing? (yes/no): ").strip().lower()

    # Ternary operator to convert input to Boolean
    is_matinee = True if matinee_input == "yes" else False

    # Determine price using nested if statements
    if age < 13:
        age_group = "Child"
        price = 6.00 if is_matinee else 8.00

    elif 13 <= age <= 17:
        age_group = "Teen"
        price = 7.00 if is_matinee else 10.00

    elif 18 <= age <= 64:
        age_group = "Adult"
        price = 8.00 if is_matinee else 13.00

    else:
        age_group = "Senior"
        price = 6.00 if is_matinee else 7.00

    # Output results
    print(f"Age group: {age_group}")
    print(f"Ticket price: ${price:.2f}")

#peoblem 2 
# Student Profile Validator

errors = []

student_id = input("Enter student ID: ").strip()
name = input("Enter full name: ").strip()
age_input = input("Enter age: ").strip()
major = input("Enter major: ").strip().upper()

# ---------------- Student ID validation ----------------
if len(student_id) != 8:
    errors.append(f"Student ID must be exactly 8 characters (got {len(student_id)})")

if len(student_id) >= 1 and not student_id[0].isalpha():
    errors.append("Student ID must start with a letter")

if len(student_id) == 8 and not student_id[1:].isdigit():
    errors.append("Last 7 characters of Student ID must be digits")

# ---------------- Name validation ----------------
if len(name.strip()) < 2:
    errors.append("Name cannot be empty and must be at least 2 characters")

# ---------------- Age validation ----------------
try:
    age = int(age_input)
    if age < 16 or age > 99:
        errors.append("Age must be between 16 and 99 (inclusive)")
except ValueError:
    errors.append("Age must be a valid integer")

# ---------------- Major validation ----------------
valid_majors = ["CS", "IT", "CE", "DS"]
if major not in valid_majors:
    errors.append(f"Major must be one of: CS, IT, CE, DS (got {major})")

# ---------------- Output ----------------
if errors:
    print("✗ Profile has errors:")
    for e in errors:
        print("-", e)
else:
    print("✓ Profile created successfully!")
    print(f"Student ID: {student_id}")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Major: {major}")
'''
# problem 3 

# Campus Café Menu System

print("==============================")
print("CAMPUS CAFÉ ORDER SYSTEM")
print("==============================")

print("1. Coffee - $3.50")
print("2. Sandwich - $6.00")
print("3. Salad - $5.50")
print("4. Combo - $8.00")
print("5. Exit")
print("==============================")

choice = input("Enter your choice (1-5): ").strip()

if choice == "5":
    print("Goodbye!")
else:
    name = input("Enter your name: ").strip()

    if name == "":
        print("Error: Name cannot be empty.")
    else:
        try:
            quantity = int(input("How many? ").strip())
            if quantity <= 0:
                print("Error: Quantity must be a positive integer.")
            else:

                item = ""
                unit_price = 0.0

                # ---------------- Coffee ----------------
                if choice == "1":
                    item = "Coffee"
                    size = input("Size (small/medium/large): ").strip().lower()

                    if size == "medium":
                        unit_price = 4.50
                        item += " (Medium)"
                    elif size == "large":
                        unit_price = 5.50
                        item += " (Large)"
                    elif size == "small":
                        unit_price = 3.50
                        item += " (Small)"
                    else:
                        unit_price = 3.50
                        item += " (Small - default, invalid size)"

                # ---------------- Sandwich ----------------
                elif choice == "2":
                    item = "Sandwich"
                    cheese = input("Add cheese? (yes/no): ").strip().lower()

                    if cheese == "yes":
                        unit_price = 6.75
                        item += " + Cheese"
                    else:
                        unit_price = 6.00
                        item += " (no cheese)"

                # ---------------- Salad ----------------
                elif choice == "3":
                    item = "Salad"
                    dressing = input("Choose dressing (ranch/italian/vinaigrette/none): ").strip().lower()

                    if dressing in ["ranch", "italian", "vinaigrette", "none"]:
                        unit_price = 5.50
                        item += f" ({dressing})"
                    else:
                        unit_price = 5.50
                        item += " (no dressing - default)"

                # ---------------- Combo ----------------
                elif choice == "4":
                    item = "Combo (Sandwich + Coffee)"

                    # Sandwich part
                    cheese = input("Add cheese to sandwich? (yes/no): ").strip().lower()
                    sandwich_price = 6.75 if cheese == "yes" else 6.00

                    # Coffee part
                    size = input("Coffee size (small/medium/large): ").strip().lower()
                    if size == "medium":
                        coffee_price = 4.50
                    elif size == "large":
                        coffee_price = 5.50
                    else:
                        coffee_price = 3.50

                    unit_price = sandwich_price + coffee_price

                else:
                    print("Invalid menu choice.")

                # ---------------- Receipt ----------------
                if choice in ["1", "2", "3", "4"]:
                    subtotal = unit_price * quantity
                    tax = subtotal * 0.07
                    total = subtotal + tax

                    print("==============================")
                    print("ORDER RECEIPT")
                    print("==============================")
                    print(f"Customer: {name}")
                    print(f"Item: {item}")
                    print(f"Quantity: {quantity}")
                    print(f"Unit Price: ${unit_price:.2f}")
                    print(f"Subtotal: ${subtotal:.2f}")
                    print(f"Tax (7%): ${tax:.2f}")
                    print(f"Total: ${total:.2f}")
                    print("==============================")
                    print("Thank you for your order!")
        except ValueError:
            print("Error: Quantity must be a valid integer.")