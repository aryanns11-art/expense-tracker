import json
import os
import datetime as dt

FILE_NAME = "expenses.json"

expenses = []

def save_expenses():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)     #json.dump() ->  Converts Python data → JSON file | indent=4 -> Makes JSON readable

#--------------------------------------------------------------------------------------------------------------------------------------------

def load_expenses():
    global expenses

    if os.path.exists(FILE_NAME):

        try:
            with open(FILE_NAME, "r") as file:
                expenses = json.load(file)          # Reads JSON data from the file and converts it into Python objects.

        except json.JSONDecodeError:
            expenses = []

#--------------------------------------------------------------------------------------------------------------------------------------------

def add_expense():

    try:
        amount = float(input("Enter expense amount: "))
    except ValueError:
        print("Invalid amount")
        return

    category = input("Enter expense category: ")

    now = dt.datetime.now()

    expense = {
        "amount": amount,
        "category": category,
        "date": now.strftime("%d-%m-%Y"),                     
        "time": now.strftime("%H:%M:%S"),                     # % = “insert dynamic value here” . Without % = “just print text”
        "month": now.strftime("%B"),                          # strftime() → formats it into readable form 
        "year": now.strftime("%Y")
    }

    expenses.append(expense)
    save_expenses()
    print("Expense added successfully!")

#---------------------------------------------------------------------------------------------------------------------------------------------------

def view_all_expenses():
    if not expenses:
        print("No expenses recorded.")
    else:
        print("Expenses :")
        for index, expense in enumerate(expenses, start=1):
            print(f"{index} . {expense['date']} {expense['time']} - {expense['category']}: ₹{expense['amount']}") 

#-------------------------------------------------------------------------------------------------------------------------------------------------------

def view_expense(month, year):
    results = []

    for expense in expenses:
        if expense['month'].lower() == month.lower() and expense['year'] == year:
            results.append(expense)

    if not results:
        print(f"No expenses found for {month} {year}")
    else:
        for index, expense in enumerate(results, start=1):
            print(f"{index} . {expense['date']} {expense['time']} - {expense['category']}: ₹{expense['amount']}")            

#-------------------------------------------------------------------------------------------------------------------------------------------------------

def category_total_input():
    category = input("Enter category: ")
    total = 0
    found = False

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            total += expense["amount"]                                 
            found = True

    if not found:
        print(f"No expenses found for category '{category}'")
    else:
        print(f"Total for {category}: ₹{total}")   

#----------------------------------------------------------------------------------------------------------------------------------------------

def monthly_summary():

    summary = {}

    for expense in expenses:

        key = f"{expense['month']} {expense['year']}"

        if key not in summary:                       # If month is not already in dictionary -> create it with value 0
            summary[key] = 0

        summary[key] += expense["amount"]

    for month, total in summary.items():
        print(f"{month} : ₹{total}")

#------------------------------------------------------------------------------------------------------------------                 

def show_total_spending():

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total Spending: ₹{total}")        

#----------------------------------------------------------------------------------------------

def delete_expense():

    if not expenses:
        print("No expenses to delete.")
        return

    view_all_expenses()

    try:
        number = int(input("Enter expense number to delete: "))

        deleted = expenses.pop(number - 1)

        save_expenses()
        print(f"Deleted: {deleted['category']}")

    except ValueError:
        print("Invalid input.")
    except IndexError:
        print("Expense number does not exist.")  

#----------------------------------------------------------------------------------------------

def edit_expense():

    if not expenses:
        print("No expenses available.")
        return

    view_all_expenses()

    try:
        number = int(input("Enter expense number to edit: "))

        expense = expenses[number - 1]

        new_amount = float(input("Enter new amount: "))
        new_category = input("Enter new category: ")

        expense["amount"] = new_amount
        expense["category"] = new_category

        save_expenses()

        print("Expense updated successfully!")
    
    except:
        print("Invalid input.")

#---------------------------------------------------------------------------------------------------------------------------------                                         

load_expenses()

while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. View All Expenses")
    print("4. View Expenses By Month")
    print("5. Edit Expense")
    print("6. Show Total Spending")
    print("7. Category Total")
    print("8. Monthly Summary")
    print("9. Exit")

    choice = input("Enter choice: ")

    match choice:

        case "1":
            add_expense()

        case "2":
            delete_expense()

        case "3":
            view_all_expenses()

        case "4":
            month=input("Enter Month:")
            year=input("Enter Year:")
            view_expense(month,year)

        case "5":
            edit_expense()

        case "6":
            show_total_spending()    

        case "7":
            category_total_input()

        case "8":
            monthly_summary()
              
        case "9":
            print("Exiting...")
            break

        case _:
            print("Invalid choice")        

if __name__ == "__main__":
    main()            