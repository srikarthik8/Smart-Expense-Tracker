#Smart Expense Tracker

expenses = []
print("\n=====SMART EXPENSES TRACKER=====")

#Get the user's monthly budget
monthly_budget = float(input("Enter your monthly budget - "))

#Ask how many expenses user wants to add
number_of_expenses = int(input("How many expenses you wants to add?"))

#Get expense details
for i in range(number_of_expenses):
    print("\nexpense,i+1")

    category = str(input("Enter category (Food/Shopping/Travel/Medical Expenses/other)"))
    amount = float(input("Enter expense amount -"))

    #store each expense
    expense = {
        "category" : category ,
        "amount" : amount
    }

    expenses.append(expense)

#Calculate total expenses
total = 0

for expense in expenses :
    total = total + expense["amount"]

#Display expense report
print("\n==========Smart Expense Report==========")

for expense in expenses:
    print(expense["category"] , "- Rs." , expense["amount"])

print("Total Expenses : Rs." , total)
print("monthly budget : Rs." , monthly_budget)
print("Remaining budget : Rs." , monthly_budget - total)

#Check budget status
if total > monthly_budget :
    print("warning! you exceeded your monthly budget.")
elif total == monthly_budget :
    print("you used your entire budget")
else :
    print("GOOD! you are within the budget")

#find the highest expense
if len(expenses) > 0 :
    highest_expense = expenses[0]

    for expense in expenses :
        if expense["amount"] > highest_expense["amount"] :
            highest_expense = expense

    print(
        "Highest Expense :",
        highest_expense["category"],
        "-Rs.",
        highest_expense["amount"]

    )

print("\nThank you for choosing Smart Expense Tracker")
print("\n====================================================")