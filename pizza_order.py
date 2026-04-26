"""
# ============================================
# PIZZA ORDER SYSTEM
# CS 1300 — Lecture 6 Lab
# ============================================
# ----- Menu Data (do not modify) -----
sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
size_prices = [6.99, 9.99, 12.99, 16.99]
topping_names = ["Pepperoni", "Mushrooms", "Green Peppers", "Onions",
"Sausage", "Bacon", "Extra Cheese", "Pineapple"]
topping_price = 1.50 # each topping, any size
# ----- Order Storage -----
order_descriptions = [] # e.g., "Large Pepperoni, Mushrooms"
order_prices = [] # e.g., 15.99
# Your code goes below this line.


# EXERCISE 1 — Display the size menu
# EXERCISE 1 — Display the size menu

print("==============================")
print("PIZZA SIZES")
print("==============================")

for i in range(len(sizes)):
    print(f"{i + 1}. {sizes[i]} ${size_prices[i]:>5.2f}")

print("==============================")

# EXERCISE 2 — Get a valid size choice

while True:
    user_input = input("Pick a size (1-4): ")

    # Check if input is an integer
    if not user_input.isdigit():
        print("Please enter a number!")
        continue

    size_choice = int(user_input) - 1  # convert to 0-based index

    # Check valid range
    if size_choice < 0 or size_choice >= len(sizes):
        print("Choose 1-4.")
        continue

    # Valid input → break loop
    break

# Set base price
base_price = size_prices[size_choice]

# EXERCISE 3 — Add toppings

selected_toppings = []

# Display available toppings using a for loop
print("Available toppings ($1.50 each):")
for i in range(len(topping_names)):
    print(f"{i + 1}. {topping_names[i]}")

# Topping selection loop (sentinel: "done")
while True:
    user_input = input("Add topping # (or 'done'): ")

    # Sentinel check
    if user_input.lower() == "done":
        break

    # Validate numeric input
    if not user_input.isdigit():
        print("Please enter a number or 'done'!")
        continue

    topping_index = int(user_input) - 1

    # Range check
    if topping_index < 0 or topping_index >= len(topping_names):
        print("Invalid topping number.")
        continue

    topping = topping_names[topping_index]

    # Duplicate check
    if topping in selected_toppings:
        print(f"Already added {topping}!")
        continue

    # Add topping
    selected_toppings.append(topping)
    print(f"✓ Added {topping}")

    # EXERCISE 4 — Calculate price and store the pizza

# Calculate total price
total_price = base_price + (len(selected_toppings) * topping_price)

# Build description string
# Start with size name
pizza_description = sizes[size_choice]

# Add toppings if any exist
if len(selected_toppings) > 0:
    pizza_description += " " + ", ".join(selected_toppings)

# Store in order lists
order_descriptions.append(pizza_description)
order_prices.append(total_price)

# EXERCISE 5 — Wrap everything in a multi-pizza loop

while True:

    # ------------------------------
    # Exercise 1 — Display menu
    # ------------------------------
    print("==============================")
    print("PIZZA SIZES")
    print("==============================")

    for i in range(len(sizes)):
        print(f"{i + 1}. {sizes[i]} ${size_prices[i]:>5.2f}")

    print("==============================")

    # ------------------------------
    # Exercise 2 — Choose size
    # ------------------------------
    while True:
        user_input = input("Pick a size (1-4): ")

        if not user_input.isdigit():
            print("Please enter a number!")
            continue

        size_choice = int(user_input) - 1

        if size_choice < 0 or size_choice >= len(sizes):
            print("Choose 1-4.")
            continue

        break

    base_price = size_prices[size_choice]

    # ------------------------------
    # Exercise 3 — Add toppings
    # ------------------------------
    selected_toppings = []

    print("Available toppings ($1.50 each):")
    for i in range(len(topping_names)):
        print(f"{i + 1}. {topping_names[i]}")

    while True:
        user_input = input("Add topping # (or 'done'): ")

        if user_input.lower() == "done":
            break

        if not user_input.isdigit():
            print("Please enter a number or 'done'!")
            continue

        topping_index = int(user_input) - 1

        if topping_index < 0 or topping_index >= len(topping_names):
            print("Invalid topping number.")
            continue

        topping = topping_names[topping_index]

        if topping in selected_toppings:
            print(f"Already added {topping}!")
            continue

        selected_toppings.append(topping)
        print(f"✓ Added {topping}")

    # ------------------------------
    # Exercise 4 — Calculate price
    # ------------------------------
    total_price = base_price + (len(selected_toppings) * topping_price)

    pizza_description = sizes[size_choice]

    if len(selected_toppings) > 0:
        pizza_description += " " + ", ".join(selected_toppings)

    order_descriptions.append(pizza_description)
    order_prices.append(total_price)

    # ------------------------------
    # Ask to order another pizza
    # ------------------------------
    while True:
        again = input("Order another pizza? (yes/no): ").lower()

        if again in ["yes", "y"]:
            break  # continue outer loop

        elif again in ["no", "n"]:
            # Exit both loops
            print("Order complete!")
            print(order_descriptions)
            print(order_prices)
            exit()

        else:
            print("Please enter yes or no.")
            continue

# EXERCISE 6 — Print receipt

print("====================================")
print("YOUR ORDER RECEIPT")
print("====================================")

subtotal = 0

# List each pizza
for i in range(len(order_descriptions)):
    print(f"{i + 1}. {order_descriptions[i]}")
    print(f"${order_prices[i]:>6.2f}")
    subtotal += order_prices[i]

print("------------------------------------")

# Calculate tax and total
tax = subtotal * 0.07
total = subtotal + tax

# Print totals (right-aligned)
print(f"Subtotal: ${subtotal:>6.2f}")
print(f"Tax (7%): ${tax:>6.2f}")
print(f"Total:    ${total:>6.2f}")

print("====================================")
print("Thank you for your order!")

# EXERCISE 7 — Find the most expensive pizza

if len(order_prices) > 0:

    max_price = order_prices[0]
    max_index = 0

    for i in range(len(order_prices)):
        if order_prices[i] > max_price:
            max_price = order_prices[i]
            max_index = i

    print("------------------------------------")
    print("Most Expensive Pizza:")
    print(f"{order_descriptions[max_index]}")
    print(f"${max_price:>6.2f}")

    # EXERCISE 8 — Discount code with attempt limit

discount = 0
attempts = 0

while True:
    code = input("Enter discount code (or 'none'): ").upper()

    # Skip discount
    if code == "NONE":
        print("No discount applied.")
        break

    # Valid codes
    if code == "STUDENT10":
        discount = 0.10
        break
    elif code == "HALFOFF":
        discount = 0.50
        break

    # Invalid code handling
    attempts += 1
    print("Invalid code.")

    if attempts >= 3:
        print("No discount applied.")
        break

# EXERCISE 9 — Count pizzas by size

personal_count = 0
medium_count = 0
large_count = 0
party_count = 0

for description in order_descriptions:

    if "Personal" in description:
        personal_count += 1
    elif "Medium" in description:
        medium_count += 1
    elif "Large" in description:
        large_count += 1
    elif "Party" in description:
        party_count += 1

print("------------------------------------")
print("PIZZA SIZE SUMMARY")
print("------------------------------------")
print(f"Personal (8\"): {personal_count}")
print(f"Medium (12\"):   {medium_count}")
print(f"Large (16\"):    {large_count}")
print(f"Party (20\"):    {party_count}")
print("====================================")
"""

# ============================================
# PIZZA ORDER SYSTEM — FINAL CLEAN VERSION
# ============================================

sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
size_prices = [6.99, 9.99, 12.99, 16.99]

topping_names = [
    "Pepperoni", "Mushrooms", "Green Peppers", "Onions",
    "Sausage", "Bacon", "Extra Cheese", "Pineapple"
]

topping_price = 1.50

order_descriptions = []
order_prices = []

print("====================================")
print("WELCOME TO PYTHON PIZZA!")
print("====================================")

# ============================================
# ORDER LOOP
# ============================================
while True:

    # ---------------- SIZE MENU ----------------
    print("\n==============================")
    print("PIZZA SIZES")
    print("==============================")

    for i in range(len(sizes)):
        print(f"{i + 1}. {sizes[i]} ${size_prices[i]:>5.2f}")

    print("==============================")

    # ---------------- SIZE CHOICE ----------------
    while True:
        user_input = input("Pick a size (1-4): ")

        if not user_input.isdigit():
            print("Please enter a number!")
            continue

        size_choice = int(user_input) - 1

        if size_choice < 0 or size_choice >= len(sizes):
            print("Choose 1-4.")
            continue

        break

    base_price = size_prices[size_choice]

    # ---------------- TOPPINGS ----------------
    selected_toppings = []   # MUST reset each pizza

    print("\nAvailable toppings ($1.50 each):")
    for i in range(len(topping_names)):
        print(f"{i + 1}. {topping_names[i]}")

    while True:
        user_input = input("Add topping # (or 'done'): ")

        if user_input.lower() == "done":
            break

        if not user_input.isdigit():
            print("Please enter a number or 'done'!")
            continue

        topping_index = int(user_input) - 1

        if topping_index < 0 or topping_index >= len(topping_names):
            print("Invalid topping number.")
            continue

        topping = topping_names[topping_index]

        if topping in selected_toppings:
            print(f"Already added {topping}!")
            continue

        selected_toppings.append(topping)
        print(f"✓ Added {topping}")

    # ---------------- PRICE ----------------
    total_price = base_price + (len(selected_toppings) * topping_price)

    pizza_description = sizes[size_choice]
    if selected_toppings:
        pizza_description += " " + ", ".join(selected_toppings)

    order_descriptions.append(pizza_description)
    order_prices.append(total_price)

    # ---------------- ORDER AGAIN ----------------
    while True:
        again = input("Order another pizza? (yes/no): ").lower()

        if again in ["yes", "y"]:
            break
        elif again in ["no", "n"]:
            break
        else:
            print("Please enter yes or no.")

    if again in ["no", "n"]:
        break


# ============================================
# EMPTY ORDER CHECK
# ============================================
if len(order_descriptions) == 0:
    print("\nNo pizzas ordered!")

else:

    # ============================================
    # DISCOUNT (Exercise 8)
    # ============================================
    discount = 0
    attempts = 0

    while True:
        code = input("\nEnter discount code (or 'none'): ").upper()

        if code == "NONE":
            print("No discount applied.")
            break

        if code == "STUDENT10":
            discount = 0.10
            break
        elif code == "HALFOFF":
            discount = 0.50
            break

        attempts += 1
        print("Invalid code.")

        if attempts >= 3:
            print("No discount applied.")
            break

    # ============================================
    # RECEIPT (Exercise 6)
    # ============================================
    print("\n====================================")
    print("YOUR ORDER RECEIPT")
    print("====================================")

    subtotal = 0

    for i in range(len(order_descriptions)):
        print(f"{i + 1}. {order_descriptions[i]}")
        print(f"${order_prices[i]:>6.2f}")
        subtotal += order_prices[i]

    print("------------------------------------")

    discount_amount = subtotal * discount
    subtotal_after_discount = subtotal - discount_amount

    tax = subtotal_after_discount * 0.07
    total = subtotal_after_discount + tax

    print(f"Subtotal: ${subtotal:>6.2f}")
    print(f"Discount: -${discount_amount:>6.2f}")
    print(f"Tax (7%): ${tax:>6.2f}")
    print(f"Total:    ${total:>6.2f}")

    print("====================================")

    # ============================================
    # MOST EXPENSIVE (Exercise 7)
    # ============================================
    max_price = order_prices[0]
    max_index = 0

    for i in range(len(order_prices)):
        if order_prices[i] > max_price:
            max_price = order_prices[i]
            max_index = i

    print("Most Expensive Pizza:")
    print(order_descriptions[max_index])
    print(f"${max_price:>6.2f}")

    # ============================================
    # SIZE SUMMARY (Exercise 9)
    # ============================================
    personal = medium = large = party = 0

    for desc in order_descriptions:
        if "Personal" in desc:
            personal += 1
        elif "Medium" in desc:
            medium += 1
        elif "Large" in desc:
            large += 1
        elif "Party" in desc:
            party += 1

    print("------------------------------------")
    print("PIZZA SIZE SUMMARY")
    print("------------------------------------")
    print(f"Personal (8\"): {personal}")
    print(f"Medium (12\"):   {medium}")
    print(f"Large (16\"):    {large}")
    print(f"Party (20\"):    {party}")

    # ============================================
    # GOODBYE
    # ============================================
    print("\nThank you for your order! ")
    print("Come again soon!")


