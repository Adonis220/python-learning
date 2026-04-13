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
menu = input("Display menu: Y/N")
while menu == "Y":
    print("""
    ==============================
    PIZZA SIZES
    ==============================
    1. Personal (8") $6.99
    2. Medium (12") $9.99
    3. Large (16") $12.99
    4. Party (20") $16.99
    ==============================
    """)
    break






