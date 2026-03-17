# 🚀 Day 3 Mini Project — Simple Bank Account System

# Problem Statement:
# Create a Python program called "Simple Bank Account System"
# that allows a user to perform basic banking operations.

# ------------------------------------------------------------
# Task 1 — Create Account
# Ask the user to enter:
# 1. Account Holder Name
# 2. Initial Deposit Amount
#
# Store the information.
#
# Example:
# Account Holder: Rahul
# Balance: 5000

# ------------------------------------------------------------
# Task 2 — Banking Menu
# Display a menu repeatedly until the user chooses to exit.
#
# Menu:
# 1. Check Balance
# 2. Deposit Money
# 3. Withdraw Money
# 4. Exit
#
# Ask the user to choose an option.

# ------------------------------------------------------------
# Task 3 — Implement Operations

# 1️⃣ Check Balance
# Display the current balance.
#
# Example Output:
# Current Balance: 5000


# 2️⃣ Deposit Money
# Ask the user to enter the deposit amount.
# Add the amount to the balance.
#
# Example:
# Enter amount to deposit: 2000
# Deposit successful
# New Balance: 7000


# 3️⃣ Withdraw Money
# Ask the user to enter the withdrawal amount.
#
# Conditions:
# - If withdrawal amount is greater than balance:
#     print "Insufficient balance"
#
# - Otherwise subtract the amount from balance.
#
# Example:
# Withdrawal successful
# Remaining Balance: 3000


# 4️⃣ Exit
# End the program.
#
# Example Output:
# Thank you for using the bank system


# ------------------------------------------------------------
# ⭐ Bonus Challenge (Optional)
#
# Create a list called transaction_history.
# Store all transactions such as:
#
# Deposited 2000
# Withdrew 500
# Deposited 1000
#
# Add another menu option:
# 5. View Transaction History
#
# When the user selects this option, print all past transactions.

# ------------------------------------------------------------
# Concepts Practiced:
# - while loops
# - if / elif / else
# - variables
# - lists
# - user input handling
# - basic banking logic





#Solution 
print("Create The Account")
print(" ")
name = input("Enter The Account Holder Name : ")
deposit_amt = int(input("Enter The Initial Deposit Amount : Rs"))
transactions = []
amount = deposit_amt
while(True):
    print("1. Check Balance \n2. Deposit Money \n3. Withdraw Money\n4. Exit\n5. View Transaction History")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        print(f"The Current Balance is : {amount}")
    elif choice == 2 :
        money_to_deposit = int(input("Enter The Amount To Deposit : Rs"))
        amount = amount+money_to_deposit
        print("Deposit Successful")
        temp_D = ["Deposit",money_to_deposit]
        transactions.append(temp_D)
        print(f"The Current Balance After Depositing is : Rs{amount}")
    elif choice == 3:
        amt_to_withdraw = int(input("Enter the amount to withdraw : Rs"))
        if amt_to_withdraw > amount :
            print("Withdraw Unsuccessful")
            print("Required Balance Unavailable")
        else :
            amount = amount - amt_to_withdraw
            print("Withdraw Successful")
            temp_W = ["Withdrawn",amt_to_withdraw]
            transactions.append(temp_W)
            print(f"The Available Balance After Withdrawl : Rs{amount}")
    elif choice == 4:
        print("Thanks For Using Our Services...")
        break
    elif choice == 5:
        print(transactions)
    else :
        print("Invalid Choice")
    

