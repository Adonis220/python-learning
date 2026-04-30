num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

for num in num_list:
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
        

n = 6
row_list = []

for x in range(1, n + 1):
    row = []
    for y in range(1, n + 1):
        row.append(x * y)
    row_list.append(row)

for row in row_list:
    print(row)


balance = 1000
history = []

while True:
    print("""
1. Check balance 
2. Deposit 
3. Withdraw 
4. Show transaction history
5. Quit
""")

    banking_input = input("Enter a valid number: ")

    if banking_input == "1":
        print("Balance:", balance)

    elif banking_input == "2":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        history.append(f"Deposited: {amount}")
        print("Deposit successful.")

    elif banking_input == "3":
        amount = float(input("Enter withdrawal amount: "))
        if amount > balance:
            print("Insufficient funds.")
        else:
            balance -= amount
            history.append(f"Withdrew: {amount}")
            print("Withdrawal successful.")

    elif banking_input == "4":
        if not history:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for item in history:
                print(item)

    elif banking_input == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid input.")
    
    

       


 


