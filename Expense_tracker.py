# 🚀 Day 4 Mini Project — Expense Tracker (CLI)

# Problem Statement:
# Create a Python program called "Expense Tracker"
# that allows a user to record and analyze their daily expenses.

# This program should help users keep track of where their money goes.


# ------------------------------------------------------------
# Task 1 — Add Expense
# Create a function that allows the user to enter:
# 1. Expense Category (Food, Transport, Shopping, Bills, etc.)
# 2. Amount spent
#
# Store each expense in a list.


# Example:
# Category: Food
# Amount: 250

# Category: Transport
# Amount: 120


# ------------------------------------------------------------
# Task 2 — Menu System
# Display a menu repeatedly until the user chooses to exit.

# Menu:
# 1. Add Expense
# 2. View All Expenses
# 3. Show Total Spending
# 4. Show Highest Expense
# 5. Exit


# ------------------------------------------------------------
# Task 3 — View All Expenses
# Display all expenses entered by the user.

# Example Output:
# Food : Rs250
# Transport : Rs120
# Shopping : Rs800


# ------------------------------------------------------------
# Task 4 — Calculate Total Spending
# Add all expenses together and display the total amount spent.

# Example:
# Total Spending: Rs1170


# ------------------------------------------------------------
# Task 5 — Find Highest Expense
# Display the highest expense recorded.

# Example:
# Highest Expense: Shopping - Rs800


# ------------------------------------------------------------
# Task 6 — Exit
# End the program.

# Example Output:
# Thank you for using the Expense Tracker


# ------------------------------------------------------------
# ⭐ Bonus Challenge (Optional)

# 1. Store expenses as a list of dictionaries.
# Example:
# {"category": "Food", "amount": 250}

# 2. Display spending per category.

# Example:
# Food Total: Rs450
# Transport Total: Rs200


# ------------------------------------------------------------
# Concepts Practiced:

# - functions
# - lists
# - dictionaries
# - loops
# - conditional statements
# - basic data aggregation
# - menu-driven CLI programs



expense_list = []
Amount = 0
#Option - 1
def add_expense():
    global Amount
    print("Choose The Category : ")
    print("1.Food \n2.Transport \n3.Shopping \n4.Bills \n5.Others")
    print(" ")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        amt_f= int(input("Enter The Amount : Rs"))
        print(f"Category - Food\nAmount = {amt_f}")
        print(" ")
        temp_f = ["Food",amt_f]
        expense_list.append(temp_f)
        Amount = Amount+amt_f
    elif choice == 2:
        amt_t = int(input("Enter The Amount : Rs"))
        print(f"Category - Transport\nAmount = {amt_t}")
        print(" ")
        temp_t = ["Transport",amt_t]
        expense_list.append(temp_t)
        Amount = Amount+amt_t
    elif choice == 3:
        amt_s = int(input("Enter The Amount : Rs"))
        print(f"Category - Shopping\nAmount = {amt_s}")
        print(" ")
        temp_s = ["Shopping",amt_s]
        expense_list.append(temp_s)
        Amount = Amount+amt_s
    elif choice == 4:
        amt_b = int(input("Enter The Amount : Rs"))
        print(f"Category - Bills\nAmount = {amt_b}")
        print(" ")
        temp_b = ["Bill",amt_b]
        expense_list.append(temp_b)
        Amount = Amount+amt_b
    elif choice == 5:
        amt_cat = int(input("Enter The Amount : Rs"))
        other_category = input("Enter the Category Name : ")
        print(f"Category - {other_category}\nAmount = {amt_cat}")
        print(" ")
        temp_cat = [other_category,amt_cat]
        expense_list.append(temp_cat)
        Amount = Amount+amt_cat
    else :
        print("Invalid Choice...Retry Again")


#Option - 2
def view_all_expenses ():
    for exp in expense_list:
        print(f"Category - {exp[0]} Amount {exp[1]}")

#Option - 3
def total_spendings():
    print(f"The Total Amount Spend is : Rs{Amount}")

#Option - 4
def highest_expense():
    length = len(expense_list)
    max = 0
    for i in range(length):
        if expense_list[i][1]>max :
            max = expense_list[i][1]
            cat = expense_list[i][0]
    print(f"The highest expense is {cat} and the amount spend is Rs{max}")


while(True):
    print("1.Add Expense\n2.View All Expenses\n3.Show Total Spending\n4.Show Highest Expense\n5.Exit")
    option = int(input("Enter The Category You Want : "))
    print(" ")
    if option == 1:
        add_expense()
        print(" ")
    elif option == 2:
        view_all_expenses()
        print(" ")
    elif option == 3:
        total_spendings()
        print(" ")
    elif option == 4:
        highest_expense()
        print(" ")
    elif option == 5:
        break
    else :
        print("Invalid Choice...Retry")
        print(" ")

